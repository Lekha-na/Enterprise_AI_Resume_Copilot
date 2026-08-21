from app.models.job import JobAnalysis
from app.models.profile import ProfileAnalysis
from app.models.resume_optimization import ResumeOptimization
from app.services.llm_service import ask_gemini


def optimize_resume(
    candidate_profile: ProfileAnalysis,
    job_analysis: JobAnalysis,
) -> list[ResumeOptimization]:
    prompt = f"""
You are a professional resume optimization specialist.

Analyze the candidate profile against the target job.

Candidate Profile:
{candidate_profile}

Job Analysis:
{job_analysis}

Identify areas where the resume could be improved.

For each recommendation:
1. Identify the resume section.
2. Explain the current issue.
3. Give a specific recommendation.
4. Explain why the recommendation would help.

Do not invent experience, skills, projects, certifications,
or achievements.

Only recommend improvements based on information available
in the candidate profile and job requirements.

Return only the structured information requested.
Do not return Markdown.
Do not add explanations or commentary outside the requested fields.
"""

    return ask_gemini(
        prompt,
        response_schema=list[ResumeOptimization],
    )