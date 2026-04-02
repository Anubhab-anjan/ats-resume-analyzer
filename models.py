from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: str
    company_name: str
    role: str

class Suggestion(BaseModel):
    category: str
    priority: str
    message: str

class AnalyzeResponse(BaseModel):
    ats_score: int
    keyword_match: int
    format_score: int
    experience_match: int
    missing_keywords: List[str]
    matched_keywords: List[str]
    suggestions: List[Suggestion]
    summary: str
