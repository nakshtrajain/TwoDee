from PIL import Image, ImageDraw
import math
import time
import re
from typing import Dict, Any, Tuple

class SimpleDrawer:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (width, height), 'white')
        self.draw = ImageDraw.Draw(self.image)
        
        # Turtle state
        self.x = width // 2
        self.y = height // 2
        self.angle = 0  # 0 degrees is pointing right
        self.pen_down = True
        self.pen_color = 'black'
        
    def forward(self, distance):
        """Move forward by distance pixels"""
        old_x, old_y = self.x, self.y
        
        # Calculate new position
        self.x += distance * math.cos(math.radians(self.angle))
        self.y += distance * math.sin(math.radians(self.angle))
        
        # Draw line if pen is down
        if self.pen_down:
            self.draw.line([(old_x, old_y), (self.x, self.y)], fill=self.pen_color, width=2)
    
    def backward(self, distance):
        """Move backward by distance pixels"""
        self.forward(-distance)
    
    def left(self, angle):
        """Turn left by angle degrees"""
        self.angle -= angle
    
    def right(self, angle):
        """Turn right by angle degrees"""
        self.angle += angle
    
    def penup(self):
        """Lift the pen up"""
        self.pen_down = False
    
    def pendown(self):
        """Put the pen down"""
        self.pen_down = True
    
    def set_color(self, color):
        """Set pen color"""
        self.pen_color = color
    
    def goto(self, x, y):
        """Go to specific coordinates"""
        old_x, old_y = self.x, self.y
        self.x = x
        self.y = y
        
        if self.pen_down:
            self.draw.line([(old_x, old_y), (self.x, self.y)], fill=self.pen_color, width=2)
    
    def circle(self, radius, filled=False):
        """Draw a circle"""
        left = self.x - radius
        top = self.y - radius
        right = self.x + radius
        bottom = self.y + radius
        
        if filled:
            self.draw.ellipse([left, top, right, bottom], fill=self.pen_color)
        else:
            self.draw.ellipse([left, top, right, bottom], outline=self.pen_color, width=2)
    
    def rectangle(self, width, height, filled=False):
        """Draw a rectangle"""
        left = self.x
        top = self.y
        right = self.x + width
        bottom = self.y + height
        
        if filled:
            self.draw.rectangle([left, top, right, bottom], fill=self.pen_color)
        else:
            self.draw.rectangle([left, top, right, bottom], outline=self.pen_color, width=2)
    
    def save_image(self, filename):
        """Save the image to file"""
        self.image.save(filename, 'PNG')
        return filename

def parse_prompt(prompt: str) -> Dict[str, Any]:
    """Parse the user prompt to determine drawing type and parameters."""
    prompt = prompt.lower()
    
    # Extract color
    colors = {
        "red": "#FF0000", "blue": "#0000FF", "green": "#00FF00", 
        "yellow": "#FFFF00", "purple": "#800080", "orange": "#FFA500",
        "pink": "#FFC0CB", "brown": "#A52A2A", "black": "#000000", 
        "gray": "#808080", "grey": "#808080"
    }
    
    color = "#000000"  # default black
    for color_name, color_value in colors.items():
        if color_name in prompt:
            color = color_value
            break
    
    # Extract size
    size = 100  # default size
    numbers = re.findall(r'\d+', prompt)
    if numbers:
        size = int(numbers[0])
    
    # Determine shape/action
    if "circle" in prompt:
        return {"type": "circle", "color": color, "size": size, "filled": "fill" in prompt}
    elif "square" in prompt or "rectangle" in prompt:
        return {"type": "square", "color": color, "size": size, "filled": "fill" in prompt}
    elif "triangle" in prompt:
        return {"type": "triangle", "color": color, "size": size, "filled": "fill" in prompt}
    elif "star" in prompt:
        return {"type": "star", "color": color, "size": size, "filled": "fill" in prompt}
    elif "house" in prompt:
        return {"type": "house", "color": color, "size": size}
    elif "tree" in prompt:
        return {"type": "tree", "color": color, "size": size}
    elif "flower" in prompt:
        return {"type": "flower", "color": color, "size": size}
    elif "spiral" in prompt:
        return {"type": "spiral", "color": color, "size": size}
    else:
        return {"type": "custom", "color": color, "size": size, "prompt": prompt}

def draw_shape(drawer: SimpleDrawer, shape_info: Dict[str, Any]):
    """Draw the specified shape"""
    drawer.set_color(shape_info["color"])
    shape_type = shape_info["type"]
    size = shape_info["size"]
    
    if shape_type == "circle":
        drawer.circle(size//2, shape_info.get("filled", False))
    
    elif shape_type == "square":
        # Draw square
        if shape_info.get("filled", False):
            drawer.rectangle(size, size, filled=True)
        else:
            for _ in range(4):
                drawer.forward(size)
                drawer.right(90)
    
    elif shape_type == "triangle":
        # Draw triangle
        if shape_info.get("filled", False):
            # For filled triangle, we'll draw the outline
            points = []
            for _ in range(3):
                points.append((drawer.x, drawer.y))
                drawer.forward(size)
                drawer.left(120)
            # Use PIL to draw filled polygon
            drawer.draw.polygon(points, fill=drawer.pen_color)
        else:
            for _ in range(3):
                drawer.forward(size)
                drawer.left(120)
    
    elif shape_type == "star":
        # Draw 5-pointed star
        if shape_info.get("filled", False):
            points = []
            for _ in range(5):
                points.append((drawer.x, drawer.y))
                drawer.forward(size)
                drawer.right(144)
            drawer.draw.polygon(points, fill=drawer.pen_color)
        else:
            for _ in range(5):
                drawer.forward(size)
                drawer.right(144)
    
    elif shape_type == "house":
        draw_house(drawer, size)
    
    elif shape_type == "tree":
        draw_tree(drawer, size)
    
    elif shape_type == "flower":
        draw_flower(drawer, size)
    
    elif shape_type == "spiral":
        draw_spiral(drawer, size)
    
    else:  # custom
        draw_custom(drawer, shape_info["prompt"])

def draw_house(drawer: SimpleDrawer, size):
    """Draw a simple house"""
    # Draw base square
    for _ in range(4):
        drawer.forward(size)
        drawer.right(90)
    
    # Move to roof position
    drawer.penup()
    drawer.forward(size)
    drawer.pendown()
    
    # Draw roof triangle
    drawer.left(135)
    drawer.forward(size * 0.7)
    drawer.left(90)
    drawer.forward(size * 0.7)
    drawer.left(135)
    
    # Draw door
    drawer.penup()
    drawer.goto(drawer.x - size * 0.7, drawer.y - size)
    drawer.pendown()
    drawer.left(90)
    drawer.forward(size * 0.6)
    drawer.right(90)
    drawer.forward(size * 0.4)
    drawer.right(90)
    drawer.forward(size * 0.6)

def draw_tree(drawer: SimpleDrawer, size):
    """Draw a simple tree"""
    # Draw trunk
    drawer.set_color("#8B4513")  # Brown
    drawer.left(90)
    drawer.forward(size)
    
    # Draw leaves (circle)
    drawer.set_color("#228B22")  # Green
    drawer.circle(size * 0.4, filled=True)

def draw_flower(drawer: SimpleDrawer, size):
    """Draw a simple flower"""
    # Draw petals
    for _ in range(8):
        drawer.circle(size * 0.3)
        drawer.right(45)
    
    # Draw center
    drawer.circle(size * 0.1, filled=True)

def draw_spiral(drawer: SimpleDrawer, size):
    """Draw a spiral"""
    for i in range(100):
        drawer.forward(i * 2)
        drawer.right(90)

def draw_custom(drawer: SimpleDrawer, prompt):
    """Draw based on custom movement commands"""
    words = prompt.split()
    
    for i, word in enumerate(words):
        if word in ["forward", "move", "go"]:
            distance = 50
            if i + 1 < len(words) and words[i + 1].isdigit():
                distance = int(words[i + 1])
            drawer.forward(distance)
        
        elif word in ["back", "backward"]:
            distance = 50
            if i + 1 < len(words) and words[i + 1].isdigit():
                distance = int(words[i + 1])
            drawer.backward(distance)
        
        elif word in ["left", "turn"]:
            angle = 90
            if i + 1 < len(words) and words[i + 1].isdigit():
                angle = int(words[i + 1])
            drawer.left(angle)
        
        elif word in ["right"]:
            angle = 90
            if i + 1 < len(words) and words[i + 1].isdigit():
                angle = int(words[i + 1])
            drawer.right(angle)
        
        elif word in ["up", "penup"]:
            drawer.penup()
        
        elif word in ["down", "pendown"]:
            drawer.pendown()

def generate_simple_drawing(prompt: str) -> Dict[str, Any]:
    """Generate a drawing from a prompt using simple PIL drawing"""
    try:
        # Parse the prompt
        shape_info = parse_prompt(prompt)
        
        # Create drawer
        drawer = SimpleDrawer()
        
        # Draw the shape
        draw_shape(drawer, shape_info)
        
        # Save the image
        timestamp = int(time.time())
        filename = f"static/drawing_{timestamp}.png"
        drawer.save_image(filename)
        
        return {
            "status": "success",
            "image_path": filename,
            "message": f"Drawing created for: {prompt}"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error generating drawing: {str(e)}"
        }

# Test the drawing system
if __name__ == "__main__":
    test_prompts = [
        "draw a red circle",
        "draw a blue square",
        "draw a filled green triangle",
        "draw a star",
        "draw a house"
    ]
    
    for prompt in test_prompts:
        print(f"Testing: {prompt}")
        result = generate_simple_drawing(prompt)
        print(f"Result: {result}")
        print("-" * 50)
