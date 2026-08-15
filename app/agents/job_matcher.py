from app.services.llm_service import ask_gemini
from app.models.match import MatchAnalysis

def match_candidate(candidate_profile: dict, job_analysis: dict):
    prompt= f"""
 Compare the candidate profile with the job requirements.
  Candidate Profile:
  {candidate_profile}

  Job Analysis:
  {job_analysis}

  Identify:
   - Skills that match
   - Skills that are missing
   - Overall match percentage
   - Overall assessment
"""
    result = ask_gemini(prompt, response_schema=MatchAnalysis)
    return result