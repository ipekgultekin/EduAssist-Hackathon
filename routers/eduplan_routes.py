from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.eduplan import StudyPlan
from database import SessionLocal
from utils.generate_plan import generate_weekly_plan
import datetime
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/eduplan/generate")
async def generate_plan(
    request: Request,
    goal: str = Form(...),
    db: Session = Depends(get_db)
):
    # 1. Kullanıcıdan hedef alınır
    user_id = request.cookies.get("user_id")
    if not user_id:
        return JSONResponse({"error": "Giriş yapmanız gerekli."}, status_code=401)

    # 2. AI plan üretir
    plan = generate_weekly_plan(goal)

    # 3. Veritabanına kaydedilir
    study_plan = StudyPlan(
        user_id=user_id,
        goal=goal,
        plan_text=plan,
        created_at=datetime.datetime.now()
    )
    db.add(study_plan)
    db.commit()

    return JSONResponse({"plan": plan})


@router.get("/eduplan/history")
async def get_plan_history(request: Request, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    if not user_id:
        return JSONResponse({"error": "Giriş yapmanız gerekli."}, status_code=401)

    plans = db.query(StudyPlan).filter(StudyPlan.user_id == user_id).order_by(StudyPlan.created_at.desc()).all()
    history = [{"goal": p.goal, "plan": p.plan_text, "created_at": p.created_at.strftime("%d.%m.%Y")} for p in plans]
    return JSONResponse({"history": history})

templates = Jinja2Templates(directory="templates")

@router.get("/eduplan", response_class=HTMLResponse)
async def eduplan_page(request: Request):
    return templates.TemplateResponse("eduplan.html", {"request": request})