import openai
import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

# Initialize Rich console
console = Console()

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# ASCII Banner
banner = """\
   █████╗ ██╗      █████╗ ███╗   ██╗
  ██╔══██╗██║     ██╔══██╗████╗  ██║
  ███████║██║     ███████║██╔██╗ ██║
  ██╔══██║██║     ██╔══██║██║╚██╗██║
  ██║  ██║███████╗██║  ██║██║ ╚████║
  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

def get_openai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"[Error: {e}]"

def main():
    console.clear()
    console.print(Text(banner, style="bold cyan"))
    console.print(Panel.fit("🤖 Welcome to AlAN GPT Terminal CLI\nType 'exit' or 'quit' to leave.", style="bold magenta"))

    while True:
        user_input = Prompt.ask("\n[bold green]> You[/bold green]").strip()

        if user_input.lower() in ['exit', 'quit']:
            console.print("\n[bold red]Goodbye![/bold red]")
            break

        # Get AI response from OpenAI API
        ai_response = get_openai_response(user_input)

        # Display AI response in a styled panel
        console.print(Panel(ai_response, title="AlAN GPT", style="bold blue"))

if __name__ == "__main__":
    main()
