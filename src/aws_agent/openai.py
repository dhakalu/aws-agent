import os

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# from openai import OpenAI
from langchain_openai import ChatOpenAI as OpenAI

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"


def create_client() -> OpenAI:
    """
    Create and return an OpenAI client using the API key from environment variables.
    """
    api_key = os.getenv("GITHUB_TOKEN")
    if not api_key:
        raise ValueError("GITHUB_TOKEN environment variable not set.")
    return OpenAI(api_key=api_key, base_url=endpoint, model=model, temperature=0.7, max_tokens=1000)


def get_response(messages: list[HumanMessage | AIMessage | SystemMessage]) -> str:
    """
    Get a response from the OpenAI client using the provided messages.
    """
    client = create_client()
    response = client.invoke(
        input=messages,
    )
    return response.content if isinstance(response, AIMessage) else str(response)
