import os
from openai import OpenAI

def create_client() -> OpenAI:
    """
    Create and return an OpenAI client using the API key from environment variables.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")
    return OpenAI(
        api_key=api_key
    )