from pydantic import BaseModel, Field


class FinalRecommendation(BaseModel):
    overall_match: float = Field(
        ge=0,
        le=100
    )
    application_recommendation: str
    key_strengths: list[str]
    major_gaps: list[str]
    priority_improvements: list[str]