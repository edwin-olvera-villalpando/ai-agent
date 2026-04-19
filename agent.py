from google import genai
from google.genai import types

def create_client(api_key: str) -> genai.Client:
    return genai.Client(api_key=api_key)


def prompt_agent(client: genai.Client, model: str, prompt: str, verbose: bool = False) -> str:
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    response = client.models.generate_content(model=model, contents=messages)

    if response.usage_metadata is None:
        raise RuntimeError("usage_metadata not found in response")
    
    if verbose:
        _add_response_metadata(prompt, response)
    
    return response.text


def _add_response_metadata(prompt: str, response) -> None:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")