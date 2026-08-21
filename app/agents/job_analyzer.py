from app.models.job import JobAnalysis, JobDescription
from app.services.llm_service import ask_gemini


def build_job_analysis_prompt(
    job_description: JobDescription,
) -> str:
    return f"""
You are a professional job description analyzer.

Analyze the following job description.

Job Title:
{job_description.job_title}

Company:
{job_description.company}

Description:
{job_description.description}

Required Skills:
{job_description.required_skills}

Preferred Skills:
{job_description.preferred_skills}

Required Experience:
{job_description.required_experience}

Responsibilities:
{job_description.responsibilities}

Extract:
1. Required skills.
2. Preferred skills.
3. Required experience.
4. Responsibilities.

Return only the structured information requested.
Do not return Markdown.
Do not add explanations or commentary outside the requested fields.
"""


def analyze_job(
    job_description: JobDescription,
) -> JobAnalysis:
    prompt = build_job_analysis_prompt(job_description)

    return ask_gemini(
        prompt,
        response_schema=JobAnalysis,
    )