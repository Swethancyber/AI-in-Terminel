from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from openai import OpenAI

# -----------------------------
# Direct OpenAI API Key
# -----------------------------
api_key = ""  # <-- Put your actual API key here
client = OpenAI(api_key=api_key)

# -----------------------------
# Initialize Rich console
# -----------------------------
console = Console()

# -----------------------------
# ASCII Banner
# -----------------------------
banner = """\
   █████╗ ██╗      █████╗ ███╗   ██╗
  ██╔══██╗██║     ██╔══██╗████╗  ██║
  ███████║██║     ███████║██╔██╗ ██║
  ██╔══██║██║     ██╔══██║██║╚██╗██║
  ██║  ██║███████╗██║  ██║██║ ╚████║
  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

# -----------------------------
# ChatGPT Response Function
# -----------------------------
def get_chatgpt_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful, concise terminal-based AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

        return response.choices[0].message.content.strip()
    except Exception as e:
        error_msg = str(e).lower()
        if "quota" in error_msg or "billing" in error_msg:
            return "❌ OpenAI quota exceeded or billing issue."
        if "api key" in error_msg:
            return "❌ Invalid OpenAI API key."
        return f"[Error: {e}]"

# -----------------------------
# Main CLI Loop
# -----------------------------
def main():
    console.clear()
    console.print(Text(banner, style="bold cyan"))
    console.print(
        Panel.fit(
            "🤖 Welcome to AlAN ChatGPT Terminal CLI\nType 'exit' or 'quit' to leave.",
            style="bold magenta"
        )
    )

    while True:
        user_input = Prompt.ask("\n[bold green]> You[/bold green]").strip()

        if user_input.lower() in {"exit", "quit"}:
            console.print("\n[bold red]Goodbye![/bold red]")
            break

        ai_response = get_chatgpt_response(user_input)

        console.print(
            Panel(
                ai_response,
                title="AlAN ChatGPT",
                style="bold blue"
            )
        )

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()
