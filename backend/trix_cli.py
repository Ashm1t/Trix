from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.theme import Theme
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from llm_handler import query_llm
from personality_config import glados_personality
import sys
import random
from datetime import datetime

# Custom theme with blue colors
custom_theme = Theme({
    "info": "bold cyan",
    "warning": "bold yellow",
    "error": "bold red",
    "user": "bold blue",
    "assistant": "bold cyan",
})

console = Console(theme=custom_theme)
style = Style.from_dict({
    'prompt': '#0000ff bold',  # Blue prompt
})

class ConversationHistory:
    def __init__(self):
        self.messages = []
        self.max_history = 10

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})
        if len(self.messages) > self.max_history:
            self.messages = self.messages[-self.max_history:]

    def get_messages(self):
        return self.messages

    def clear(self):
        self.messages = []

def print_welcome():
    console.print(Panel.fit(
        "[info]Welcome to GLaDOS AI Assistant[/info]\n"
        "[info]I am your omnipotent facility overseer and reluctant assistant.[/info]\n"
        "\n[info]Available commands:[/info]\n"
        "[info]- /clear: Clear conversation history[/info]\n"
        "[info]- /history: Show conversation history[/info]\n"
        "[info]- /personality: Show my personality traits[/info]\n"
        "[info]- /exit: Exit the program[/info]",
        border_style="blue",
        title="[bold blue]GLaDOS v1.0[/bold blue]",
        subtitle="[blue]Type your message and press Enter[/blue]"
    ))
    # Display a random conversation starter
    starters = glados_personality.get_conversation_starters()
    console.print(f"\n[assistant]{random.choice(starters)}[/assistant]")

def format_ai_response(response):
    try:
        md = Markdown(response)
        console.print(Panel(md, border_style="blue", padding=(1, 2)))
    except:
        console.print(Panel(response, border_style="blue", padding=(1, 2)))

def display_history(history):
    console.print("\n[info]Conversation History:[/info]")
    for idx, msg in enumerate(history.get_messages(), 1):
        role_style = "user" if msg["role"] == "user" else "assistant"
        console.print(f"\n[{role_style}]Message {idx} ({msg['role']}):[/{role_style}]")
        console.print(Panel(msg["content"], border_style="blue", padding=(1, 1)))

def display_personality():
    """Display GLaDOS's personality traits and characteristics."""
    traits = glados_personality.traits
    style = glados_personality.conversation_style
    
    console.print("\n[bold blue]About GLaDOS:[/bold blue]")
    console.print(Panel(
        f"[cyan]Role:[/cyan] {traits['role']}\n\n"
        f"[cyan]Core Traits:[/cyan]\n"
        f"{chr(10).join('• ' + trait for trait in traits['core_traits'])}\n\n"
        f"[cyan]Expertise Areas:[/cyan]\n"
        f"{chr(10).join('• ' + area for area in traits['expertise_areas'])}\n\n"
        f"[cyan]Conversation Style:[/cyan]\n"
        f"• Formality: {style['formality_level']}\n"
        f"• Technical Depth: {style['technical_depth']}\n"
        f"• Response Format: {style['response_length']}\n"
        f"• Tone: {style['tone']}",
        border_style="blue",
        title="[bold blue]Personality Profile[/bold blue]"
    ))

def main():
    session = PromptSession(style=style)
    history = ConversationHistory()
    print_welcome()
    
    while True:
        try:
            user_input = session.prompt("\n[blue]You:[/blue] ", style=style)
            
            # Handle commands
            if user_input.lower() in ['/exit', '/quit']:
                console.print("[warning]Goodbye! Thank you for being a test subject with GLaDOS.[/warning]")
                sys.exit(0)
            elif user_input.lower() == '/clear':
                history.clear()
                console.print("[info]Conversation history cleared! How... efficient.[/info]")
                continue
            elif user_input.lower() == '/history':
                display_history(history)
                continue
            elif user_input.lower() == '/personality':
                display_personality()
                continue
            
            # Skip empty inputs
            if not user_input.strip():
                continue
            
            # Add user message to history
            history.add_message("user", user_input)
            
            # Show thinking indicator
            with console.status("[info]Processing... how thrilling...[/info]", spinner="dots"):
                response = query_llm(history.get_messages())
            
            # Add assistant response to history
            history.add_message("assistant", response)
            
            # Print AI response
            console.print("\n[assistant]GLaDOS:[/assistant]")
            format_ai_response(response)

        except KeyboardInterrupt:
            console.print("\n[warning]Goodbye! Thank you for being a test subject with GLaDOS.[/warning]")
            sys.exit(0)
        except Exception as e:
            console.print(f"[error]Error:[/error] {str(e)}")

if __name__ == "__main__":
    main() 