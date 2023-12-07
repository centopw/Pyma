# Pyma
Allow user to have a conversation with different AI models, build on OLlama

## Features
- Choose from different AI models like GPT-3, Claude, etc.
- Have a natural conversation with the selected AI assistant
- Useful commands like search, run code, etc.
- Saves chat history to file

## Usage

1. Clone the repository

```bash
    git clone https://github.com/centopw/Pyma.git
```

2. Install the requirements

```bash
    pip install -r requirements.txt
```

3. Run the main.py file

```bash
    python /app/main.py
```

### Commands

- `/exit` - Exit the program
- `/search` - Searches DuckDuckGo and returns top result
-  ~ More are coming soon!

### Configuration

The main configuration is in `constants.py`.

Set `API_URL` to the endpoint for model APIs.
Customize other constants if needed.

### Code Structure

- `main.py` - Main file to run
- `constants.py` - Constants used in the program
- `chat.py` - Chat class to handle chat logic
- `utils.py` - Utility functions

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.