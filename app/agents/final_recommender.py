from app.services.llm_service import ask_gemini
from app.models.recommendation import FinalRecommendation


def generate_final_recommendation(
    candidate_profile: dict,
    job_analysis: dict,
    match_analysis: dict,
    skill_gaps: list,
    resume_optimizations: list
):
    prompt = f"""
Provide a final recommendation for the candidate based on the information below.

Candidate Profile:
{candidate_profile}

Job Analysis:
{job_analysis}

Match Analysis:
{match_analysis}

Skill Gaps:
{skill_gaps}

Resume Optimizations:
{resume_optimizations}

Return:
- Overall match percentage
- Application recommendation
- Key strengths
- Major gaps
- Priority improvements

Do not invent candidate experience, skills, projects, certifications, or achievements.
Base the recommendation only on the provided information.
"""

    result = ask_gemini(
        prompt,
        response_schema=FinalRecommendation
    )

    return result