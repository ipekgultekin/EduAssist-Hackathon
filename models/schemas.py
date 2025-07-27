from pydantic import BaseModel

class EducationRequest(BaseModel):
    topic: str
    question: str = None
    lang: str
    mode: str
