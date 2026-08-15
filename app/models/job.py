from pydantic import BaseModel, Field

class JobDescription(BaseModel):
    job_title: str = Field(min_length=1)
    company: str = Field(min_length=1)
    description: str = Field(min_length=1)
    required_skills: list[str] = Field(min_length=1)
    preferred_skills: list[str]
    required_experience: str = Field(min_length=1)
    responsibilities: list[str] = Field(min_length=1)

class JobAnalysis(BaseModel):
    required_skills: list[str]
    preferred_skills: list[str]
    required_experience: str
    responsibilities: list[str]
