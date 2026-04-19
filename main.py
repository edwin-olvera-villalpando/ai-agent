import argparse
from config import get_config
from agent import create_client, prompt_agent


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    config = get_config()
    client = create_client(config["api_key"])
    response = prompt_agent(client, config["model"], args.user_prompt, verbose=args.verbose)
    print(f"Response: {response}")

if __name__ == "__main__":
    main()