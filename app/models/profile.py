from pydantic import BaseModel, Field

class CandidateProfile(BaseModel):
    name:str = Field(min_length=1)
    skills:list[str] = Field(min_length=1)
    experience:list[str]
    projects:list[str] = Field(min_length=1)
    education:str = Field(min_length=1)
    certifications:list[str]

class ProfileAnalysis(BaseModel):
    candidate_level: str
    primary_domain: str
    years_experience: float = Field(ge=0)
    key_skills: list[str]
    project_summary: str
    education_summary: str
    certification_summary: str