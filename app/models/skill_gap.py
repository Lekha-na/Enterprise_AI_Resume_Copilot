from pydantic import BaseModel, Field

class SkillGap(BaseModel):
    skill: str = Field(min_length=1)
    importance: str = Field(
        pattern="^(High|Medium|Low)$"
    )
    reason: str = Field(min_length=1)
    recommendation: str = Field(min_length=1)