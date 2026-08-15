from pydantic import BaseModel

class ResumeOptimization(BaseModel):
    section: str
    current_issue: str
    recommendation: str
    reason: str