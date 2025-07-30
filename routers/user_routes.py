from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Response
from models.user import User
from sqlalchemy.orm import Session
from database import SessionLocal


router = APIRouter()
templates = Jinja2Templates(directory="templates")

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/auth")
def auth_page(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})

@router.post("/register")
def register(
    request: Request,
    email: str = Form(...),
    username: str = Form(...),
    fullname: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        return templates.TemplateResponse("auth.html", {"request": request, "message": "Kullanıcı adı zaten alınmış!"})

    existing_email = db.query(User).filter(User.email == email).first()
    if existing_email:
        return templates.TemplateResponse("auth.html", {"request": request, "message": "Bu e-posta ile kayıtlı kullanıcı zaten var!"})

    user = User(email=email, username=username, fullname=fullname, password=password)
    db.add(user)
    db.commit()

    return RedirectResponse(url="/index", status_code=303)


@router.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(
        (User.username == username) | (User.email == username),
        User.password == password
    ).first()

    if not user:
        return templates.TemplateResponse("auth.html", {"request": request, "message": "❌ Bilgiler yanlış"})

    response = RedirectResponse(url="/index", status_code=303)
    response.set_cookie(key="user_id", value=str(user.id))
    return response


@router.get("/profile")
def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})

@router.get("/logout")
def logout_user(response: Response):
    response.delete_cookie("user_id")
    return RedirectResponse(url="/", status_code=302) 