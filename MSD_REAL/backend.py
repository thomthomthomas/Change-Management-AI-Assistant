from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json
from inference import generate_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class FeedbackRequest(BaseModel):
    message: str
    feedback: str

@app.get("/")
async def root():
    return {"message": "Welcome to the Change Management AI Assistant"}

@app.post("/api/chat")
async def chat(request: ChatRequest):
    try:
        response = generate_response(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/feedback")
async def feedback(request: FeedbackRequest):
    feedback_data = {
        "timestamp": datetime.now().isoformat(),
        "message": request.message,
        "feedback": request.feedback,
        "processed": False
    }
    with open("feedback.log", "a") as f:
        f.write(json.dumps(feedback_data) + "\n")
    return {"status": "Feedback stored for knowledge base updates"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)