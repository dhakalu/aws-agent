from dotenv import load_dotenv

from src.aws_agent.github_models import get_response

load_dotenv()


def main() -> None:
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        try:
            response = get_response(user_input)
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
