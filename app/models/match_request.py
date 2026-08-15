from pydantic import BaseModel

from app.models.profile import CandidateProfile
from app.models.job import JobDescription

class MatchRequest(BaseModel):
    candidate: CandidateProfile
    job: JobDescription