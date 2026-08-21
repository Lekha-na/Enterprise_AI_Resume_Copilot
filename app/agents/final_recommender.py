from app.models.job import JobAnalysis
from app.models.match import MatchAnalysis
from app.models.profile import ProfileAnalysis
from app.models.recommendation import FinalRecommendation
from app.models.resume_optimization import ResumeOptimization
from app.models.skill_gap import SkillGap
from app.services.llm_service import ask_gemini


def generate_final_recommendation(
    candidate_profile: ProfileAnalysis,
    job_analysis: JobAnalysis,
    match_analysis: MatchAnalysis,
    skill_gaps: list[SkillGap],
    resume_optimizations: list[ResumeOptimization],
) -> FinalRecommendation:
    prompt = f"""
You are a professional career recommendation analyst.

Provide a final recommendation for the candidate based on
the information below.

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

Determine:
1. Overall match percentage from 0 to 100.
2. Application recommendation.
3. Key strengths.
4. Major gaps.
5. Priority improvements.

Do not invent candidate experience, skills, projects,
certifications, or achievements.

Base the recommendation only on the provided information.

Return only the structured information requested.
Do not return Markdown.
Do not add explanations or commentary outside the requested fields.
"""

    return ask_gemini(
        prompt,
        response_schema=FinalRecommendation,
    )