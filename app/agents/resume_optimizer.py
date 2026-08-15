from app.services.llm_service import ask_gemini
from app.models.resume_optimization import ResumeOptimization

def optimize_resume(candidate_profile: dict, job_analysis: dict):
    prompt= f"""
Analyze the candidate profile against the target job.

Candidate Profile:
{candidate_profile}

Job Analysis:
{job_analysis}

Identify areas where the resume could be improved.

For each recommendation:
- Identify the resume section
- Explain the current issue
- Give a specific recommendation
- Explain why the recommendation would help

Do not invent experience, skills, projects, certifications, or achievements.
Only recommend improvements based on information available in the candidate profile
and job requirements.
"""
    result=ask_gemini(prompt, response_schema=list[ResumeOptimization])
    return result