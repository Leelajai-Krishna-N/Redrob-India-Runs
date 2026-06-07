from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.ranker.feature_engineering import (
    CandidateFeatures,
    ScoredCandidate,
    build_market_reference,
    extract_candidate_features,
    score_candidate,
)
from src.ranker.reasoning_generator import generate_reasoning


RANKER_VERSION = "ranker_v1"


def find_project_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "data").exists() and (parent / "src").exists():
            return parent
    return Path(__file__).resolve().parents[2]


PROJECT_ROOT = find_project_root()
DATA_DIR = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "[PUB] India_runs_data_and_ai_challenge"
    / "[PUB] India_runs_data_and_ai_challenge"
    / "India_runs_data_and_ai_challenge"
)
DATASET_PATH = DATA_DIR / "candidates.jsonl"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / RANKER_VERSION
FORENSIC_SCORES_PATH = PROJECT_ROOT / "outputs" / "eda" / "forensic_audit" / "candidate_consistency_scores.csv"


def load_candidates(path: Path, limit: int | None = None) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for idx, line in enumerate(handle):
            if limit is not None and idx >= limit:
                break
            if line.strip():
                candidates.append(json.loads(line))
    return candidates


def load_forensic_scores(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    scores = pd.read_csv(path)
    required = {"candidate_id", "raw_suspicion_points", "reason_codes"}
    if not required.issubset(scores.columns):
        return {}
    return {
        str(row.candidate_id): {
            "raw_suspicion_points": row.raw_suspicion_points,
            "reason_codes": row.reason_codes,
        }
        for row in scores.itertuples(index=False)
    }


def attach_forensic(candidate: dict[str, Any], forensic: dict[str, dict[str, Any]]) -> dict[str, Any]:
    candidate["_forensic"] = forensic.get(candidate.get("candidate_id", ""), {"raw_suspicion_points": 0.0, "reason_codes": ""})
    return candidate


def score_candidates(candidates: list[dict[str, Any]], forensic: dict[str, dict[str, Any]]) -> tuple[pd.DataFrame, dict[str, CandidateFeatures]]:
    for candidate in candidates:
        attach_forensic(candidate, forensic)
    market_reference = build_market_reference(candidates)
    rows: list[dict[str, Any]] = []
    feature_by_id: dict[str, CandidateFeatures] = {}
    for candidate in candidates:
        features = extract_candidate_features(candidate)
        scored = score_candidate(features, market_reference)
        reasoning = generate_reasoning(features, scored)
        feature_by_id[features.candidate_id] = features
        rows.append(scoring_row(features, scored, reasoning))
    scoring = pd.DataFrame(rows).sort_values(["final_score", "technical_score", "career_score"], ascending=False)
    scoring.insert(0, "rank", range(1, len(scoring) + 1))
    return scoring, feature_by_id


def scoring_row(features: CandidateFeatures, scored: ScoredCandidate, reasoning: str) -> dict[str, Any]:
    return {
        "candidate_id": scored.candidate_id,
        "technical_score": scored.technical_score,
        "career_score": scored.career_score,
        "market_score": scored.market_score,
        "consistency_score": scored.consistency_score,
        "consistency_penalty": scored.consistency_penalty,
        "calibration_penalty": scored.calibration_penalty,
        "final_score": scored.final_score,
        "score_cap": scored.score_cap if scored.score_cap is not None else "",
        "reasoning": reasoning,
        "current_title": features.current_title,
        "current_company": features.current_company,
        "years_of_experience": features.years_of_experience,
        "skill_count": features.skill_count,
        "ai_skill_count": features.ai_skill_count,
        "relevant_role_count": features.relevant_role_count,
        "relevant_duration_months": features.relevant_duration_months,
        "career_ranking_evidence_count": features.career_ranking_evidence_count,
        "career_retrieval_evidence_count": features.career_retrieval_evidence_count,
        "keyword_stuffer": features.keyword_stuffer,
        "ai_transition": features.ai_transition,
        "consulting_only": features.consulting_only,
        "consistency_points": features.consistency_points,
        "consistency_reason_codes": features.consistency_reason_codes,
    }


def write_outputs(
    candidates: list[dict[str, Any]],
    scoring: pd.DataFrame,
    feature_by_id: dict[str, CandidateFeatures],
    output_dir: Path,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    scoring.to_csv(output_dir / "candidate_scoring.csv", index=False, quoting=csv.QUOTE_MINIMAL)
    top100 = scoring.head(100).copy()
    top100.to_csv(output_dir / "top_100_candidates.csv", index=False, quoting=csv.QUOTE_MINIMAL)
    report = build_ranking_report(candidates, scoring, feature_by_id)
    (output_dir / "ranking_report.md").write_text(report, encoding="utf-8")


def build_ranking_report(
    candidates: list[dict[str, Any]],
    scoring: pd.DataFrame,
    feature_by_id: dict[str, CandidateFeatures],
) -> str:
    by_id = {candidate["candidate_id"]: candidate for candidate in candidates}
    top_ids = scoring.head(100)["candidate_id"].tolist()
    title_counts = Counter()
    skill_counts = Counter()
    for cid in top_ids:
        candidate = by_id[cid]
        title_counts.update([candidate.get("profile", {}).get("current_title", "")])
        skill_counts.update(skill.get("name", "") for skill in candidate.get("skills", []))

    lines = [
        "# Ranker V1 Report",
        "",
        "## Summary",
        "- Deterministic, explainable scoring only: no LLM calls, embeddings, cross-encoders, external APIs, or neural models.",
        "- Scoring principle: when skill keywords conflict with demonstrated career evidence, career evidence is trusted more heavily.",
        "- Final score = 45% technical relevance + 25% career evidence + 20% market signal + 10% consistency, minus transparent calibration penalties.",
        "",
        "## Score Distributions",
        distribution_table(scoring, ["technical_score", "market_score", "consistency_penalty", "final_score"]),
        "",
        "## Top 100 Current Titles",
    ]
    lines.extend([f"- `{title}`: {count}" for title, count in title_counts.most_common(100)])
    lines.extend(["", "## Top 100 Skills"])
    lines.extend([f"- `{skill}`: {count}" for skill, count in skill_counts.most_common(100)])
    lines.extend(["", "## Examples: Top-Ranked Candidates"])
    lines.extend(example_lines(scoring.head(10), feature_by_id))
    lines.extend(["", "## Examples: AI-Transition Candidates"])
    lines.extend(example_lines(scoring[scoring["ai_transition"]].head(10), feature_by_id))
    lines.extend(["", "## Examples: Keyword Stuffers"])
    lines.extend(example_lines(scoring[scoring["keyword_stuffer"]].head(10), feature_by_id))
    lines.extend(["", "## Examples: Heavily Penalized Candidates"])
    lines.extend(example_lines(scoring.sort_values("consistency_penalty", ascending=False).head(10), feature_by_id))
    lines.extend(
        [
            "",
            "## Interpretation Notes",
            "- Tier A ranking/relevance evidence carries the largest technical weight.",
            "- Career descriptions carry more weight than summaries, skills, headlines, or titles.",
            "- Keyword stuffer and AI-transition penalties are modest but visible in `calibration_penalty`.",
            "- Severe forensic issues cap the final score; they do not remove candidates.",
        ]
    )
    return "\n".join(lines)


def distribution_table(scoring: pd.DataFrame, columns: list[str]) -> str:
    rows = []
    for col in columns:
        series = scoring[col].astype(float)
        rows.append(
            {
                "metric": col,
                "min": series.min(),
                "p25": series.quantile(0.25),
                "median": series.median(),
                "p75": series.quantile(0.75),
                "p95": series.quantile(0.95),
                "max": series.max(),
            }
        )
    return pd.DataFrame(rows).round(4).to_markdown(index=False)


def example_lines(rows: pd.DataFrame, feature_by_id: dict[str, CandidateFeatures]) -> list[str]:
    if rows.empty:
        return ["- No examples found."]
    output = []
    for row in rows.itertuples(index=False):
        features = feature_by_id[row.candidate_id]
        output.append(
            f"- `{row.candidate_id}` final={row.final_score:.4f}, tech={row.technical_score:.3f}, "
            f"career={row.career_score:.3f}, market={row.market_score:.3f}: {row.reasoning}"
        )
        top_terms = Counter(hit.term for hit in features.career_evidence_hits).most_common(4)
        if top_terms:
            output.append("  Career evidence terms: " + ", ".join(f"`{term}`" for term, _ in top_terms))
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run deterministic Redrob Ranker V1.")
    parser.add_argument("--dataset", type=Path, default=DATASET_PATH)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--limit", type=int, default=None, help="Optional row limit for quick local smoke tests.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.dataset.exists():
        raise FileNotFoundError(f"Dataset not found: {args.dataset}")
    candidates = load_candidates(args.dataset, limit=args.limit)
    forensic = load_forensic_scores(FORENSIC_SCORES_PATH)
    scoring, feature_by_id = score_candidates(candidates, forensic)
    write_outputs(candidates, scoring, feature_by_id, args.output_dir)
    print(f"Ranker V1 complete. Scored {len(scoring)} candidates. Outputs written to {args.output_dir}")


if __name__ == "__main__":
    main()
