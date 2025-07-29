from fastapi import FastAPI, Request, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from routers import ai_routes
import os
import requests
import base64
from dotenv import load_dotenv
from models.user import User
from database import Base, engine
from routers import user_routes

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(ai_routes.router)
app.include_router(user_routes.router)


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/index", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/konu", response_class=HTMLResponse)
async def konu_page(request: Request):
    return templates.TemplateResponse("konu.html", {"request": request})

@app.get("/soru", response_class=HTMLResponse)
async def soru_page(request: Request):
    return templates.TemplateResponse("soru.html", {"request": request})

@app.get("/eksik", response_class=HTMLResponse)
async def eksik_page(request: Request):
    return templates.TemplateResponse("eksik.html", {"request": request})

Base.metadata.create_all(bind=engine)


