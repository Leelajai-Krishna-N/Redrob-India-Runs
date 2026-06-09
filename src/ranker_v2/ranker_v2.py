from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.ranker_v2.evidence_tracing import EvidenceRecord
from src.ranker_v2.feature_extraction_v2 import (
    CandidateV2Features,
    ScoredCandidateV2,
    build_market_reference,
    extract_candidate_features_v2,
    score_candidate_v2,
)
from src.ranker_v2.reasoning_generator_v2 import generate_reasoning_v2


RANKER_VERSION = "ranker_v2"


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
VALIDATION_DIR = PROJECT_ROOT / "reports" / "v2_validation"
FORENSIC_SCORES_PATH = PROJECT_ROOT / "outputs" / "eda" / "forensic_audit" / "candidate_consistency_scores.csv"
GOLD_SET_PATH = PROJECT_ROOT / "reports" / "v1_hiring_committee_review" / "candidate_gold_set.csv"
COMMITTEE_REVIEW_PATH = PROJECT_ROOT / "reports" / "v1_hiring_committee_review" / "candidate_committee_review.csv"
V1_SCORING_PATH = PROJECT_ROOT / "outputs" / "ranker_v1" / "candidate_scoring.csv"


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
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not {"candidate_id", "raw_suspicion_points", "reason_codes"}.issubset(reader.fieldnames or []):
            return {}
        return {
            row["candidate_id"]: {
                "raw_suspicion_points": row.get("raw_suspicion_points", 0.0),
                "reason_codes": row.get("reason_codes", ""),
            }
            for row in reader
        }


def attach_forensic(candidate: dict[str, Any], forensic: dict[str, dict[str, Any]]) -> dict[str, Any]:
    candidate["_forensic"] = forensic.get(
        candidate.get("candidate_id", ""),
        {"raw_suspicion_points": 0.0, "reason_codes": ""},
    )
    return candidate


def score_candidates_v2(
    candidates: list[dict[str, Any]],
    forensic: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, CandidateV2Features]]:
    for candidate in candidates:
        attach_forensic(candidate, forensic)
    market_reference = build_market_reference(candidates)
    rows: list[dict[str, Any]] = []
    feature_by_id: dict[str, CandidateV2Features] = {}
    for candidate in candidates:
        features = extract_candidate_features_v2(candidate)
        scored = score_candidate_v2(features, market_reference)
        reasoning = generate_reasoning_v2(features, scored)
        feature_by_id[features.candidate_id] = features
        rows.append(scoring_row(features, scored, reasoning))
    rows.sort(
        key=lambda row: (
            -float(row["final_score"]),
            -float(row["search_ranking_score"]),
            -float(row["retrieval_score"]),
            -float(row["evaluation_score"]),
            -float(row["trust_score"]),
            row["candidate_id"],
        )
    )
    for idx, row in enumerate(rows, start=1):
        row["rank"] = idx
    return rows, feature_by_id


def scoring_row(features: CandidateV2Features, scored: ScoredCandidateV2, reasoning: str) -> dict[str, Any]:
    return {
        "rank": "",
        "candidate_id": scored.candidate_id,
        "search_ranking_score": scored.search_ranking_score,
        "retrieval_score": scored.retrieval_score,
        "evaluation_score": scored.evaluation_score,
        "recommendation_score": scored.recommendation_score,
        "vector_search_score": scored.vector_search_score,
        "behavioral_score": scored.behavioral_score,
        "trust_score": scored.trust_score,
        "trust_penalty": scored.trust_penalty,
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
        "relevant_duration_months": round(features.relevant_duration_months, 3),
        "max_evidence_level": features.max_evidence_level,
        "level4_5_count": features.level4_5_count,
        "search_ranking_evidence_count": features.evidence_counts.get("search_ranking", 0),
        "retrieval_evidence_count": features.evidence_counts.get("retrieval", 0),
        "evaluation_evidence_count": features.evidence_counts.get("evaluation", 0),
        "recommendation_evidence_count": features.evidence_counts.get("recommendation", 0),
        "vector_search_evidence_count": features.evidence_counts.get("vector_search", 0),
        "ownership_term_count": features.ownership_term_count,
        "scale_term_count": features.scale_term_count,
        "template_repetition": features.template_repetition,
        "keyword_stuffer": features.keyword_stuffer,
        "ai_transition": features.ai_transition,
        "consulting_only": features.consulting_only,
        "trust_points": round(features.trust_points, 3),
        "trust_reason_codes": "; ".join(features.trust_reason_codes),
        "consistency_points": features.consistency_points,
        "consistency_reason_codes": features.consistency_reason_codes,
    }


def write_outputs(
    candidates: list[dict[str, Any]],
    scoring: list[dict[str, Any]],
    feature_by_id: dict[str, CandidateV2Features],
    output_dir: Path,
    validation_dir: Path,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    validation_dir.mkdir(parents=True, exist_ok=True)
    write_csv(output_dir / "candidate_scoring.csv", scoring)
    top100 = scoring[:100]
    write_csv(output_dir / "top_100_candidates.csv", top100)
    write_evidence_traces(output_dir / "evidence_traces.csv", feature_by_id)
    (output_dir / "ranking_report.md").write_text(
        build_ranking_report(candidates, scoring, feature_by_id),
        encoding="utf-8",
    )
    write_validation_reports(scoring, validation_dir)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)


def write_evidence_traces(path: Path, feature_by_id: dict[str, CandidateV2Features]) -> None:
    fields = [
        "candidate_id",
        "feature_family",
        "matched_term",
        "source_type",
        "source_location",
        "company",
        "role_title",
        "snippet",
        "evidence_level",
        "contribution",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for cid in sorted(feature_by_id):
            for record in feature_by_id[cid].evidence_records:
                writer.writerow(evidence_record_row(record))


def evidence_record_row(record: EvidenceRecord) -> dict[str, Any]:
    return {
        "candidate_id": record.candidate_id,
        "feature_family": record.feature_family,
        "matched_term": record.matched_term,
        "source_type": record.source_type,
        "source_location": record.source_location,
        "company": record.company,
        "role_title": record.role_title,
        "snippet": record.snippet,
        "evidence_level": record.evidence_level,
        "contribution": record.contribution,
    }


def build_ranking_report(
    candidates: list[dict[str, Any]],
    scoring: list[dict[str, Any]],
    feature_by_id: dict[str, CandidateV2Features],
) -> str:
    by_id = {candidate["candidate_id"]: candidate for candidate in candidates}
    top_ids = [row["candidate_id"] for row in scoring[:100]]
    title_counts = Counter(by_id[cid].get("profile", {}).get("current_title", "") for cid in top_ids)
    skill_counts: Counter[str] = Counter()
    for cid in top_ids:
        skill_counts.update(skill.get("name", "") for skill in by_id[cid].get("skills", []))

    lines = [
        "# Ranker V2 Report",
        "",
        "## Summary",
        "- Deterministic, explainable scoring only: no LLM calls, embeddings, cross-encoders, external APIs, or neural models.",
        "- V2 replaces the broad V1 technical score with evidence-traced feature families.",
        "- Family weights emphasize search ranking, retrieval infrastructure, evaluation/relevance science, and conditional recommendation/matching evidence.",
        "- Trust is handled mostly with caps and reason-coded penalties, including template repetition.",
        "",
        "## Score Distributions",
        distribution_table(
            scoring,
            [
                "search_ranking_score",
                "retrieval_score",
                "evaluation_score",
                "recommendation_score",
                "behavioral_score",
                "trust_penalty",
                "final_score",
            ],
        ),
        "",
        "## Evidence-Level Summary",
        evidence_level_summary(scoring[:100]),
        "",
        "## Top 100 Current Titles",
    ]
    lines.extend([f"- `{title}`: {count}" for title, count in title_counts.most_common(100)])
    lines.extend(["", "## Top 100 Skills"])
    lines.extend([f"- `{skill}`: {count}" for skill, count in skill_counts.most_common(100)])
    lines.extend(["", "## Examples: Top-Ranked Candidates"])
    lines.extend(example_lines(scoring[:10], feature_by_id))
    lines.extend(["", "## Examples: Template-Repetition Caps"])
    repeated = [row for row in scoring if str(row.get("template_repetition")) == "True"][:10]
    lines.extend(example_lines(repeated, feature_by_id))
    lines.extend(["", "## Interpretation Notes"])
    lines.extend(
        [
            "- Level 4 and 5 evidence is rewarded more strongly than skill or headline mentions.",
            "- Recommendation evidence is strongest when paired with ranking, retrieval, or evaluation context.",
            "- Vector-search evidence is strongest when attached to retrieval or production context.",
            "- Behavioral score is a tie-breaker-sized feature, not the dominant relevance signal.",
        ]
    )
    return "\n".join(lines)


def distribution_table(scoring: list[dict[str, Any]], columns: list[str]) -> str:
    rows = []
    for column in columns:
        values = sorted(float(row[column]) for row in scoring)
        rows.append(
            [
                column,
                f"{percentile(values, 0):.4f}",
                f"{percentile(values, 25):.4f}",
                f"{percentile(values, 50):.4f}",
                f"{percentile(values, 75):.4f}",
                f"{percentile(values, 95):.4f}",
                f"{percentile(values, 100):.4f}",
            ]
        )
    return markdown_table(["metric", "min", "p25", "median", "p75", "p95", "max"], rows)


def percentile(values: list[float], percentile_value: float) -> float:
    if not values:
        return 0.0
    index = (len(values) - 1) * percentile_value / 100.0
    low = int(index)
    high = min(low + 1, len(values) - 1)
    if low == high:
        return values[low]
    return values[low] * (high - index) + values[high] * (index - low)


def evidence_level_summary(rows: list[dict[str, Any]]) -> str:
    counts = Counter(int(float(row["max_evidence_level"])) for row in rows)
    return markdown_table(
        ["max_evidence_level", "top100_count"],
        [[str(level), str(counts.get(level, 0))] for level in range(1, 6)],
    )


def example_lines(rows: list[dict[str, Any]], feature_by_id: dict[str, CandidateV2Features]) -> list[str]:
    if not rows:
        return ["- No examples found."]
    output: list[str] = []
    for row in rows:
        output.append(
            f"- `{row['candidate_id']}` final={float(row['final_score']):.4f}, "
            f"search={float(row['search_ranking_score']):.3f}, retrieval={float(row['retrieval_score']):.3f}, "
            f"eval={float(row['evaluation_score']):.3f}: {row['reasoning']}"
        )
        top_records = sorted(
            feature_by_id[row["candidate_id"]].evidence_records,
            key=lambda record: (-record.evidence_level, -record.contribution),
        )[:3]
        if top_records:
            output.append(
                "  Evidence: "
                + "; ".join(
                    f"{record.feature_family}:{record.matched_term}@L{record.evidence_level}"
                    for record in top_records
                )
            )
    return output


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    lines.extend("| " + " | ".join(str(value).replace("|", "/") for value in row) + " |" for row in rows)
    return "\n".join(lines)


def read_csv_by_id(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return {row["candidate_id"]: row for row in csv.DictReader(handle)}


def write_validation_reports(scoring: list[dict[str, Any]], validation_dir: Path) -> None:
    gold = read_csv_by_id(GOLD_SET_PATH)
    if not gold:
        return
    committee = read_csv_by_id(COMMITTEE_REVIEW_PATH)
    v1 = read_csv_by_id(V1_SCORING_PATH)
    v2 = {row["candidate_id"]: row for row in scoring}
    labels = ["ELITE", "STRONG", "MEDIUM", "WEAK"]

    comparison_rows = []
    for label in labels:
        ids = [cid for cid, row in gold.items() if row.get("gold_label") == label and cid in v2]
        comparison_rows.append(
            [
                label,
                str(len(ids)),
                f"{mean([float(v1[cid]['rank']) for cid in ids if cid in v1]):.1f}",
                f"{mean([float(v2[cid]['rank']) for cid in ids]):.1f}",
                f"{mean([float(v1[cid]['final_score']) for cid in ids if cid in v1]):.4f}",
                f"{mean([float(v2[cid]['final_score']) for cid in ids]):.4f}",
                str(sum(1 for cid in ids if float(v2[cid]["rank"]) <= 100)),
            ]
        )
    (validation_dir / "gold_set_comparison.md").write_text(
        "# Gold Set Comparison\n\n"
        + markdown_table(
            ["Gold", "Count", "Avg V1 Rank", "Avg V2 Rank", "Avg V1 Final", "Avg V2 Final", "V2 Top100 Count"],
            comparison_rows,
        )
        + "\n\nLower average rank is better for ELITE/STRONG; higher average rank is better for WEAK.",
        encoding="utf-8",
    )

    movement_rows = []
    for cid, gold_row in gold.items():
        if cid not in v1 or cid not in v2:
            continue
        v1_rank = int(float(v1[cid]["rank"]))
        v2_rank = int(float(v2[cid]["rank"]))
        movement_rows.append([cid, gold_row["gold_label"], str(v1_rank), str(v2_rank), str(v1_rank - v2_rank)])
    movement_rows.sort(key=lambda row: int(row[4]), reverse=True)
    (validation_dir / "rank_movement_analysis.md").write_text(
        "# Rank Movement Analysis\n\n"
        "Positive movement means the candidate moved up in V2.\n\n"
        "## Biggest Upward Moves\n\n"
        + markdown_table(["Candidate", "Gold", "V1 Rank", "V2 Rank", "Movement"], movement_rows[:25])
        + "\n\n## Biggest Downward Moves\n\n"
        + markdown_table(["Candidate", "Gold", "V1 Rank", "V2 Rank", "Movement"], list(reversed(movement_rows[-25:]))),
        encoding="utf-8",
    )

    elite_rows = [
        [
            cid,
            v1.get(cid, {}).get("rank", ""),
            v2[cid]["rank"],
            v2[cid]["final_score"],
            committee.get(cid, {}).get("candidate_family", ""),
            v2[cid]["reasoning"],
        ]
        for cid, row in gold.items()
        if row.get("gold_label") == "ELITE" and cid in v2
    ]
    elite_rows.sort(key=lambda row: int(float(row[2])))
    (validation_dir / "elite_candidate_analysis.md").write_text(
        "# Elite Candidate Analysis\n\n"
        + markdown_table(["Candidate", "V1 Rank", "V2 Rank", "V2 Final", "Family", "V2 Reasoning"], elite_rows),
        encoding="utf-8",
    )

    medium_weak = [cid for cid, row in gold.items() if row.get("gold_label") in {"MEDIUM", "WEAK"} and cid in v2 and cid in v1]
    fp_rows = [
        ["V1 medium/weak in Top 25", str(sum(1 for cid in medium_weak if float(v1[cid]["rank"]) <= 25))],
        ["V2 medium/weak in Top 25", str(sum(1 for cid in medium_weak if float(v2[cid]["rank"]) <= 25))],
        ["V1 medium/weak in Top 50", str(sum(1 for cid in medium_weak if float(v1[cid]["rank"]) <= 50))],
        ["V2 medium/weak in Top 50", str(sum(1 for cid in medium_weak if float(v2[cid]["rank"]) <= 50))],
    ]
    promoted_examples = sorted(medium_weak, key=lambda cid: float(v2[cid]["rank"]))[:20]
    (validation_dir / "false_promotion_reduction.md").write_text(
        "# False Promotion Reduction\n\n"
        + markdown_table(["Metric", "Count"], fp_rows)
        + "\n\n## Highest-Ranked Medium/Weak Candidates In V2\n\n"
        + markdown_table(
            ["Candidate", "Gold", "V1 Rank", "V2 Rank", "Trust Flags", "Reasoning"],
            [
                [
                    cid,
                    gold[cid]["gold_label"],
                    v1[cid]["rank"],
                    v2[cid]["rank"],
                    v2[cid]["trust_reason_codes"],
                    v2[cid]["reasoning"],
                ]
                for cid in promoted_examples
            ],
        ),
        encoding="utf-8",
    )

    elite_strong = [cid for cid, row in gold.items() if row.get("gold_label") in {"ELITE", "STRONG"} and cid in v2 and cid in v1]
    fs_rows = [
        ["V1 elite/strong outside Top 50", str(sum(1 for cid in elite_strong if float(v1[cid]["rank"]) > 50))],
        ["V2 elite/strong outside Top 50", str(sum(1 for cid in elite_strong if float(v2[cid]["rank"]) > 50))],
        ["V1 elite/strong outside Top 100", str(sum(1 for cid in elite_strong if float(v1[cid]["rank"]) > 100))],
        ["V2 elite/strong outside Top 100", str(sum(1 for cid in elite_strong if float(v2[cid]["rank"]) > 100))],
    ]
    suppressed_examples = sorted(elite_strong, key=lambda cid: float(v2[cid]["rank"]), reverse=True)[:20]
    (validation_dir / "false_suppression_reduction.md").write_text(
        "# False Suppression Reduction\n\n"
        + markdown_table(["Metric", "Count"], fs_rows)
        + "\n\n## Lowest-Ranked Elite/Strong Candidates In V2\n\n"
        + markdown_table(
            ["Candidate", "Gold", "V1 Rank", "V2 Rank", "Reasoning"],
            [[cid, gold[cid]["gold_label"], v1[cid]["rank"], v2[cid]["rank"], v2[cid]["reasoning"]] for cid in suppressed_examples],
        ),
        encoding="utf-8",
    )


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run deterministic Redrob Ranker V2.")
    parser.add_argument("--dataset", type=Path, default=DATASET_PATH)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--validation-dir", type=Path, default=VALIDATION_DIR)
    parser.add_argument("--limit", type=int, default=None, help="Optional row limit for smoke tests.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.dataset.exists():
        raise FileNotFoundError(f"Dataset not found: {args.dataset}")
    candidates = load_candidates(args.dataset, limit=args.limit)
    forensic = load_forensic_scores(FORENSIC_SCORES_PATH)
    scoring, feature_by_id = score_candidates_v2(candidates, forensic)
    write_outputs(candidates, scoring, feature_by_id, args.output_dir, args.validation_dir)
    print(f"Ranker V2 complete. Scored {len(scoring)} candidates. Outputs written to {args.output_dir}")


if __name__ == "__main__":
    main()

