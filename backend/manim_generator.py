from typing import Dict, Any
import re
from pathlib import Path
import uuid

# Basic animation templates
ANIMATION_TEMPLATES = {
    "circle": """
from manim import *

class CircleAnimation(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait()
""",
    "square": """
from manim import *

class SquareAnimation(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        self.wait()
""",
    "text": """
from manim import *

class TextAnimation(Scene):
    def construct(self):
        text = Text("{text}")
        self.play(Write(text))
        self.wait()
"""
}

def parse_prompt(prompt: str) -> Dict[str, Any]:
    """Parse the user prompt to determine animation type and parameters."""
    prompt = prompt.lower()
    
    # Basic parsing logic - can be expanded based on requirements
    if "circle" in prompt:
        return {"type": "circle"}
    elif "square" in prompt:
        return {"type": "square"}
    else:
        return {"type": "text", "text": prompt}

def generate_animation(prompt: str) -> str:
    """Generate Manim code from the user prompt."""
    parsed = parse_prompt(prompt)
    animation_type = parsed.get("type", "text")
    
    if animation_type == "text":
        return ANIMATION_TEMPLATES["text"].format(text=parsed.get("text", "Hello World"))
    
    return ANIMATION_TEMPLATES.get(animation_type, ANIMATION_TEMPLATES["text"])

def save_manim_code(code: str) -> str:
    """Save the generated Manim code to a file and return the file path."""
    file_name = f"scene_{uuid.uuid4().hex[:8]}.py"
    file_path = Path("backend/static") / file_name
    
    with open(file_path, "w") as f:
        f.write(code)
    
    return str(file_path)