import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
model = os.environ.get('GEMINI_MODEL')

if api_key is None:
    raise RuntimeError("api_key is None. Please provide api_key")

client = genai.Client(api_key=api_key)

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
