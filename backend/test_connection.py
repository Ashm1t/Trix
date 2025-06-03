from llm_handler import test_connection
from rich.console import Console

console = Console()

def main():
    console.print("[bold blue]Testing Groq API Connection...[/bold blue]\n")
    
    if test_connection():
        console.print("\n[bold green]You're all set! The API key is working correctly.[/bold green]")
    else:
        console.print("\n[bold red]Please check your API key and internet connection.[/bold red]")

if __name__ == "__main__":
    main() 