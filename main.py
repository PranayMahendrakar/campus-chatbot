#!/usr/bin/env python3
"""Campus Chatbot - Author: Pranay M"""
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from modules import ConversationManager

console = Console()
chat_manager = ConversationManager()

def main():
    console.print(Panel("🏫 CAMPUS CHATBOT 🏫\nYour Campus Assistant", style="bold cyan"))
    console.print("[dim]Ask about resources, events, policies, directions, and more![/dim]")
    console.print("[dim]Type 'quit' to exit, 'clear' to reset conversation[/dim]\n")
    
    while True:
        message = Prompt.ask("[bold green]You[/bold green]")
        if message.lower() == 'quit': break
        if message.lower() == 'clear':
            chat_manager.clear_history()
            console.print("[yellow]Conversation cleared[/yellow]")
            continue
        
        response = chat_manager.chat(message)
        console.print(Panel(Markdown(response), title="Campus Bot", border_style="cyan"))

if __name__ == "__main__": main()
