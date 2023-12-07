# Import necessary libraries
import aiohttp
import asyncio
from chat import chat, chat_history
from utils import search_ddg
from rich.console import Console
import requests
from constants import API_URL, MODELS

# Initialize a console for rich text output
console = Console()

def get_model_names():
    response = requests.get(f'{API_URL}/tags')
    if response.status_code == 200:
        models = response.json()['models']
        MODELS.update({model['name']: model['name'] for model in models})
    else:
        console.print("Failed to fetch models.", style="bold red")

# Main execution
if __name__ == "__main__":
    # Fetch the list of models and update MODELS dictionary
    get_model_names()

    # Prompt the user to choose a model
    console.print("Choose a model:", style="bold yellow")
    for i, name in enumerate(MODELS.keys(), start=1):
        console.print(f"{i}. {name}", style="bold cyan")
    model_index = int(console.input("Enter the number of the model: ")) - 1

    # Check if the entered model number is valid
    if model_index < 0 or model_index >= len(MODELS):
        console.print("Invalid number.", style="bold red")
    else:
        # If valid, start the chat with the chosen model
        model = list(MODELS.keys())[model_index]
        asyncio.run(chat(model))

        # After the chat ends, save the chat history to a text file
        with open("chat_history.txt", "w") as f:
            f.write('\n'.join(str(item) for item in chat_history))