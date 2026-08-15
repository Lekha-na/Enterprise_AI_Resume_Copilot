from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.models.profile import CandidateProfile
from app.models.job import JobDescription
from app.models.match_request import MatchRequest
from app.models.analyze_response import AnalyzeResponse
from app.agents.profile_analyzer import analyze_profile as analyze_profile_agent
from app.agents.job_analyzer import analyze_job as analyze_job_agent
from app.agents.job_matcher import match_candidate
from app.agents.skill_gap_analyzer import analyze_skill_gap
from app.agents.resume_optimizer import optimize_resume
from app.agents.final_recommender import (
    generate_final_recommendation
)

app=FastAPI()

@app.exception_handler(RuntimeError)
async def runtime_error_handler(
    request: Request,
    exc: RuntimeError
):
    return JSONResponse(
        status_code=503,
        content={
            "error": "AI service unavailable",
            "message": str(exc)
        }
    )

@app.get("/")
def root():
  return{"message":"Enterprise AI Resume Copilot is running"}

@app.post("/analyze-profile")
def analyze_profile_endpoint(profile: CandidateProfile):
  return analyze_profile_agent(profile)

@app.post("/analyze-job")
def analyze_job_endpoint(job: JobDescription):
  return analyze_job_agent(job)

@app.post("/analyze-match")
def analyze_match_endpoint(request: MatchRequest):
   
   profile_analysis = analyze_profile_agent(request.candidate)

   job_analysis = analyze_job_agent(request.job)

   match_analysis = match_candidate(
        profile_analysis,
        job_analysis
    )
   return match_analysis

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_endpoint(request: MatchRequest):

    # 1. Analyze candidate profile
    profile_analysis = analyze_profile_agent(
        request.candidate
    )

    # 2. Analyze job description
    job_analysis = analyze_job_agent(
        request.job
    )

    # 3. Match candidate with job
    match_analysis = match_candidate(
        profile_analysis,
        job_analysis
    )

    # 4. Analyze skill gaps
    skill_gaps = analyze_skill_gap(
        match_analysis.missing_skills,
        job_analysis
    )

    # 5. Optimize resume
    resume_optimizations = optimize_resume(
        profile_analysis,
        job_analysis
    )

    # 6. Generate final recommendation
    final_recommendation = generate_final_recommendation(
        profile_analysis,
        job_analysis,
        match_analysis,
        skill_gaps,
        resume_optimizations
    )

    return {
        "profile_analysis": profile_analysis,
        "job_analysis": job_analysis,
        "match_analysis": match_analysis,
        "skill_gaps": skill_gaps,
        "resume_optimizations": resume_optimizations,
        "final_recommendation": final_recommendation
    }

  
  