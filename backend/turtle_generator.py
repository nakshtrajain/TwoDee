import turtle
import io
import base64
from PIL import Image, ImageDraw
import tkinter as tk
from typing import Dict, Any
import re
import math
import time
import threading
from queue import Queue
import os

class TurtleDrawer:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = None
        self.turtle_obj = None
        self.drawing_complete = False
        
    def setup_turtle(self):
        """Setup turtle graphics environment"""
        try:
            # Create a new turtle screen
            self.screen = turtle.Screen()
            self.screen.setup(width=self.width, height=self.height)
            self.screen.bgcolor("white")
            self.screen.title("TwoDee Drawing")
            
            # Create turtle object
            self.turtle_obj = turtle.Turtle()
            self.turtle_obj.speed(0)  # Fastest speed for batch generation
            self.turtle_obj.shape("turtle")
            
            # Disable animation for faster drawing when needed
            self.screen.tracer(0, 0)
            
        except Exception as e:
            print(f"Warning: Could not setup turtle graphics display: {e}")
            # Continue without display for headless environments
        
    def parse_and_draw(self, prompt: str):
        """Parse the prompt and execute drawing commands"""
        prompt = prompt.lower().strip()
        
        # Reset turtle position
        self.turtle_obj.penup()
        self.turtle_obj.home()
        self.turtle_obj.pendown()
        
        # Parse different drawing commands
        if "circle" in prompt:
            self._draw_circle(prompt)
        elif "square" in prompt or "rectangle" in prompt:
            self._draw_square(prompt)
        elif "triangle" in prompt:
            self._draw_triangle(prompt)
        elif "star" in prompt:
            self._draw_star(prompt)
        elif "spiral" in prompt:
            self._draw_spiral(prompt)
        elif "flower" in prompt:
            self._draw_flower(prompt)
        elif "house" in prompt:
            self._draw_house(prompt)
        elif "tree" in prompt:
            self._draw_tree(prompt)
        else:
            # Default: draw based on simple commands
            self._parse_movement_commands(prompt)
            
        # Update the screen
        self.screen.update()
        
    def _extract_number(self, text: str, default: int = 100) -> int:
        """Extract number from text, return default if not found"""
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else default
        
    def _extract_color(self, text: str) -> str:
        """Extract color from text"""
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "gray"]
        for color in colors:
            if color in text:
                return color
        return "black"
        
    def _draw_circle(self, prompt: str):
        """Draw a circle based on prompt"""
        radius = self._extract_number(prompt, 50)
        color = self._extract_color(prompt)
        
        self.turtle_obj.color(color)
        if "fill" in prompt or "filled" in prompt:
            self.turtle_obj.begin_fill()
            self.turtle_obj.circle(radius)
            self.turtle_obj.end_fill()
        else:
            self.turtle_obj.circle(radius)
            
    def _draw_square(self, prompt: str):
        """Draw a square or rectangle based on prompt"""
        size = self._extract_number(prompt, 100)
        color = self._extract_color(prompt)
        
        self.turtle_obj.color(color)
        if "fill" in prompt or "filled" in prompt:
            self.turtle_obj.begin_fill()
            
        for _ in range(4):
            self.turtle_obj.forward(size)
            self.turtle_obj.right(90)
            
        if "fill" in prompt or "filled" in prompt:
            self.turtle_obj.end_fill()
            
    def _draw_triangle(self, prompt: str):
        """Draw a triangle based on prompt"""
        size = self._extract_number(prompt, 100)
        color = self._extract_color(prompt)
        
        self.turtle_obj.color(color)
        if "fill" in prompt or "filled" in prompt:
            self.turtle_obj.begin_fill()
            
        for _ in range(3):
            self.turtle_obj.forward(size)
            self.turtle_obj.left(120)
            
        if "fill" in prompt or "filled" in prompt:
            self.turtle_obj.end_fill()
            
    def _draw_star(self, prompt: str):
        """Draw a star based on prompt"""
        size = self._extract_number(prompt, 100)
        color = self._extract_color(prompt)
        
        self.turtle_obj.color(color)
        if "fill" in prompt or "filled" in prompt:
            self.turtle_obj.begin_fill()
            
        for _ in range(5):
            self.turtle_obj.forward(size)
            self.turtle_obj.right(144)
            
        if "fill" in prompt or "filled" in prompt:
            self.turtle_obj.end_fill()
            
    def _draw_spiral(self, prompt: str):
        """Draw a spiral based on prompt"""
        color = self._extract_color(prompt)
        self.turtle_obj.color(color)
        
        for i in range(100):
            self.turtle_obj.forward(i * 2)
            self.turtle_obj.right(90)
            
    def _draw_flower(self, prompt: str):
        """Draw a flower based on prompt"""
        color = self._extract_color(prompt)
        self.turtle_obj.color(color)
        
        # Draw petals
        for _ in range(8):
            self.turtle_obj.circle(50, 60)
            self.turtle_obj.left(120)
            self.turtle_obj.circle(50, 60)
            self.turtle_obj.left(120)
            self.turtle_obj.left(45)
            
    def _draw_house(self, prompt: str):
        """Draw a simple house based on prompt"""
        color = self._extract_color(prompt)
        self.turtle_obj.color(color)
        
        # Draw base
        for _ in range(4):
            self.turtle_obj.forward(100)
            self.turtle_obj.right(90)
            
        # Draw roof
        self.turtle_obj.forward(100)
        self.turtle_obj.left(135)
        self.turtle_obj.forward(70)
        self.turtle_obj.left(90)
        self.turtle_obj.forward(70)
        self.turtle_obj.left(135)
        
        # Draw door
        self.turtle_obj.penup()
        self.turtle_obj.goto(-20, -100)
        self.turtle_obj.pendown()
        self.turtle_obj.left(90)
        self.turtle_obj.forward(60)
        self.turtle_obj.right(90)
        self.turtle_obj.forward(40)
        self.turtle_obj.right(90)
        self.turtle_obj.forward(60)
        
    def _draw_tree(self, prompt: str):
        """Draw a simple tree based on prompt"""
        color = self._extract_color(prompt)
        self.turtle_obj.color("brown")
        
        # Draw trunk
        self.turtle_obj.left(90)
        self.turtle_obj.forward(100)
        
        # Draw branches
        self.turtle_obj.color("green")
        self.turtle_obj.right(45)
        self.turtle_obj.forward(50)
        self.turtle_obj.backward(50)
        self.turtle_obj.left(90)
        self.turtle_obj.forward(50)
        self.turtle_obj.backward(50)
        self.turtle_obj.right(45)
        
        # Draw leaves (circle)
        self.turtle_obj.color(color if color != "brown" else "green")
        self.turtle_obj.circle(40)
        
    def _parse_movement_commands(self, prompt: str):
        """Parse basic movement commands"""
        words = prompt.split()
        
        for i, word in enumerate(words):
            if word in ["forward", "move", "go"]:
                distance = 50
                if i + 1 < len(words) and words[i + 1].isdigit():
                    distance = int(words[i + 1])
                self.turtle_obj.forward(distance)
                
            elif word in ["back", "backward"]:
                distance = 50
                if i + 1 < len(words) and words[i + 1].isdigit():
                    distance = int(words[i + 1])
                self.turtle_obj.backward(distance)
                
            elif word in ["left", "turn"]:
                angle = 90
                if i + 1 < len(words) and words[i + 1].isdigit():
                    angle = int(words[i + 1])
                self.turtle_obj.left(angle)
                
            elif word in ["right"]:
                angle = 90
                if i + 1 < len(words) and words[i + 1].isdigit():
                    angle = int(words[i + 1])
                self.turtle_obj.right(angle)
                
            elif word in ["up", "penup"]:
                self.turtle_obj.penup()
                
            elif word in ["down", "pendown"]:
                self.turtle_obj.pendown()
                
    def save_as_image(self, filename: str = "drawing.png"):
        """Save the turtle drawing as an image"""
        try:
            # Get the canvas
            canvas = self.screen.getcanvas()
            
            # Save as PostScript first
            ps_file = filename.replace('.png', '.eps')
            canvas.postscript(file=ps_file)
            
            # Convert PS to PNG using PIL
            img = Image.open(ps_file)
            img.save(filename, 'PNG')
            
            # Clean up PS file
            import os
            os.remove(ps_file)
            
            return filename
            
        except Exception as e:
            print(f"Error saving image: {e}")
            return None
            
    def get_image_data(self):
        """Get image data as base64 string"""
        try:
            filename = "temp_drawing.png"
            saved_file = self.save_as_image(filename)
            
            if saved_file:
                with open(saved_file, "rb") as img_file:
                    img_data = base64.b64encode(img_file.read()).decode('utf-8')
                
                # Clean up temp file
                import os
                os.remove(saved_file)
                
                return img_data
            return None
            
        except Exception as e:
            print(f"Error getting image data: {e}")
            return None
            
    def close(self):
        """Close the turtle graphics window"""
        if self.screen:
            self.screen.bye()


def generate_turtle_drawing(prompt: str) -> Dict[str, Any]:
    """Generate a turtle drawing from a prompt and return image data"""
    try:
        drawer = TurtleDrawer()
        drawer.setup_turtle()
        drawer.parse_and_draw(prompt)
        
        # Save the drawing as an image
        image_filename = f"static/drawing_{int(time.time())}.png"
        saved_file = drawer.save_as_image(image_filename)
        
        drawer.close()
        
        if saved_file:
            return {
                "status": "success",
                "image_path": saved_file,
                "message": f"Drawing created for: {prompt}"
            }
        else:
            return {
                "status": "error",
                "message": "Failed to save drawing"
            }
            
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error generating drawing: {str(e)}"
        }


# Example usage and testing
if __name__ == "__main__":
    # Test the turtle drawing
    test_prompts = [
        "draw a red circle",
        "draw a blue square",
        "draw a filled green triangle",
        "draw a star",
        "draw a house",
        "draw a tree"
    ]
    
    for prompt in test_prompts:
        print(f"Testing: {prompt}")
        result = generate_turtle_drawing(prompt)
        print(f"Result: {result}")
        print("-" * 50)
