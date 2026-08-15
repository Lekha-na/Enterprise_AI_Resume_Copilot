from pydantic import BaseModel

class SkillGap(BaseModel):
    skill: str
    importance: str
    reason: str
    recommendation: str