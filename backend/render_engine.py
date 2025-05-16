import os
import subprocess
from pathlib import Path
import uuid
from .manim_generator import save_manim_code

def render_video(manim_code: str) -> str:
    """
    Render a video from Manim code and return the path to the rendered video.
    """
    try:
        # Save the Manim code to a temporary file
        scene_file = save_manim_code(manim_code)
        
        # Get the scene class name from the code
        scene_class = None
        for line in manim_code.split('\n'):
            if line.startswith('class ') and '(Scene)' in line:
                scene_class = line.split('class ')[1].split('(')[0].strip()
                break
        
        if not scene_class:
            raise ValueError("No scene class found in the Manim code")
        
        # Create output directory if it doesn't exist
        output_dir = Path("backend/static")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate a unique name for the output file
        output_name = f"video_{uuid.uuid4().hex[:8]}"
        
        # Run Manim command to render the video
        command = [
            "manim",
            "-qm",  # Medium quality
            scene_file,
            scene_class,
            "--media_dir", str(output_dir),
            "-o", output_name
        ]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise RuntimeError(f"Manim rendering failed: {result.stderr}")
        
        # Find the rendered video file
        video_file = list(output_dir.glob(f"{output_name}.mp4"))[0]
        
        # Clean up the temporary scene file
        Path(scene_file).unlink()
        
        return str(video_file)
        
    except Exception as e:
        raise RuntimeError(f"Failed to render video: {str(e)}")

def cleanup_old_videos(max_age_hours: int = 24):
    """Clean up videos older than the specified age."""
    # Implementation for cleanup logic (optional)
    pass 