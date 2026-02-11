from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.shemas import PromptRequest, PromptResponse
from app.llm import call_llm
from app.logger import logger

app = FastAPI(title="Local LLM API")

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# @app.get("/", response_class=HTMLResponse)
# def test_root():
#     return "<h1>Backend is working</h1>"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/", response_class=HTMLResponse)
def chat_ui(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})


@app.post("/generate", response_model=PromptResponse)
def generate_text(request: PromptRequest):
    logger.info(f"Received prompt: {request.prompt}")
    response = call_llm(request.prompt)
    return {"response": response}
