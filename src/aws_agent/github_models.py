import os

from openai import OpenAI

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"


def create_client() -> OpenAI:
    """
    Create and return an OpenAI client using the API key from environment variables.
    """
    api_key = os.getenv("GITHUB_TOKEN")
    if not api_key:
        raise ValueError("GITHUB_TOKEN environment variable not set.")
    return OpenAI(api_key=api_key, base_url=endpoint)


def get_response(prompt: str) -> str:
    """
    Get a response from the OpenAI client using the provided prompt.
    """
    client = create_client()
    response = client.chat.completions.create(
        model=model, messages=[{"role": "user", "content": prompt}], max_tokens=150
    )
    return response.choices[0].message.content.strip()
