import aiohttp
from rich.console import Console
from constants import API_URL, MODELS
from utils import search_ddg
from constants import KNOWN_COMMANDS, SYSTEM_PROMPTS

# Initialize a console for rich text output
console = Console()

# Initialize a list to keep track of the chat history
chat_history = []

# Function to generate a response from the AI model
async def generate(session, model, prompt):
    # Prepare the data to be sent to the API
    data = {
        "model": model,
        "prompt": prompt,
        "system": SYSTEM_PROMPTS,
        "temperature": 0.3,
        "stream": False,
    }

    # Make a POST request to the API
    async with session.post(f"{API_URL}/generate", json=data) as resp:
        # If the response status is not 200, print an error message
        if resp.status != 200:
            console.print(f"Error: {resp.status}", style="bold red")
            return None

        # Parse the response data
        json_data = await resp.json()
        response = json_data["response"]

        # Print the AI's response
        console.print(f"\n[bold green]Centix:[/bold green] {response}\n")

        return response

# Function to handle the chat interaction
async def chat(model):
    # If the model name is not valid, print an error message
    if model not in MODELS:
        console.print("Invalid model name.", style="bold red")
        return

    # Create a new HTTP session
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                # Get the user's input
                prompt = console.input("[bold red]You: [/bold red]")
                # If the input starts with "/", it's a command
                if prompt.startswith("/"):
                    # If the command is "/exit", break the loop
                    if prompt == "/exit":
                        break
                    # If the command starts with "/search ", perform a search
                    elif prompt.startswith("/search "):
                        query = prompt[8:]
                        result = search_ddg(query)
                        console.print(f"\n[bold green]Search result:[/bold green] {result}\n")
                        continue
                # Add the interaction to the chat history
                chat_history.append({"model": model, "prompt": prompt})
                # Generate a response from the AI
                response = await generate(session, MODELS[model], prompt)
            # If the user interrupts the program, break the loop
            except KeyboardInterrupt:
                break

    # Print a goodbye message
    console.print("Goodbye!", style="bold blue")