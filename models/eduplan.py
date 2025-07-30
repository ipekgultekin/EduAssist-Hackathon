from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class StudyPlan(Base):
    __tablename__ = "study_plans"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    goal = Column(String)
    plan_text = Column(String)
    created_at = Column(DateTime)
