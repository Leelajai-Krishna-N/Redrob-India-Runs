import unittest

from src.ranker_v2.feature_extraction_v2 import (
    extract_candidate_features_v2,
    score_candidate_v2,
)
from src.ranker_v2.reasoning_generator_v2 import generate_reasoning_v2


def candidate(
    candidate_id,
    title,
    summary,
    career_descriptions,
    skills,
    consistency_points=0,
    notice_period=30,
):
    if isinstance(career_descriptions, str):
        career_descriptions = [career_descriptions]
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
                "company": f"SearchWorks {idx}",
                "title": title,
                "description": description,
                "duration_months": 36,
                "is_current": idx == 0,
                "company_size": "501-1000",
                "industry": "Technology",
            }
            for idx, description in enumerate(career_descriptions)
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
            "expected_salary_range_inr_lpa": {"min": 30, "max": 45},
        },
        "_forensic": {"raw_suspicion_points": consistency_points, "reason_codes": ""},
    }


class RankerV2Tests(unittest.TestCase):
    def test_ownership_and_evaluation_beats_keyword_mentions(self):
        owned = candidate(
            "V2A",
            "Search Engineer",
            "Search relevance engineer.",
            "Owned a production ranking layer for candidate search serving 50M queries per month. "
            "Designed NDCG, MRR, recall@K, human judgments, and A/B testing for relevance evaluation.",
            ["Python", "Elasticsearch"],
        )
        mentioned = candidate(
            "V2B",
            "AI Engineer",
            "Interested in ranking retrieval recommendation embeddings and search.",
            "Built generic ML dashboards and model monitoring for churn prediction.",
            ["Ranking", "Retrieval", "NDCG", "Pinecone"],
        )
        owned_features = extract_candidate_features_v2(owned)
        mentioned_features = extract_candidate_features_v2(mentioned)
        owned_score = score_candidate_v2(owned_features)
        mentioned_score = score_candidate_v2(mentioned_features)
        self.assertGreater(owned_features.max_evidence_level, mentioned_features.max_evidence_level)
        self.assertGreater(owned_score.final_score, mentioned_score.final_score)
        self.assertGreater(owned_score.evaluation_score, mentioned_score.evaluation_score)

    def test_recommendation_needs_search_or_evaluation_context_for_full_credit(self):
        search_backed = candidate(
            "V2C",
            "Recommendation Systems Engineer",
            "Recommendation engineer.",
            "Owned recommendation systems with learning to rank, retrieval candidate generation, and offline evaluation.",
            ["Recommendation Systems"],
        )
        recommendation_only = candidate(
            "V2D",
            "Recommendation Systems Engineer",
            "Recommendation engineer.",
            "Worked on recommendations and personalization experiments for a consumer product.",
            ["Recommendation Systems"],
        )
        backed = score_candidate_v2(extract_candidate_features_v2(search_backed))
        only = score_candidate_v2(extract_candidate_features_v2(recommendation_only))
        self.assertGreater(backed.recommendation_score, only.recommendation_score)
        self.assertGreater(backed.search_ranking_score + backed.evaluation_score, only.search_ranking_score + only.evaluation_score)

    def test_template_repetition_creates_trust_cap(self):
        repeated_description = (
            "Owned the ranking layer for e-commerce search. Designed relevance labeling, NDCG, MRR, "
            "and A/B testing for the ranking system."
        )
        repeated = candidate(
            "V2E",
            "Search Engineer",
            "Search engineer.",
            [repeated_description, repeated_description],
            ["Python", "BM25"],
        )
        features = extract_candidate_features_v2(repeated)
        scored = score_candidate_v2(features)
        self.assertTrue(features.template_repetition)
        self.assertIn("template_repetition", features.trust_reason_codes)
        self.assertIsNotNone(scored.score_cap)

    def test_reasoning_uses_stored_evidence_and_concerns(self):
        features = extract_candidate_features_v2(
            candidate(
                "V2F",
                "Search Engineer",
                "Search relevance engineer.",
                "Built hybrid retrieval with BM25 and semantic search for product search.",
                ["Python"],
                notice_period=120,
            )
        )
        scored = score_candidate_v2(features)
        reasoning = generate_reasoning_v2(features, scored)
        self.assertIn("Retrieval", reasoning)
        self.assertIn("BM25", reasoning)
        self.assertIn("notice period", reasoning)
        self.assertNotIn("Pinecone", reasoning)


if __name__ == "__main__":
    unittest.main()

