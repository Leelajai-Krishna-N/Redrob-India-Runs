import unittest

from src.ranker.feature_engineering import extract_candidate_features, score_candidate
from src.ranker.reasoning_generator import generate_reasoning


def candidate(
    candidate_id,
    title,
    summary,
    career_description,
    skills,
    notice_period=30,
    consistency_points=0,
):
    return {
        "candidate_id": candidate_id,
        "profile": {
            "headline": title,
            "summary": summary,
            "country": "India",
            "years_of_experience": 6.0,
            "current_title": title,
            "current_company": "SearchWorks",
            "current_company_size": "501-1000",
            "current_industry": "Technology",
        },
        "career_history": [
            {
                "company": "SearchWorks",
                "title": title,
                "description": career_description,
                "duration_months": 48,
                "is_current": True,
                "company_size": "501-1000",
                "industry": "Technology",
            }
        ],
        "skills": [{"name": skill, "proficiency": "advanced", "endorsements": 10, "duration_months": 24} for skill in skills],
        "education": [],
        "redrob_signals": {
            "recruiter_response_rate": 0.8,
            "search_appearance_30d": 300,
            "saved_by_recruiters_30d": 18,
            "interview_completion_rate": 0.85,
            "profile_views_received_30d": 120,
            "notice_period_days": notice_period,
            "open_to_work_flag": True,
            "verified_email": True,
            "verified_phone": True,
        },
        "_forensic": {"raw_suspicion_points": consistency_points, "reason_codes": ""},
    }


class RankerV1Tests(unittest.TestCase):
    def test_career_evidence_beats_keyword_stuffed_skills(self):
        career_backed = candidate(
            "C1",
            "Search Engineer",
            "Builds search products.",
            "Owned learning to rank, BM25 retrieval, relevance evaluation, and search ranking pipelines.",
            ["Python", "Elasticsearch"],
        )
        skill_stuffed = candidate(
            "C2",
            "Accountant",
            "Finance professional curious about AI.",
            "Owned monthly close, statutory audit, GL controls, and tax filings.",
            ["LangChain", "RAG", "LLM Fine Tuning", "CUDA", "MLOps", "Pinecone"],
        )
        backed_score = score_candidate(extract_candidate_features(career_backed))
        stuffed_score = score_candidate(extract_candidate_features(skill_stuffed))
        self.assertGreater(backed_score.technical_score, stuffed_score.technical_score)
        self.assertGreater(stuffed_score.calibration_penalty, 0)

    def test_reasoning_only_mentions_detected_evidence(self):
        features = extract_candidate_features(
            candidate(
                "C3",
                "Search Engineer",
                "Relevance engineer.",
                "Built semantic search and ranking evaluation for product search.",
                ["Python"],
                notice_period=90,
            )
        )
        scored = score_candidate(features)
        reasoning = generate_reasoning(features, scored)
        self.assertIn("ranking", reasoning.lower())
        self.assertIn("notice period", reasoning.lower())
        self.assertNotIn("langchain", reasoning.lower())

    def test_severe_consistency_caps_final_score(self):
        features = extract_candidate_features(
            candidate(
                "C4",
                "Search Engineer",
                "Relevance engineer.",
                "Owned learning to rank and search infrastructure.",
                ["Elasticsearch", "Python"],
                consistency_points=30,
            )
        )
        scored = score_candidate(features)
        self.assertLessEqual(scored.final_score, 0.72)
        self.assertGreater(scored.consistency_penalty, 0)


if __name__ == "__main__":
    unittest.main()
