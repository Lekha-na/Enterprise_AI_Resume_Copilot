from app.agents.final_recommender import generate_final_recommendation
from app.agents.job_analyzer import analyze_job as analyze_job_agent
from app.agents.job_matcher import match_candidate
from app.agents.profile_analyzer import analyze_profile as analyze_profile_agent
from app.agents.resume_optimizer import optimize_resume
from app.agents.skill_gap_analyzer import analyze_skill_gap

from app.models.analyze_response import AnalyzeResponse
from app.models.job import JobDescription
from app.models.profile import CandidateProfile


def analyze_resume(
    candidate: CandidateProfile | dict,
    job: JobDescription | dict,
) -> AnalyzeResponse:

    # Convert dictionaries to Pydantic models
    if isinstance(candidate, dict):
        candidate = CandidateProfile.model_validate(candidate)

    if isinstance(job, dict):
        job = JobDescription.model_validate(job)

    # 1. Analyze candidate profile
    profile_analysis = analyze_profile_agent(candidate)

    # 2. Analyze job description
    job_analysis = analyze_job_agent(job)

    # 3. Match candidate with job
    match_analysis = match_candidate(
        profile_analysis,
        job_analysis,
    )

    # 4. Analyze skill gaps
    skill_gaps = analyze_skill_gap(
        match_analysis.missing_skills,
        job_analysis,
    )

    # 5. Optimize resume
    resume_optimizations = optimize_resume(
        profile_analysis,
        job_analysis,
    )

    # 6. Generate final recommendation
    final_recommendation = generate_final_recommendation(
        profile_analysis,
        job_analysis,
        match_analysis,
        skill_gaps,
        resume_optimizations,
    )

    # 7. Return complete analysis
    return AnalyzeResponse(
        profile_analysis=profile_analysis,
        job_analysis=job_analysis,
        match_analysis=match_analysis,
        skill_gaps=skill_gaps,
        resume_optimizations=resume_optimizations,
        final_recommendation=final_recommendation,
    )