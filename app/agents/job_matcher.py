from app.models.job import JobAnalysis
from app.models.match import MatchAnalysis
from app.models.profile import ProfileAnalysis
from app.services.llm_service import ask_gemini


def match_candidate(
    candidate_profile: ProfileAnalysis,
    job_analysis: JobAnalysis,
) -> MatchAnalysis:
    prompt = f"""
You are a professional candidate-job matching analyst.

Compare the candidate profile with the job requirements.

Candidate Profile:
{candidate_profile}

Job Analysis:
{job_analysis}

Determine:
1. Skills that match.
2. Skills that are missing.
3. Overall match percentage from 0 to 100.
4. Overall assessment.

Calculate the match percentage based on the relevance of the
candidate's skills to the required and preferred job skills.

Return only the structured information requested.
Do not return Markdown.
Do not add explanations or commentary outside the requested fields.
"""

    return ask_gemini(
        prompt,
        response_schema=MatchAnalysis,
    )