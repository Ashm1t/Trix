import httpx
import os
from rich.console import Console
from personality_config import glados_personality

# Direct API key - replace with your actual key
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

console = Console()

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
