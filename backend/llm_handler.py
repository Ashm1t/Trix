import httpx
import os
from rich.console import Console
from personality_config import glados_personality
from pathlib import Path

console = Console()

# First check if API key is already in environment (from launcher script)
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Only try to load from .env file if API key not already set
if not GROQ_API_KEY:
    try:
        from dotenv import load_dotenv
        
        # Try to load from .env file in different possible locations
        env_paths = [
            Path('.') / '.env',
            Path('..') / '.env',
            Path(__file__).parent / '.env',
            Path(__file__).parent.parent / '.env'
        ]

        env_loaded = False
        for env_path in env_paths:
            if env_path.exists():
                try:
                    load_dotenv(env_path)
                    env_loaded = True
                    break
                except UnicodeDecodeError:
                    # Skip corrupted .env files
                    continue
        
        # Try to get API key again after loading .env
        GROQ_API_KEY = os.getenv('GROQ_API_KEY')
        
    except ImportError:
        # python-dotenv not installed, skip .env loading
        pass

# Final check for API key
if not GROQ_API_KEY:
    error_message = """
    ERROR: GROQ_API_KEY not found in environment variables.
    
    Please either:
    1. Use the launcher scripts (launch_glados.py or launch_glados.bat)
    2. Or create a .env file in the project root directory with UTF-8 encoding:
       GROQ_API_KEY=your_actual_groq_api_key_here
    3. Or set the environment variable manually:
       Windows: set GROQ_API_KEY=your_key
       PowerShell: $env:GROQ_API_KEY="your_key"
    """
    raise ValueError(error_message)

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Model configurations with correct Groq model names
MODEL_CONFIGS = {
    "llama-3.3-70b-versatile": {
        "context_window": 131072,
        "description": "Latest Llama 3.3 70B model"
    },
    "llama-3.1-8b-instant": {
        "context_window": 131072,
        "description": "Fast Llama 3.1 8B model"
    },
    "llama3-8b-8192": {
        "context_window": 8192,
        "description": "Llama 3 8B model"
    },
    "gemma2-9b-it": {
        "context_window": 8192,
        "description": "Gemma 2 9B model"
    }
}

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def test_connection():
    """Test the connection to Groq API and return available models."""
    try:
        # Simple test query
        test_messages = [{"role": "user", "content": "Hi, this is a test message."}]
        response = query_llm(test_messages, "llama3-8b-8192")
        console.print("[green]✓ Successfully connected to Groq API[/green]")
        console.print("\n[bold cyan]Available Models:[/bold cyan]")
        for model, config in MODEL_CONFIGS.items():
            console.print(f"[blue]• {model}[/blue]")
            console.print(f"  Context Window: {config['context_window']} tokens")
            console.print(f"  Description: {config['description']}\n")
        return True
    except Exception as e:
        console.print(f"[red]✗ Error connecting to Groq API: {str(e)}[/red]")
        return False

def prepare_messages(user_messages):
    """
    Prepare messages for the LLM by adding system prompt and formatting.
    
    Args:
        user_messages (list): List of message dictionaries with 'role' and 'content'
    """
    # Get the system prompt from personality configuration
    system_prompt = glados_personality.generate_system_prompt()
    
    # Start with the system message
    messages = [
        {"role": "system", "content": system_prompt}
    ]
    
    # Add user messages
    messages.extend(user_messages)
    
    return messages

def query_llm(messages, model="llama3-8b-8192"):
    """
    Query the LLM through Groq's API.
    
    Args:
        messages (list): List of message dictionaries with 'role' and 'content'
        model (str): Model to use (default: llama3-8b-8192)
    """
    # Prepare messages with personality
    formatted_messages = prepare_messages(messages)
    
    payload = {
        "model": model,
        "messages": formatted_messages,
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        response = httpx.post(GROQ_API_URL, headers=HEADERS, json=payload, timeout=30.0)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except httpx.TimeoutException:
        return glados_personality.get_error_responses()["technical_error"]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Run connection test if file is run directly
    test_connection()
