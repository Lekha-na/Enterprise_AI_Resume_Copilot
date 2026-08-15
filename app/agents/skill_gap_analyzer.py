from app.services.llm_service import ask_gemini
from app.models.skill_gap import SkillGap

def analyze_skill_gap(missing_skills: list[str], job_analysis: dict):
    prompt= f"""
Analyze the candidate's missing skills for the given job.

Missing Skills:
{missing_skills}

Job Analysis:
{job_analysis}

For each missing skill, explain:
- Its imporatnce for the job
- Why it is missing or relevant
- What the candidate should do to improve it
  """

    result = ask_gemini(prompt, response_schema=list[SkillGap])

    return result