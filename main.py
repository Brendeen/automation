import os
import shutil
import re
from rich.console import Console
from rich.prompt import Prompt
from folder_creator import new_folder, user_mover, sort_folders


def main():
    console = Console()
    console.print("""
    
            [blue]Hi! What can I help you with?[/blue]
            
            Please type one of the following...
            
            [green]- new folder - to create a new folder[/green]
            
            [yellow]- move user - to remove a user from app[/yellow]
            
            [blue]- sort - to sort your folders by file path
            
            [red]- N - to quit
""")

    selection = Prompt.ask("[blue]--[/blue]")

    while selection:
        if selection == "new folder":
            name = Prompt.ask("Please write a folder name -- ")
            new_folder(name)
            console.print(f"""
            [blue]File {name} created![/blue]
        """)
            selection = Prompt.ask("[blue]Anything else I can help with?")

        elif selection == "move user":
            name = Prompt.ask("Please specify which user -- ")
            user_mover(name)
            console.print("""
            [blue]User deleted, files backed up to temporary folder.[/blue]
""")
            selection = Prompt.ask("[blue]Anything else I can help with?")
        elif selection == "sort":
            name = Prompt.ask("Please write the folder to be sorted -- ")
            sort_folders(name)
            console.print("""
            [blue]File sorted![/blue]
        """)
            selection = Prompt.ask("[blue]Anything else I can help with?")

        elif selection == "N":
            console.print("Ok, bye!")
            break
        else:
            console.print("I'm sorry, I didnt get that...")
            selection = Prompt.ask("[blue]--[/blue]")


if __name__ == "__main__":
    main()
