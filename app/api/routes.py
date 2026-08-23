from fastapi import APIRouter

from app.agents.profile_analyzer import (
    analyze_profile as analyze_profile_agent
)
from app.agents.job_analyzer import (
    analyze_job as analyze_job_agent
)
from app.agents.job_matcher import match_candidate

from app.models.profile import CandidateProfile
from app.models.job import JobDescription
from app.models.match_request import MatchRequest
from app.models.analyze_response import AnalyzeResponse

from app.orchestrator.resume_analysis import analyze_resume


router = APIRouter()


@router.post(
    "/analyze-profile",
    summary="Analyze candidate profile",
    description=(
        "Analyzes a candidate profile and returns "
        "structured candidate information."
    ),
    response_description="Structured candidate profile analysis",
    tags=["Analysis"],
)
def analyze_profile_endpoint(
    profile: CandidateProfile
):
    return analyze_profile_agent(profile)


@router.post(
    "/analyze-job",
    summary="Analyze job description",
    description=(
        "Analyzes a job description and extracts "
        "required skills, preferred skills, experience, "
        "and responsibilities."
    ),
    response_description="Structured job description analysis",
    tags=["Analysis"],
)
def analyze_job_endpoint(
    job: JobDescription
):
    return analyze_job_agent(job)


@router.post(
    "/analyze-match",
    summary="Match candidate against a job",
    description=(
        "Compares a candidate profile against a job "
        "description and calculates the overall match."
    ),
    response_description="Candidate-job matching analysis",
    tags=["Analysis"],
)
def analyze_match_endpoint(
    request: MatchRequest
):
    profile_analysis = analyze_profile_agent(
        request.candidate
    )

    job_analysis = analyze_job_agent(
        request.job
    )

    match_analysis = match_candidate(
        profile_analysis,
        job_analysis
    )

    return match_analysis


@router.post(
    "/analyze",
    response_model=AnalyzeResponse,
    summary="Run complete resume analysis",
    description=(
        "Runs the complete AI Resume Copilot pipeline, "
        "including profile analysis, job analysis, matching, "
        "skill-gap analysis, resume optimization, and "
        "final recommendation."
    ),
    response_description="Complete resume analysis",
    tags=["Analysis"],
)
def analyze_endpoint(
    request: MatchRequest
):
    return analyze_resume(
        request.candidate,
        request.job
    )