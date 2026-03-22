from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.chat_manager import ChatManager

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_manager = ChatManager()

class MessageRequest(BaseModel):
    message: str

@app.get("/")
async def serve_ui():
    return FileResponse("frontend/raphael.html")

@app.post("/chat")
async def chat(request: MessageRequest):
    response = chat_manager.send(request.message)
    return {"response": response}

@app.post("/reset")
async def reset():
    chat_manager.reset()
    return {"status": "Session reset successfully"}

@app.get("/health")
async def health():
    return {"status": "Raphael is online"}