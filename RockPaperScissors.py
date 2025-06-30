import random
from rich.prompt import Prompt
from rich.console import Console
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


console = Console()

choice = ["Rock", "Paper", "Scissors"]
compChoice = random.choice(choice).lower()
count = 0

user = 0
comp = 0
ties = 0

clear()

while True:

    userChoice = Prompt.ask(
        "[white on red]Choose One Of The Following [/white on red] ",
        choices=["Rock", "Paper", "Scissors", "Quit"],
        case_sensitive=False,
    ).lower()

    if userChoice == "quit":
        console.print("Thank you for playing my game!!")
        console.print(f"User: [green]{user}[/green]")
        console.print(f"Comp: [yellow]{comp}[/yellow]")
        console.print(f"Tie: [cyan]{ties}[/cyan]")
        break

    console.print(f"Computer chose: [yellow]{compChoice}[/yellow]")
    if userChoice == compChoice:
        console.print("You Tied!!", style="blue")
        ties += 1

    elif (
        userChoice == "rock"
        and compChoice == "paper"
        or userChoice == "paper"
        and compChoice == "scissors"
        or userChoice == "scissors"
        and compChoice == "rock"
    ):
        console.print("You Lost", style="red")
        comp += 1

    else:
        console.print("You Win", style="green")
        user += 1
    console.print(
        f"[bold]Score => You: [green]{user}[/green], Computer: [red]{comp}[/red], Ties: [blue]{ties}[/blue][/bold]\n"
    )
