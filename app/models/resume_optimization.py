from pydantic import BaseModel, Field

class ResumeOptimization(BaseModel):
    section: str = Field(min_length=1)
    current_issue: str = Field(min_length=1)
    recommendation: str = Field(min_length=1)
    reason: str = Field(min_length=1)