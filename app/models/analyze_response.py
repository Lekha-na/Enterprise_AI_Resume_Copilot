from pydantic import BaseModel

from app.models.profile import ProfileAnalysis
from app.models.job import JobAnalysis
from app.models.match import MatchAnalysis
from app.models.skill_gap import SkillGap
from app.models.resume_optimization import ResumeOptimization
from app.models.recommendation import FinalRecommendation


class AnalyzeResponse(BaseModel):
    profile_analysis: ProfileAnalysis
    job_analysis: JobAnalysis
    match_analysis: MatchAnalysis
    skill_gaps: list[SkillGap]
    resume_optimizations: list[ResumeOptimization]
    final_recommendation: FinalRecommendation