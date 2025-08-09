#!/usr/bin/env python3
"""
Startup script for TwoDee Drawing Generator Backend
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    # Change to backend directory
    backend_dir = Path(__file__).parent / "backend"
    os.chdir(backend_dir)
    
    print("🚀 Starting TwoDee Drawing Generator Backend...")
    print("📁 Working directory:", backend_dir)
    print("🌐 Server will be available at: http://localhost:8000")
    print("📚 API docs will be available at: http://localhost:8000/docs")
    print("🎯 Health check: http://localhost:8000/api/health")
    print("-" * 50)
    
    try:
        # Start the FastAPI server with uvicorn
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000", 
            "--reload"
        ], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
