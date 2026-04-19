# AI Agent

## What is this and why should I care?

This project is a simple AI agent designed to take a CLI prompt and return a response using Google's `gemini-2.5-flash` model.

Additionally using the `--verbose` flag, you can view additional metadata regarding the response such as:
 - User prompt
 - Prompt tokens
 - Response tokens

## How to run AI agent?

### Setup

 This agent requires 2 environment variables 
 - `GEMINI_API_KEY`
 - `GEMINI_MODEL`

 After cloning this project into your local project directory please create and add a `.env` file to the project's root directory and provide your own `GEMINI_API_KEY` and which `GEMINI_MODEL` you would like the AI agent to interact with. 

 Can't have you using my API key and blowing all my money now can we?
 
 ### Execution
 Go to the project's root folder in a terminal and run one of the following commands:

 ```bash
 uv run main.py "<INSERT_YOUR_PROMPT_HERE>"
 ```

or

 ```bash
 uv run main.py --verbose "<INSERT_YOUR_PROMPT_HERE>"
 ```

 Make sure to replace `<INSERT_YOUR_PROMPT_HERE>` with the prompt you wish to send to the AI agent.