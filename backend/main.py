from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from simple_drawer import generate_simple_drawing
import os
from pathlib import Path

app = FastAPI()

# Create static directory if it doesn't exist
static_dir = Path("static")
static_dir.mkdir(parents=True, exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DrawingPrompt(BaseModel):
    prompt: str

@app.post("/api/generate")
async def generate_drawing(prompt: DrawingPrompt):
    try:
        # Generate the drawing
        result = generate_simple_drawing(prompt.prompt)
        
        if result["status"] == "success":
            # Get the relative path for the frontend
            image_path = result["image_path"]
            relative_path = "/" + image_path
            
            return {
                "status": "success",
                "message": result["message"],
                "image_url": relative_path
            }
        else:
            return {
                "status": "error",
                "message": result["message"]
            }
            
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to generate drawing: {str(e)}"
        }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def read_root():
    return FileResponse('static/index.html') 