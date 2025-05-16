from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnimationPrompt(BaseModel):
    prompt: str

@app.post("/api/generate")
async def generate_video(prompt: AnimationPrompt):
    # Temporary response for testing
    return {
        "status": "success",
        "message": f"Received prompt: {prompt.prompt}",
        "video_url": "/static/sample.mp4"  # This is just a placeholder
    }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"} 