import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.logging_config import configure_logging
from app.orchestrator.resume_analysis import analyze_resume

from app.models.profile import CandidateProfile
from app.models.job import JobDescription
from app.models.match_request import MatchRequest
from app.models.analyze_response import AnalyzeResponse

from app.agents.profile_analyzer import (
    analyze_profile as analyze_profile_agent
)
from app.agents.job_analyzer import (
    analyze_job as analyze_job_agent
)
from app.agents.job_matcher import match_candidate


# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------

configure_logging()

logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# FastAPI Application
# ---------------------------------------------------------

app = FastAPI(
    title="Enterprise AI Resume Copilot API",
    description=(
        "Production-ready AI-powered resume analysis and job matching API. "
        "The system analyzes candidate profiles, evaluates job descriptions, "
        "matches candidates against job requirements, identifies skill gaps, "
        "optimizes resumes, and generates final application recommendations "
        "using specialized AI agents powered by Google Gemini."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


# ---------------------------------------------------------
# Global Runtime Error Handler
# ---------------------------------------------------------

@app.exception_handler(RuntimeError)
async def runtime_error_handler(
    request: Request,
    exc: RuntimeError
):
    logger.error(
        "RuntimeError while processing %s %s: %s",
        request.method,
        request.url.path,
        exc,
    )

    return JSONResponse(
        status_code=503,
        content={
            "error": "AI service unavailable",
            "message": str(exc),
        },
    )


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.get(
    "/",
    summary="Health check",
    description=(
        "Checks whether the Enterprise AI Resume Copilot API "
        "is running and available."
    ),
    response_description="API availability status",
    tags=["Health"],
)
def root():
    return {
        "message": "Enterprise AI Resume Copilot is running"
    }


# ---------------------------------------------------------
# Profile Analysis
# ---------------------------------------------------------

@app.post(
    "/analyze-profile",
    summary="Analyze candidate profile",
    description=(
        "Analyzes a candidate profile using the AI profile "
        "analyzer and returns structured information about "
        "experience, domain, skills, projects, education, "
        "and certifications."
    ),
    response_description="Structured candidate profile analysis",
    tags=["Analysis"],
)
def analyze_profile_endpoint(
    profile: CandidateProfile
):
    return analyze_profile_agent(profile)


# ---------------------------------------------------------
# Job Analysis
# ---------------------------------------------------------

@app.post(
    "/analyze-job",
    summary="Analyze job description",
    description=(
        "Analyzes a job description and extracts required skills, "
        "preferred skills, experience requirements, and "
        "responsibilities."
    ),
    response_description="Structured job description analysis",
    tags=["Analysis"],
)
def analyze_job_endpoint(
    job: JobDescription
):
    return analyze_job_agent(job)


# ---------------------------------------------------------
# Candidate-Job Matching
# ---------------------------------------------------------

@app.post(
    "/analyze-match",
    summary="Match candidate against a job",
    description=(
        "Compares a candidate profile with a job description "
        "and identifies matched skills, missing skills, and "
        "an overall match percentage."
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


# ---------------------------------------------------------
# Complete Resume Analysis
# ---------------------------------------------------------

@app.post(
    "/analyze",
    response_model=AnalyzeResponse,
    summary="Run complete resume analysis",
    description=(
        "Runs the complete AI Resume Copilot pipeline including "
        "profile analysis, job analysis, candidate-job matching, "
        "skill-gap analysis, resume optimization, and final "
        "recommendation."
    ),
    response_description="Complete resume analysis result",
    tags=["Analysis"],
)
def analyze_endpoint(
    request: MatchRequest
):
    return analyze_resume(
        request.candidate,
        request.job
    )