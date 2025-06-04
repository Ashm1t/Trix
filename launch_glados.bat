@echo off
title GLaDOS AI Assistant
cd /d "%~dp0"

:: Set your Groq API key here (replace with your actual key)
set GROQ_API_KEY=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

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not found in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

:: Change to backend directory and run GLaDOS
cd backend
python trix_cli.py

:: Keep the window open if there's an error
if errorlevel 1 (
    echo.
    echo An error occurred. Press any key to exit...
    pause >nul
) 