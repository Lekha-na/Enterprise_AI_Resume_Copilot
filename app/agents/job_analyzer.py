from app.services.llm_service import ask_gemini
from app.models.job import JobAnalysis

def analyze_job(job_description: str):
    prompt = f"""
    Analyze the following job description and extract the important information"
    job_description= {job_description}

    Exctract:
    Required skills
    Preferred skills
    Required experience
    Responsibilities
"""

    result = ask_gemini(prompt, response_schema=JobAnalysis)
    return result