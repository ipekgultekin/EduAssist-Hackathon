from pydantic import BaseModel

class EducationRequest(BaseModel):
    topic: str
    lang: str
    mode: str
    question: str = None
    answer: str = None
    step: int = 0
