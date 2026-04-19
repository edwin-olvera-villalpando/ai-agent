# AI Agent

## What is this and why should I care?

This project is a simple AI agent designed to take a CLI prompt and return a response using Google's `gemini-2.5-flash` model.

Additionally using the `--verbose` flag, you can view additional metadata regarding the response such as:
 - User prompt
 - Prompt tokens
 - Response tokens

 ## How to run AI agent?

 Clone this project into your local project directory and run the following command:

 ```bash
 uv run main.py "<INSERT_YOUR_PROMPT_HERE>"
 ```

or

 ```bash
 uv run main.py --verbose "<INSERT_YOUR_PROMPT_HERE>"
 ```

 Make sure to replace `<INSERT_YOUR_PROMPT_HERE>` with the prompt you wish to send to the AI agent.