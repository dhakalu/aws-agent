from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from src.aws_agent import agent

load_dotenv()


def main() -> None:
    context = []
    print("Welcome to the AWS Agent CLI! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        try:
            context.append(HumanMessage(content=user_input))
            response = agent.invoke({"messages": context})
            ai_response = response["messages"][-1] if response["messages"] else None
            context = response["messages"]
            if ai_response:
                print(f"AI:  {ai_response.content}")
            else:
                print("No response from AI.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
