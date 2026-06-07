from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import mutual_info_classif
from sklearn.preprocessing import StandardScaler

from run_redrob_eda import DATASET_PATH, JD_PATH, OUTPUT_DIR, load_candidates, normalize_text, read_docx_text


AUDIT_DIR = OUTPUT_DIR / "forensic_audit"
RANDOM_SEED = 42
TODAY = pd.Timestamp("2026-06-06")


DOMAIN_TERMS = {
    "ai_ml": {
        "ai",
        "ml",
        "machine learning",
        "deep learning",
        "llm",
        "nlp",
        "computer vision",
        "model",
        "fine-tuning",
        "fine tuning",
        "mlops",
        "tensorflow",
        "pytorch",
        "langchain",
        "rag",
        "embedding",
        "cuda",
        "feature engineering",
    },
    "data": {
        "data",
        "analytics",
        "analyst",
        "sql",
        "spark",
        "airflow",
        "warehouse",
        "etl",
        "bi",
        "tableau",
        "power bi",
        "statistics",
    },
    "software": {
        "software",
        "backend",
        "frontend",
        "full stack",
        "developer",
        "engineer",
        "java",
        "python",
        "javascript",
        "api",
        "microservices",
        "cloud",
        "devops",
    },
    "search_recs": {
        "search",
        "retrieval",
        "ranking",
        "recommendation",
        "recommender",
        "elasticsearch",
        "opensearch",
        "solr",
        "vector database",
        "faiss",
        "milvus",
        "qdrant",
        "pinecone",
        "rerank",
    },
    "design": {"designer", "graphic", "ux", "ui", "figma", "photoshop", "illustrator", "brand", "visual"},
    "finance": {"accountant", "finance", "financial", "audit", "tax", "bookkeeping", "accounts", "cpa"},
    "sales_marketing": {"sales", "marketing", "seo", "content", "campaign", "brand", "growth", "crm"},
    "support_ops": {"support", "customer", "operations", "ops", "process", "ticket", "service desk"},
    "hr": {"hr", "human resources", "recruiter", "talent", "payroll", "people operations"},
    "civil_mechanical": {"civil", "mechanical", "construction", "structural", "cad", "solidworks", "manufacturing"},
    "research": {"research", "scientist", "paper", "publication", "experiment", "lab"},
}
DOMAIN_REGEX_STRINGS = {
    domain: "|".join(re.escape(term) for term in sorted(terms, key=len, reverse=True))
    for domain, terms in DOMAIN_TERMS.items()
}
DOMAIN_PATTERNS = {domain: re.compile(pattern) for domain, pattern in DOMAIN_REGEX_STRINGS.items()}

AI_TERMS = DOMAIN_TERMS["ai_ml"] | DOMAIN_TERMS["search_recs"] | {
    "generative ai",
    "transformer",
    "hugging face",
    "openai",
    "prompt",
    "vector",
}
CONSULTING_TERMS = {
    "consultant",
    "consulting",
    "deloitte",
    "accenture",
    "pwc",
    "kpmg",
    "ey",
    "capgemini",
    "infosys",
    "tcs",
    "wipro",
    "cognizant",
}
JD_TERMS = {
    "retrieval",
    "ranking",
    "recommendation",
    "recommender",
    "search",
    "embedding",
    "vector",
    "faiss",
    "milvus",
    "qdrant",
    "pinecone",
    "elasticsearch",
    "opensearch",
    "evaluation",
    "ndcg",
    "mrr",
    "rerank",
    "rag",
}
DEGREE_ORDER = {
    "diploma": 0,
    "associate": 0,
    "bachelor": 1,
    "b.tech": 1,
    "b.e.": 1,
    "bsc": 1,
    "b.s.": 1,
    "master": 2,
    "m.tech": 2,
    "m.e.": 2,
    "msc": 2,
    "m.s.": 2,
    "mba": 2,
    "phd": 3,
    "ph.d": 3,
    "doctor": 3,
}


def ensure_dir() -> None:
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)


def contains_any(text: str, terms: set[str]) -> bool:
    return any(term in text for term in terms)


def term_count(text: str, terms: set[str]) -> int:
    return sum(1 for term in terms if term in text)


def domain_scores(text: str) -> dict[str, int]:
    norm = normalize_text(text)
    return {domain: len(pattern.findall(norm)) for domain, pattern in DOMAIN_PATTERNS.items()}


def dominant_domain(text: str) -> str:
    scores = domain_scores(text)
    best_domain, best_score = max(scores.items(), key=lambda item: item[1])
    return best_domain if best_score > 0 else "unknown"


def dominant_domains(series: pd.Series) -> pd.Series:
    norm = series.fillna("").map(normalize_text)
    score_frame = pd.DataFrame(index=series.index)
    for domain, pattern in DOMAIN_REGEX_STRINGS.items():
        score_frame[domain] = norm.str.count(pattern)
    max_scores = score_frame.max(axis=1)
    domains = score_frame.idxmax(axis=1)
    domains[max_scores <= 0] = "unknown"
    return domains


def first_matching_domains(series: pd.Series) -> pd.Series:
    norm = series.fillna("").map(normalize_text)
    domains = pd.Series("unknown", index=series.index, dtype="object")
    remaining = pd.Series(True, index=series.index)
    for domain, pattern in DOMAIN_REGEX_STRINGS.items():
        hits = remaining & norm.str.contains(pattern, regex=True, na=False)
        domains.loc[hits] = domain
        remaining.loc[hits] = False
    return domains


def degree_level(degree: Any) -> int | None:
    text = normalize_text(degree)
    for key, level in DEGREE_ORDER.items():
        if key in text:
            return level
    return None


def build_frames(candidates: list[dict[str, Any]]) -> dict[str, pd.DataFrame]:
    profiles, careers, skills, education, signals, texts = [], [], [], [], [], []
    raw_by_id = {}
    for cand in candidates:
        cid = cand["candidate_id"]
        raw_by_id[cid] = cand
        profile = cand.get("profile", {})
        profiles.append({"candidate_id": cid, **profile})
        text_parts = [profile.get("headline", ""), profile.get("summary", ""), profile.get("current_title", "")]
        for idx, role in enumerate(cand.get("career_history", [])):
            careers.append({"candidate_id": cid, "role_index": idx, **role})
            text_parts.extend([role.get("title", ""), role.get("description", ""), role.get("company", ""), role.get("industry", "")])
        for idx, skill in enumerate(cand.get("skills", [])):
            skills.append({"candidate_id": cid, "skill_index": idx, **skill})
            text_parts.append(skill.get("name", ""))
        for idx, edu in enumerate(cand.get("education", [])):
            education.append({"candidate_id": cid, "education_index": idx, **edu})
        signal = cand.get("redrob_signals", {}).copy()
        salary = signal.pop("expected_salary_range_inr_lpa", {}) or {}
        assessments = signal.pop("skill_assessment_scores", {}) or {}
        signal["expected_salary_min_lpa"] = salary.get("min")
        signal["expected_salary_max_lpa"] = salary.get("max")
        signal["skill_assessment_count"] = len(assessments)
        signal["skill_assessment_mean"] = float(np.mean(list(assessments.values()))) if assessments else np.nan
        signals.append({"candidate_id": cid, **signal})
        texts.append({"candidate_id": cid, "full_text": normalize_text(" ".join(text_parts))})

    frames = {
        "profiles": pd.DataFrame(profiles),
        "careers": pd.DataFrame(careers),
        "skills": pd.DataFrame(skills),
        "education": pd.DataFrame(education),
        "signals": pd.DataFrame(signals),
        "texts": pd.DataFrame(texts),
    }
    frames["raw_by_id"] = raw_by_id
    for col in ["signup_date", "last_active_date"]:
        frames["signals"][col] = pd.to_datetime(frames["signals"][col], errors="coerce")
    for col in ["start_date", "end_date"]:
        frames["careers"][col] = pd.to_datetime(frames["careers"][col], errors="coerce")
    return frames


def load_optional_labels() -> pd.DataFrame:
    candidates = []
    for path in Path.cwd().rglob("*.csv"):
        name = path.name.lower()
        if any(token in name for token in ["label", "sus", "manual", "review"]):
            try:
                df = pd.read_csv(path)
            except Exception:
                continue
            cols = {c.lower(): c for c in df.columns}
            if "candidate_id" in cols and any(c in cols for c in ["is_sus", "sus", "label", "manual_label"]):
                df = df.rename(columns={cols["candidate_id"]: "candidate_id"})
                for label_col in ["is_sus", "sus", "label", "manual_label"]:
                    if label_col in cols:
                        df = df.rename(columns={cols[label_col]: "label"})
                        candidates.append(df[["candidate_id", "label"]])
                        break
    if not candidates:
        return pd.DataFrame(columns=["candidate_id", "is_sus_label"])
    labels = pd.concat(candidates).drop_duplicates("candidate_id")
    labels["is_sus_label"] = labels["label"].astype(str).str.lower().isin(["1", "true", "sus", "suspicious", "yes"])
    return labels[["candidate_id", "is_sus_label"]]


def category_flags(frames: dict[str, pd.DataFrame], labels: pd.DataFrame) -> pd.DataFrame:
    profiles = frames["profiles"].copy()
    texts = frames["texts"].set_index("candidate_id")["full_text"]
    skills = frames["skills"].copy()
    skills["skill_norm"] = skills["name"].map(normalize_text)
    skill_text = skills.groupby("candidate_id")["skill_norm"].apply(lambda s: " ".join(s)).reindex(profiles["candidate_id"], fill_value="")
    current_titles = profiles.set_index("candidate_id")["current_title"].map(normalize_text)
    high_exp_threshold = profiles["years_of_experience"].quantile(0.95)
    flags = pd.DataFrame({"candidate_id": profiles["candidate_id"]}).set_index("candidate_id")
    flags["is_ai_title"] = current_titles.map(lambda t: contains_any(t, AI_TERMS)).reindex(flags.index, fill_value=False)
    flags["is_consulting"] = texts.map(lambda t: contains_any(t, CONSULTING_TERMS)).reindex(flags.index, fill_value=False)
    flags["is_high_experience"] = profiles.set_index("candidate_id")["years_of_experience"] >= high_exp_threshold
    flags["is_jd_aligned"] = (texts + " " + skill_text).map(lambda t: contains_any(t, JD_TERMS)).reindex(flags.index, fill_value=False)
    rng = np.random.default_rng(RANDOM_SEED)
    random_ids = rng.choice(flags.index.to_numpy(), size=min(5000, len(flags)), replace=False)
    flags["is_random_bucket"] = flags.index.isin(random_ids)

    prior_sus = set()
    for filename in ["suspicious_timeline_profiles.csv", "suspicious_skill_profiles.csv"]:
        path = OUTPUT_DIR / filename
        if path.exists():
            df = pd.read_csv(path)
            if "candidate_id" in df:
                prior_sus.update(df["candidate_id"].astype(str))
    flags["is_sus_proxy"] = flags.index.isin(prior_sus)
    if not labels.empty:
        flags = flags.join(labels.set_index("candidate_id")["is_sus_label"], how="left")
    else:
        flags["is_sus_label"] = np.nan
    flags.reset_index().to_csv(AUDIT_DIR / "category_flags.csv", index=False)
    return flags


def add_reason(store: dict[str, list[dict[str, Any]]], cid: str, code: str, severity: int, evidence: str) -> None:
    if sum(1 for item in store[cid] if item["code"] == code) >= 3:
        return
    store[cid].append({"code": code, "severity": severity, "evidence": evidence[:600]})


def text_has_domain_evidence(text: Any, domain: str) -> bool:
    if domain == "unknown":
        return False
    lowered = str(text).lower()
    return any(term in lowered for term in DOMAIN_TERMS[domain])


def lacks_domain_evidence(frame: pd.DataFrame) -> pd.Series:
    desc = frame["description"].fillna("").str.lower()
    lacks = frame["title_domain"].ne("unknown").copy()
    for domain, terms in DOMAIN_TERMS.items():
        mask = frame["title_domain"].eq(domain)
        if not mask.any():
            continue
        pattern = "|".join(re.escape(term) for term in sorted(terms, key=len, reverse=True))
        lacks.loc[mask] = ~desc.loc[mask].str.contains(pattern, regex=True, na=False)
    return lacks


def choose_audit_ids(flags: pd.DataFrame) -> set[str]:
    rng = np.random.default_rng(RANDOM_SEED)
    ids: set[str] = set()
    for col in ["is_sus_proxy", "is_sus_label", "is_ai_title", "is_high_experience"]:
        if col in flags:
            ids.update(flags.index[flags[col].fillna(False).astype(bool)])
    for col, cap in [("is_consulting", 3000), ("is_jd_aligned", 3000), ("is_random_bucket", 5000)]:
        candidates = flags.index[flags[col].fillna(False).astype(bool)].to_numpy()
        if len(candidates) > cap:
            candidates = rng.choice(candidates, size=cap, replace=False)
        ids.update(candidates)
    pd.DataFrame({"candidate_id": sorted(ids)}).to_csv(AUDIT_DIR / "audited_candidate_scope.csv", index=False)
    return ids


def consistency_checks(frames: dict[str, pd.DataFrame], flags: pd.DataFrame, audit_ids: set[str]) -> pd.DataFrame:
    profiles = frames["profiles"][frames["profiles"]["candidate_id"].isin(audit_ids)].set_index("candidate_id")
    careers = frames["careers"][frames["careers"]["candidate_id"].isin(audit_ids)].copy()
    education = frames["education"][frames["education"]["candidate_id"].isin(audit_ids)].copy()
    skills = frames["skills"][frames["skills"]["candidate_id"].isin(audit_ids)].copy()
    signals = frames["signals"][frames["signals"]["candidate_id"].isin(audit_ids)].set_index("candidate_id")
    texts = frames["texts"][frames["texts"]["candidate_id"].isin(audit_ids)].set_index("candidate_id")
    reasons: dict[str, list[dict[str, Any]]] = defaultdict(list)

    skills["skill_norm"] = skills["name"].map(normalize_text)
    skill_text = skills.groupby("candidate_id")["skill_norm"].apply(lambda s: " ".join(s))

    title_domain_map = {value: dominant_domain(value) for value in careers["title"].fillna("").unique()}
    current_title_domain_map = {value: dominant_domain(value) for value in profiles["current_title"].fillna("").unique()}
    careers["title_domain"] = careers["title"].fillna("").map(title_domain_map)
    current_roles = careers[careers["is_current"].astype(bool)].copy()
    current_mismatches = current_roles[lacks_domain_evidence(current_roles)]
    for row in current_mismatches.itertuples(index=False):
        add_reason(
            reasons,
            row.candidate_id,
            "current_title_description_mismatch",
            3,
            f"Current title `{row.title}` maps to {row.title_domain}, but description lacks matching domain evidence: {row.description}",
        )

    previous_roles = careers[~careers["is_current"].astype(bool)].copy()
    previous_mismatches = previous_roles[lacks_domain_evidence(previous_roles)]
    for row in previous_mismatches.itertuples(index=False):
        add_reason(
            reasons,
            row.candidate_id,
            "previous_title_description_mismatch",
            2,
            f"Previous title `{row.title}` maps to {row.title_domain}, but description lacks matching domain evidence: {row.description}",
        )

    for cid, group in careers.sort_values(["candidate_id", "start_date"]).groupby("candidate_id"):
        domains = group["title_domain"].tolist()
        known = [d for d in domains if d != "unknown"]
        if len(set(known)) >= 4:
            add_reason(reasons, cid, "abrupt_career_jumps", 4, " -> ".join(group["title"].fillna("").astype(str).tolist()))
        elif len(set(known)) == 3 and len(known) >= 3:
            add_reason(reasons, cid, "moderate_career_incoherence", 2, " -> ".join(group["title"].fillna("").astype(str).tolist()))

    if not education.empty:
        education["level"] = education["degree"].map(degree_level)
        for cid, group in education.sort_values(["candidate_id", "start_year"]).groupby("candidate_id"):
            valid = group.dropna(subset=["level", "start_year", "end_year"])
            if valid.empty:
                continue
            for row in valid.itertuples(index=False):
                if row.end_year < row.start_year:
                    add_reason(reasons, cid, "education_end_before_start", 5, f"{row.degree} at {row.institution}: {row.start_year}-{row.end_year}")
                if row.end_year - row.start_year > 12:
                    add_reason(reasons, cid, "unusually_long_education", 2, f"{row.degree} at {row.institution}: {row.start_year}-{row.end_year}")
            levels_by_start = valid["level"].tolist()
            if any(next_level < prev for prev, next_level in zip(levels_by_start, levels_by_start[1:])):
                add_reason(reasons, cid, "degree_order_reversal", 4, "; ".join(f"{r.degree} {r.start_year}-{r.end_year}" for r in valid.itertuples()))
            career_start = careers.loc[careers["candidate_id"].eq(cid), "start_date"].min()
            latest_grad = pd.to_numeric(valid["end_year"], errors="coerce").max()
            if pd.notna(career_start) and pd.notna(latest_grad) and latest_grad > career_start.year + 1:
                add_reason(reasons, cid, "graduation_after_employment_start", 3, f"First job starts {career_start.date()}, latest graduation year {int(latest_grad)}")

    temporal_bad = signals[signals["signup_date"] > signals["last_active_date"]]
    for cid, row in temporal_bad.iterrows():
        add_reason(reasons, cid, "signup_after_last_active", 5, f"signup_date={row.signup_date.date()}, last_active_date={row.last_active_date.date()}")
    future_dates = signals[signals["signup_date"] > TODAY]
    for cid, row in future_dates.iterrows():
        add_reason(reasons, cid, "signup_date_in_future", 3, f"signup_date={row.signup_date.date()}, audit_date={TODAY.date()}")
    future_active = signals[signals["last_active_date"] > TODAY]
    for cid, row in future_active.iterrows():
        add_reason(reasons, cid, "last_active_date_in_future", 4, f"last_active_date={row.last_active_date.date()}, audit_date={TODAY.date()}")

    salary = signals[["expected_salary_min_lpa", "expected_salary_max_lpa"]].apply(pd.to_numeric, errors="coerce")
    bad_salary = salary[salary["expected_salary_min_lpa"] > salary["expected_salary_max_lpa"]]
    for cid, row in bad_salary.iterrows():
        add_reason(reasons, cid, "salary_min_exceeds_max", 5, f"min={row.expected_salary_min_lpa}, max={row.expected_salary_max_lpa}")
    wide_salary = salary[(salary["expected_salary_max_lpa"] - salary["expected_salary_min_lpa"] > 80) | (salary["expected_salary_max_lpa"] > 250)]
    for cid, row in wide_salary.iterrows():
        add_reason(reasons, cid, "unrealistic_salary_range", 2, f"min={row.expected_salary_min_lpa}, max={row.expected_salary_max_lpa}")

    skill_domain_by_skill = {value: dominant_domain(value) for value in skills["skill_norm"].fillna("").unique()}
    skills["skill_domain"] = skills["skill_norm"].map(skill_domain_by_skill)
    skill_domains = (
        skills[skills["skill_domain"].ne("unknown")]
        .groupby("candidate_id")["skill_domain"]
        .agg(lambda s: s.value_counts().index[0] if not s.empty else "unknown")
    )
    career_domains = (
        careers[careers["title_domain"].ne("unknown")]
        .groupby("candidate_id")["title_domain"]
        .agg(lambda s: s.value_counts().index[0] if not s.empty else "unknown")
    )
    headline_domain_map = {value: dominant_domain(value) for value in profiles["headline"].fillna("").unique()}
    profile_domains = pd.DataFrame(index=profiles.index)
    profile_domains["title_domain"] = profiles["current_title"].fillna("").map(current_title_domain_map)
    profile_domains["headline_domain"] = profiles["headline"].fillna("").map(headline_domain_map)
    profile_domains["skills_domain"] = skill_domains.reindex(profiles.index, fill_value="unknown")
    profile_domains["career_domain"] = career_domains.reindex(profiles.index, fill_value="unknown")
    domain_mismatch_rows = profile_domains[
        profile_domains["skills_domain"].ne("unknown")
        & profile_domains["title_domain"].ne("unknown")
        & profile_domains["skills_domain"].ne(profile_domains["title_domain"])
    ]
    for cid, row in domain_mismatch_rows.iterrows():
        current_title = profiles.at[cid, "current_title"]
        title_domain = row["title_domain"]
        skills_domain = row["skills_domain"]
        add_reason(reasons, cid, "skills_current_role_mismatch", 2, f"title=`{current_title}` ({title_domain}), dominant skills={skills_domain}")

    headline_mismatch_rows = profile_domains[
        profile_domains["headline_domain"].ne("unknown")
        & profile_domains["skills_domain"].ne("unknown")
        & profile_domains["headline_domain"].ne(profile_domains["skills_domain"])
    ]
    for cid, row in headline_mismatch_rows.iterrows():
        headline = profiles.at[cid, "headline"]
        add_reason(
            reasons,
            cid,
            "skills_headline_mismatch",
            1,
            f"headline=`{headline}` ({row['headline_domain']}), dominant skills={row['skills_domain']}",
        )

    career_mismatch_rows = profile_domains[
        profile_domains["skills_domain"].ne("unknown")
        & profile_domains["career_domain"].ne("unknown")
        & profile_domains["skills_domain"].ne(profile_domains["career_domain"])
        & profile_domains["title_domain"].ne("ai_ml")
    ]
    for cid, row in career_mismatch_rows.iterrows():
        add_reason(
            reasons,
            cid,
            "skills_career_history_mismatch",
            1,
            f"career text domain={row['career_domain']}, dominant skills={row['skills_domain']}",
        )

    for cid in flags.index[flags["is_ai_title"] & flags.index.isin(audit_ids)]:
        text = texts.at[cid, "full_text"]
        ai_skill_hits = term_count(skill_text.get(cid, ""), AI_TERMS)
        ai_desc_hits = term_count(text, AI_TERMS)
        if ai_skill_hits < 2 or ai_desc_hits < 3:
            add_reason(reasons, cid, "ai_title_weak_ai_evidence", 4, f"ai_skill_hits={ai_skill_hits}, ai_text_hits={ai_desc_hits}, title={profiles.at[cid, 'current_title']}")

    rows = []
    for cid in profiles.index:
        items = reasons.get(cid, [])
        raw_score = sum(item["severity"] for item in items)
        score_10 = min(10.0, round(raw_score / 3.0, 1))
        rows.append(
            {
                "candidate_id": cid,
                "suspicion_score_10": score_10,
                "raw_suspicion_points": raw_score,
                "reason_count": len(items),
                "reason_codes": "; ".join(item["code"] for item in items),
                "evidence": " || ".join(f"{item['code']}: {item['evidence']}" for item in items[:8]),
            }
        )
    out = pd.DataFrame(rows).sort_values(["suspicion_score_10", "raw_suspicion_points", "reason_count"], ascending=False)
    out.to_csv(AUDIT_DIR / "candidate_consistency_scores.csv", index=False)
    return out


def feature_table(frames: dict[str, pd.DataFrame], flags: pd.DataFrame, consistency: pd.DataFrame) -> pd.DataFrame:
    profiles = frames["profiles"].set_index("candidate_id")
    signals = frames["signals"].set_index("candidate_id")
    skills = frames["skills"]
    careers = frames["careers"]
    education = frames["education"]

    features = pd.DataFrame(index=profiles.index)
    features["years_of_experience"] = pd.to_numeric(profiles["years_of_experience"], errors="coerce")
    features["skill_count"] = skills.groupby("candidate_id").size().reindex(features.index, fill_value=0)
    features["career_role_count"] = careers.groupby("candidate_id").size().reindex(features.index, fill_value=0)
    features["education_count"] = education.groupby("candidate_id").size().reindex(features.index, fill_value=0)
    for col in [
        "profile_completeness_score",
        "recruiter_response_rate",
        "search_appearance_30d",
        "saved_by_recruiters_30d",
        "interview_completion_rate",
        "offer_acceptance_rate",
        "github_activity_score",
        "expected_salary_min_lpa",
        "expected_salary_max_lpa",
        "skill_assessment_count",
    ]:
        features[col] = pd.to_numeric(signals[col], errors="coerce")
    features["salary_mid_lpa"] = (features["expected_salary_min_lpa"] + features["expected_salary_max_lpa"]) / 2
    features["salary_range_lpa"] = features["expected_salary_max_lpa"] - features["expected_salary_min_lpa"]
    features["days_since_last_active"] = (TODAY - signals["last_active_date"]).dt.days
    consistency_idx = consistency.set_index("candidate_id")
    features["consistency_suspicion_score_10"] = consistency_idx["suspicion_score_10"].reindex(features.index, fill_value=0)
    features["consistency_reason_count"] = consistency_idx["reason_count"].reindex(features.index, fill_value=0)
    for col in flags.columns:
        features[col] = flags[col]
    features = features.reset_index().rename(columns={"index": "candidate_id"})
    features.to_csv(AUDIT_DIR / "forensic_feature_table.csv", index=False)
    return features


def category_comparisons(features: pd.DataFrame) -> None:
    buckets = {
        "AI-title": "is_ai_title",
        "Consulting": "is_consulting",
        "High-experience": "is_high_experience",
        "JD-aligned": "is_jd_aligned",
        "Random": "is_random_bucket",
        "Sus-proxy": "is_sus_proxy",
    }
    metrics = [
        "years_of_experience",
        "salary_mid_lpa",
        "salary_range_lpa",
        "skill_count",
        "profile_completeness_score",
        "recruiter_response_rate",
        "search_appearance_30d",
        "saved_by_recruiters_30d",
        "interview_completion_rate",
        "offer_acceptance_rate",
    ]
    rows = []
    for bucket, flag in buckets.items():
        subset = features[features[flag].fillna(False).astype(bool)]
        for metric in metrics:
            s = pd.to_numeric(subset[metric], errors="coerce").dropna()
            rows.append(
                {
                    "bucket": bucket,
                    "metric": metric,
                    "candidate_count": len(subset),
                    "mean": s.mean(),
                    "median": s.median(),
                    "p25": s.quantile(0.25) if not s.empty else np.nan,
                    "p75": s.quantile(0.75) if not s.empty else np.nan,
                    "p95": s.quantile(0.95) if not s.empty else np.nan,
                }
            )
    out = pd.DataFrame(rows)
    out.to_csv(AUDIT_DIR / "category_comparison_tables.csv", index=False)


def hidden_signal_analysis(features: pd.DataFrame) -> None:
    targets = {
        "is_sus_proxy": "Suspicion proxy",
        "is_jd_aligned": "JD alignment",
        "is_ai_title": "AI-title",
    }
    exclude = {"candidate_id", "is_sus_label"}
    X = features.drop(columns=[c for c in exclude if c in features], errors="ignore").copy()
    for col in X.columns:
        if X[col].dtype == "object":
            X[col] = X[col].astype(str).str.lower().isin(["true", "1"])
    X = X.apply(pd.to_numeric, errors="coerce").fillna(0)
    rows = []
    corr_rows = []
    for target, label in targets.items():
        if target not in X or X[target].nunique() < 2:
            continue
        y = X[target].astype(int)
        feature_cols = [c for c in X.columns if c not in targets and c != target]
        X_target = X[feature_cols]
        mi = mutual_info_classif(X_target, y, random_state=RANDOM_SEED, discrete_features="auto")
        rf = RandomForestClassifier(n_estimators=160, max_depth=8, random_state=RANDOM_SEED, n_jobs=-1, class_weight="balanced")
        rf.fit(X_target, y)
        for col, mi_value, importance in zip(feature_cols, mi, rf.feature_importances_):
            rows.append({"target": label, "feature": col, "mutual_information": mi_value, "rf_importance": importance})
            corr_rows.append({"target": label, "feature": col, "correlation": X_target[col].corr(y)})
    pd.DataFrame(rows).sort_values(["target", "rf_importance"], ascending=[True, False]).to_csv(
        AUDIT_DIR / "hidden_signal_feature_importance.csv", index=False
    )
    pd.DataFrame(corr_rows).sort_values(["target", "correlation"], ascending=[True, False]).to_csv(
        AUDIT_DIR / "hidden_signal_correlations.csv", index=False
    )


def generator_artifacts(frames: dict[str, pd.DataFrame]) -> dict[str, Any]:
    profiles = frames["profiles"]
    careers = frames["careers"]
    skills = frames["skills"].copy()
    education = frames["education"]
    artifacts = {}
    for name, series in {
        "summary": profiles["summary"].map(normalize_text),
        "headline": profiles["headline"].map(normalize_text),
        "role_description": careers["description"].map(normalize_text),
    }.items():
        counts = series.value_counts()
        artifacts[name] = counts[counts > 1].head(25)
    path_counts = careers.sort_values(["candidate_id", "start_date"]).groupby("candidate_id")["title"].apply(
        lambda s: " -> ".join(normalize_text(x) for x in s)
    )
    artifacts["career_paths"] = path_counts.value_counts().head(25)
    skills["skill_norm"] = skills["name"].map(normalize_text)
    bundles = skills.groupby("candidate_id")["skill_norm"].apply(lambda s: " | ".join(sorted(set(s))))
    artifacts["skill_bundles"] = bundles.value_counts().head(25)
    edu_patterns = education.groupby("candidate_id").apply(
        lambda g: " | ".join(f"{normalize_text(r.degree)}:{normalize_text(r.field_of_study)}:{r.start_year}-{r.end_year}" for r in g.itertuples()),
        include_groups=False,
    )
    artifacts["education_patterns"] = edu_patterns.value_counts().head(25)

    lines = ["# Generator Artifact Investigation", ""]
    lines.append("The evidence points to synthetic generation when exact text, paths, or bundles repeat across many profiles.")
    for section, counts in artifacts.items():
        lines.extend(["", f"## Repeated {section.replace('_', ' ').title()}"])
        if counts.empty:
            lines.append("- No repeated values found in the top scan.")
        else:
            for value, count in counts.items():
                lines.append(f"- Count {int(count)}: `{str(value)[:280]}`")
    (AUDIT_DIR / "generator_artifacts_report.md").write_text("\n".join(lines), encoding="utf-8")
    return artifacts


def write_scoring_framework() -> None:
    lines = [
        "# Suspicion Scoring Framework",
        "",
        "This is an explainability framework, not a model and not a ground-truth label definition.",
        "",
        "| Signal | Points | Justification |",
        "|---|---:|---|",
        "| Signup date after last active date | +5 | Impossible platform chronology. |",
        "| Salary minimum exceeds maximum | +5 | Impossible compensation range. |",
        "| Education end before start | +5 | Impossible education timeline. |",
        "| Abrupt career jumps across 4+ unrelated domains | +4 | Strong evidence of random/template mixing. |",
        "| Degree order reversal | +4 | Master's/PhD chronology contradicts normal progression. |",
        "| AI-title with weak AI evidence | +4 | Title appears unsupported by skills/work text. |",
        "| Current title-description mismatch | +3 | Current role label contradicts described work. |",
        "| Graduation after employment start | +3 | Possible overlap or chronology issue. |",
        "| Previous title-description mismatch | +2 | Historical role label contradicts described work. |",
        "| Skills-current-role mismatch | +2 | Skill bundle appears sampled from another archetype. |",
        "| Unrealistic salary range | +2 | Possible numeric generator artifact. |",
        "| Skills-headline or skills-career mismatch | +1 | Weak inconsistency signal, useful only with other evidence. |",
        "",
        "Scores are capped to 10 for reporting. Raw points are preserved in CSV outputs.",
    ]
    (AUDIT_DIR / "suspicion_scoring_framework.md").write_text("\n".join(lines), encoding="utf-8")


def suspicious_explanations(consistency: pd.DataFrame, flags: pd.DataFrame) -> None:
    sus_ids = set(flags.index[flags["is_sus_proxy"]])
    if "is_sus_label" in flags and flags["is_sus_label"].notna().any():
        sus_ids |= set(flags.index[flags["is_sus_label"].fillna(False)])
    subset = consistency[consistency["candidate_id"].isin(sus_ids)].sort_values(
        ["suspicion_score_10", "raw_suspicion_points"], ascending=False
    )
    lines = [
        "# Suspicious Candidate Explanations",
        "",
        "Uses manual labels if available; otherwise uses the prior EDA suspicious timeline/skill flags as `is_sus_proxy`.",
        "",
    ]
    for row in subset.itertuples(index=False):
        lines.extend(
            [
                f"## Candidate ID: {row.candidate_id}",
                "",
                f"Suspicion Score: {row.suspicion_score_10}/10",
                "",
                "Reasons:",
            ]
        )
        codes = [c for c in str(row.reason_codes).split("; ") if c]
        if codes:
            lines.extend([f"- {code.replace('_', ' ')}" for code in codes])
        else:
            lines.append("- No additional forensic inconsistency found; prior sus proxy should be manually validated.")
        lines.extend(["", "Evidence:", str(row.evidence) if row.evidence else "No direct evidence generated by the rule set.", ""])
    (AUDIT_DIR / "suspicious_candidate_explanations.md").write_text("\n".join(lines), encoding="utf-8")


def ranked_outputs(consistency: pd.DataFrame) -> None:
    top_sus = consistency.sort_values(["suspicion_score_10", "raw_suspicion_points", "reason_count"], ascending=False).head(50)
    realistic = consistency.sort_values(["suspicion_score_10", "raw_suspicion_points", "reason_count"], ascending=True).head(50)
    top_sus.to_csv(AUDIT_DIR / "top_50_most_suspicious_candidates.csv", index=False)
    realistic.to_csv(AUDIT_DIR / "top_50_most_realistic_candidates.csv", index=False)


def audit_report(features: pd.DataFrame, consistency: pd.DataFrame, flags: pd.DataFrame) -> None:
    cat = pd.read_csv(AUDIT_DIR / "category_comparison_tables.csv")
    importance = pd.read_csv(AUDIT_DIR / "hidden_signal_feature_importance.csv")
    total = len(features)
    deep_scope = len(consistency)
    severe = int((consistency["suspicion_score_10"] >= 8).sum())
    medium = int(((consistency["suspicion_score_10"] >= 4) & (consistency["suspicion_score_10"] < 8)).sum())
    label_note = (
        "Manual sus labels were found and merged."
        if flags["is_sus_label"].notna().any()
        else "No separate manual sus-label CSV was found; sus analysis uses prior EDA suspicious flags as a proxy."
    )
    lines = [
        "# Dataset Forensic Audit Report",
        "",
        "## Executive Summary",
        f"- Full-dataset feature rows analyzed: {total}",
        f"- Deep consistency audit scope: {deep_scope}",
        f"- Severe rule-based suspicion score >= 8 within deep scope: {severe}",
        f"- Medium rule-based suspicion score 4-7.9 within deep scope: {medium}",
        f"- {label_note}",
        "- The scoring framework validates suspiciousness with evidence; it does not assume labels are correct.",
        "",
        "## Major Anomalies",
    ]
    reason_counts = Counter()
    for codes in consistency["reason_codes"].fillna(""):
        reason_counts.update([c for c in codes.split("; ") if c])
    lines.extend([f"- `{reason}`: {count}" for reason, count in reason_counts.most_common(15)])
    lines.extend(["", "## Category Comparisons", "Median values by bucket for key metrics:"])
    pivot = cat.pivot_table(index="bucket", columns="metric", values="median", aggfunc="first")
    lines.append(pivot.round(3).to_markdown())
    lines.extend(["", "## Hidden Signals", "Top Random Forest predictors by target:"])
    for target, group in importance.groupby("target"):
        lines.append(f"### {target}")
        for row in group.sort_values("rf_importance", ascending=False).head(8).itertuples(index=False):
            lines.append(f"- `{row.feature}`: importance={row.rf_importance:.4f}, MI={row.mutual_information:.4f}")
    lines.extend(
        [
            "",
            "## Suspected Generator Weaknesses",
            "- Exact repeated text, repeated career paths, repeated education patterns, and repeated skill bundles are reported separately in `generator_artifacts_report.md`.",
            "- Cross-domain role/description mismatches suggest random field sampling or imperfect template stitching.",
            "- Weak AI evidence under AI titles suggests title templates may be assigned independently from skills or work descriptions.",
            "",
            "## Confidence Levels",
            "- High confidence: impossible date relationships, salary min/max inversions, education end-before-start.",
            "- Medium confidence: role-description mismatch and abrupt career jumps, because taxonomy rules are approximate.",
            "- Low-to-medium confidence: skill mismatch, because multi-disciplinary profiles can be legitimate.",
        ]
    )
    (AUDIT_DIR / "dataset_audit_report.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ensure_dir()
    candidates = load_candidates(DATASET_PATH)
    print("Loaded candidates", flush=True)
    frames = build_frames(candidates)
    print("Built normalized frames", flush=True)
    labels = load_optional_labels()
    flags = category_flags(frames, labels)
    print("Computed category flags", flush=True)
    audit_ids = choose_audit_ids(flags)
    print(f"Selected {len(audit_ids)} candidates for deep consistency audit", flush=True)
    consistency = consistency_checks(frames, flags, audit_ids)
    print("Computed consistency checks", flush=True)
    features = feature_table(frames, flags, consistency)
    print("Built feature table", flush=True)
    category_comparisons(features)
    print("Wrote category comparisons", flush=True)
    hidden_signal_analysis(features)
    print("Computed hidden signal analysis", flush=True)
    generator_artifacts(frames)
    print("Investigated generator artifacts", flush=True)
    write_scoring_framework()
    suspicious_explanations(consistency, flags)
    ranked_outputs(consistency)
    audit_report(features, consistency, flags)
    print(f"Forensic audit complete. Outputs written to {AUDIT_DIR}")


if __name__ == "__main__":
    main()
