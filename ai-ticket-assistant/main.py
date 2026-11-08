"""FastAPI LLM ticket processing build"""

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Ticket Assistant działa"}

tickets = [
    {
        "id": 1,
        "title": "Nie działa VPN",
        "description": "Przy połączeniu wyskakuje timeout",
        "status": "nowe"
    }
]


@app.get("/tickets")
def get_tickets():
    return tickets