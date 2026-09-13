from pydantic import BaseModel
from typing import List


class JobDescription(BaseModel):
    job_title: str
    company: str
    location: str
    department: str
    experience: str
    skills: List[str] = []
    education: List[str] = []
    responsibilities: List[str] = []
    preferred_skills: List[str] = []