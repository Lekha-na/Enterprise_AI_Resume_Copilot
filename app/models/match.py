from pydantic import BaseModel, Field

class MatchAnalysis(BaseModel):
    matched_skills: list[str]
    missing_skills: list[str]
    match_percentage: float = Field(
        ge=0,
        le=100
    )
    overall_assessment: str