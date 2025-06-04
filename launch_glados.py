#!/usr/bin/env python3
"""
GLaDOS AI Assistant Launcher
This script sets up the environment and launches GLaDOS CLI.
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    # Set the API key (replace with your actual key)
    api_key = "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"
    os.environ['GROQ_API_KEY'] = api_key
    
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    backend_dir = script_dir / "backend"
    cli_script = backend_dir / "trix_cli.py"
    
    # Check if the CLI script exists
    if not cli_script.exists():
        print("ERROR: GLaDOS CLI script not found!")
        print(f"Expected location: {cli_script}")
        input("Press Enter to exit...")
        return 1
    
    # Change to the backend directory
    os.chdir(backend_dir)
    
    try:
        # Launch GLaDOS CLI
        subprocess.run([sys.executable, "trix_cli.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: GLaDOS failed to start with exit code {e.returncode}")
        input("Press Enter to exit...")
        return e.returncode
    except KeyboardInterrupt:
        print("\nGLaDOS terminated by user.")
        return 0
    except Exception as e:
        print(f"ERROR: Unexpected error occurred: {e}")
        input("Press Enter to exit...")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 