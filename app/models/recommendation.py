from pydantic import BaseModel


class FinalRecommendation(BaseModel):
    overall_match: float
    application_recommendation: str
    key_strengths: list[str]
    major_gaps: list[str]
    priority_improvements: list[str]