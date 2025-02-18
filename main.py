from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Mount static files for serving CSS, JS, images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 template rendering
templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Run the FastAPI app with: uvicorn main:app --reload
