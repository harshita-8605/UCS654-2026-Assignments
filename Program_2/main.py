from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import zipfile
import os
import smtplib
from email.message import EmailMessage
from mashup import create_mashup
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Read credentials from .env
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate", response_class=HTMLResponse)
def generate(
    request: Request,
    singer: str = Form(...),
    num_videos: int = Form(...),
    duration: int = Form(...),
    email: str = Form(...)
):

    if num_videos <= 10 or duration <= 20:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": "Number of videos must be > 10 and duration > 20 seconds."
            }
        )

    try:
        # Step 1: Create mashup
        mp3_path = create_mashup(singer, num_videos, duration)

        # Step 2: Zip file
        zip_path = os.path.join("output", "mashup.zip")
        with zipfile.ZipFile(zip_path, "w") as zipf:
            zipf.write(mp3_path, arcname="mashup.mp3")

        # Step 3: Send Email
        msg = EmailMessage()
        msg["Subject"] = "Your Mashup File"
        msg["From"] = SENDER_EMAIL
        msg["To"] = email
        msg.set_content("Hi,\n\nYour mashup file is attached.\n\nEnjoy!")

        with open(zip_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="zip",
                filename="mashup.zip"
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "success": "Mashup created and sent to your email!"
            }
        )

    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": "Something went wrong while processing."
            }
        )
