import os
from dotenv import load_dotenv

load_dotenv()

def get_config() -> dict:
    api_key = os.environ.get("GEMINI_API_KEY")
    model = os.environ.get('GEMINI_MODEL')

    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY is not set")
    
    if model is None:
        raise RuntimeError("GEMINI_MODEL is not set")
    
    return {"api_key": api_key, "model": model}