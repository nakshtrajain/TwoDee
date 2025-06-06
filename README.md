# TwoDee Animation Generator

A web application that generates 2D animations from text prompts using Manim.

## Features

- Text-to-animation generation using Manim
- Real-time video rendering
- Modern React frontend with Tailwind CSS
- FastAPI backend for efficient processing

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- Manim Community Edition
- FFmpeg (required for Manim)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd TwoDee
```

2. Set up the backend:
```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

3. Set up the frontend:
```bash
cd frontend
npm install
```

## Running the Application

1. Start the backend server:
```bash
# From the root directory
cd backend
uvicorn main:app --reload
```

2. Start the frontend development server:
```bash
# From the root directory
cd frontend
npm start
```

3. Open your browser and navigate to `http://localhost:3000`

## Usage

1. Enter a text prompt describing the animation you want to create
2. Click "Generate Animation"
3. Wait for the animation to be generated
4. The video will automatically play when ready

## Example Prompts

- "Create a circle that transforms into a square"
- "Show a bouncing square"
- "Display text that fades in"

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. #   T w o D e e 
 
 