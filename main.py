import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Add src directory to Python path for development
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from aws_agent import create_client  # noqa: E402

client = create_client()


def main() -> None:
    response = client.chat.completions.create(
        model="gpt-3o", messages=[{"role": "user", "content": "Hello from aws-agent!"}]
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
