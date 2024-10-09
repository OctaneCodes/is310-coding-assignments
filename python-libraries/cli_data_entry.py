from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import os

console = Console()
games = [
    {"Title": "Counter-Strike", "Release Date": "2000", "Publisher": "Valve"},
    {"Title": "Counter-Strike: Condition Zero", "Release Date": "2004", "Publisher": "Turtle Rock Studios"},
    {"Title": "Counter-Strike: Source", "Release Date": "2004", "Publisher": "Valve"},
    {"Title": "Counter-Strike: Global Offensive", "Release Date": "2012", "Publisher": "Valve"},
    {"Title": "Counter-Strike 2", "Release Date": "2023", "Publisher": "Valve"}
]

def get_game_data():
    while True:
        console.print("\nEnter additional game data: ")

        # Gather input for the game data
        title = Prompt.ask("Enter game title")
        release_date = Prompt.ask("Enter game release date")
        publisher = Prompt.ask("Enter game publisher")

        new_game = {"Title": title, "Release Date": release_date, "Publisher": publisher}
        is_correct = Prompt.ask("\nIs this Correct? (yes/no)", choices=["yes", "no"])

        if is_correct.lower() == "yes":
            games.append(new_game)  # Append to the games list
            console.print(f"\nAdded: {new_game}")
        else:
            console.print("[bold red]Let's try again.[/bold red]")

        # Ask if the user wants to continue adding more games
        continue_prompt = Prompt.ask("Do you want to add another game? (yes/no)", choices=["yes", "no"])
        if continue_prompt.lower() != "yes":
            break


def display_games():
    # Create a table to display the games
    table = Table(title="Video Games")
    table.add_column("Title", style="cyan", no_wrap=True)
    table.add_column("Release Date", style="magenta")
    table.add_column("Publisher", style="green", justify="right")

    for game in games:
        table.add_row(game["Title"], game["Release Date"], game["Publisher"])

    console.print("Here is a list of games I own:", style="bold cyan")
    console.print(table)


def save_games_to_file(filename):
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))  
    file_path = os.path.join(script_directory, filename)  # Create the full file path
    
    with open(filename, 'w') as file:
        for game in games:
            file.write(f"Title: {game['Title']}, Release Date: {game['Release Date']}, Publisher: {game['Publisher']}\n")
    console.print(f"\nGame list has been saved to {filename}")


# Display initial list of games
display_games()
# Get additional game data from the user
get_game_data()
# Display the updated list of games
display_games()
save_games_to_file("games_list.txt")