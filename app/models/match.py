from pydantic import BaseModel

class MatchAnalysis(BaseModel):
    matched_skills: list[str]
    missing_skills: list[str]
    match_percentage: float
    overall_assessment: str