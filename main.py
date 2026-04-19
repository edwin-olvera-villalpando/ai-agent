import argparse

from google import genai
from google.genai import types
from config import get_config

config = get_config()
client = genai.Client(api_key=config["api_key"])

def main():

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(model=model, contents=messages)

    if response.usage_metadata is None:
        raise RuntimeError("usage_metadata not found in response")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print(f"Response: {response.text}")

if __name__ == "__main__":
    main()
