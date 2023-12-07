import requests
from constants import KNOWN_COMMANDS, API_URL

def search_ddg(query):
    response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
    return response.json()["AbstractText"]

def get_model_names():
    response = requests.get(f'{API_URL}/tags')
    if response.status_code == 200:
        models = response.json()['models']
        model_dict = {model['name']: model['name'] for model in models if model['name']}
        return model_dict
    else:
        console.print("Failed to fetch models.", style="bold red")
        return {}

def run_code(code):
    try:
        exec(code)
        return "Run successfully"
    except Exception as e:
        return str(e)