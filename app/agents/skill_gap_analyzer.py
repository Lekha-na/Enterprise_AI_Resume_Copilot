from app.models.job import JobAnalysis
from app.models.skill_gap import SkillGap
from app.services.llm_service import ask_gemini


def analyze_skill_gap(
    missing_skills: list[str],
    job_analysis: JobAnalysis,
) -> list[SkillGap]:
    prompt = f"""
You are a professional career skill-gap analyst.

Analyze the candidate's missing skills for the given job.

Missing Skills:
{missing_skills}

Job Analysis:
{job_analysis}

For each missing skill:
1. Explain its importance for the job.
2. Explain why the skill is relevant.
3. Recommend a practical way for the candidate to improve it.

Classify importance as exactly one of:
- High
- Medium
- Low

Return only the structured information requested.
Do not return Markdown.
Do not add explanations or commentary outside the requested fields.
"""

    return ask_gemini(
        prompt,
        response_schema=list[SkillGap],
    )