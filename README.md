# AWS Agent - Educational AI Agent Framework

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.26+-green.svg)](https://python.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.5.2+-orange.svg)](https://langchain-ai.github.io/langgraph/)

## 🎓 Overview

This is an **educational repository** designed to help developers learn and understand AI agent development using modern frameworks. The project demonstrates how to build a conversational AI agent using LangChain, LangGraph, and the GitHub Models API, providing hands-on experience with:

- **AI Agent Architecture**: Understanding state management and conversation flow
- **LangGraph Integration**: Building stateful, graph-based AI applications
- **Modern Python Development**: Best practices with type hints, testing, and code quality tools
- **API Integration**: Working with language models through standardized interfaces

> **Note**: This project is primarily for learning purposes and demonstrates core concepts of AI agent development. It's an excellent starting point for understanding how modern AI agents work under the hood.

## 🏗️ Architecture

The project implements a simple but extensible AI agent architecture:

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐
│   User Input    │───▶│  LangGraph   │───▶│   OpenAI API    │
│   (CLI/Text)    │    │   Agent      │    │  (via GitHub)   │
└─────────────────┘    └──────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────┐
                       │ State Mgmt   │
                       │ (Messages)   │
                       └──────────────┘
```

### Key Components

- **`agent.py`**: Core agent logic using LangGraph's StateGraph
- **`openai.py`**: Integration with GitHub Models API (OpenAI-compatible)
- **`main.py`**: CLI interface for interactive conversations
- **State Management**: Maintains conversation history and context

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended) or pip
- GitHub Token for accessing GitHub Models API

### 1. Clone and Setup

```bash
git clone https://github.com/dhakalu/aws-agent.git
cd aws-agent
```

### 2. Install Dependencies

Using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -e .
```

For development:
```bash
uv sync --extra dev
# or
pip install -e ".[dev]"
```

### 3. Environment Configuration

Create a `.env` file in the project root:

```env
# GitHub Models API Configuration
GITHUB_TOKEN=your_github_token_here
```

**Getting a GitHub Token:**
1. Go to [GitHub Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Generate a new token with appropriate permissions
3. Copy the token to your `.env` file

### 4. Run the Agent

```bash
python main.py
```

You'll see an interactive CLI where you can chat with the agent:

```
Welcome to the AWS Agent CLI! Type 'exit' to quit.
You: Hello, how are you?
AI: Hello! I'm doing well, thank you for asking...
You: exit
```

## 📁 Project Structure

```
aws-agent/
├── src/aws_agent/           # Main package
│   ├── __init__.py         # Package initialization
│   ├── agent.py            # LangGraph agent implementation
│   └── openai.py           # GitHub Models API integration
├── tests/                  # Test suite (expandable)
├── main.py                 # CLI entry point
├── pyproject.toml         # Project configuration & dependencies
├── Makefile               # Development commands
├── uv.lock               # Locked dependencies
├── .gitignore            # Git ignore patterns
└── README.md             # This file
```

## 🛠️ Development

This project includes comprehensive development tooling to demonstrate best practices:

### Code Quality Tools

```bash
# Check code style and linting
make lint

# Auto-fix code style issues
make lint-fix

# Run tests with coverage
make test

# Run security scans
make scan

# Run all quality checks
make check
```

### Development Dependencies

- **Testing**: pytest, pytest-asyncio, pytest-cov
- **Code Formatting**: black, isort
- **Linting**: ruff, mypy
- **Type Checking**: Built-in mypy configuration

### Adding New Features

1. **Fork and Branch**: Create a feature branch for your changes
2. **Code**: Implement your feature following the existing patterns
3. **Test**: Add tests for new functionality
4. **Quality**: Run `make check` to ensure code quality
5. **Submit**: Create a pull request with your changes

## 🧠 Learning Objectives

Working with this project will help you understand:

### AI Agent Concepts
- **State Management**: How agents maintain context across conversations
- **Graph-based Execution**: Using LangGraph for complex agent workflows
- **Message Handling**: Managing different types of messages (Human, AI, System)

### LangChain Ecosystem
- **LangChain Core**: Working with messages and language model abstractions
- **LangGraph**: Building stateful, multi-step AI applications
- **Model Integration**: Connecting to various language model providers

### Software Engineering
- **Python Best Practices**: Type hints, project structure, dependency management
- **Testing**: Writing and running tests for AI applications
- **Code Quality**: Linting, formatting, and security scanning
- **Documentation**: Creating clear, maintainable code documentation

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GITHUB_TOKEN` | GitHub personal access token for API access | Yes | None |

### Model Configuration

The agent uses GitHub Models API with these settings (configurable in `openai.py`):

- **Endpoint**: `https://models.github.ai/inference`
- **Model**: `openai/gpt-4.1`
- **Temperature**: `0.7`
- **Max Tokens**: `1000`

## 📚 Learning Resources

### Documentation
- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [GitHub Models API](https://github.com/marketplace/models)

### Tutorials and Guides
- [LangChain Expression Language (LCEL)](https://python.langchain.com/docs/concepts/lcel/)
- [Building Stateful Applications with LangGraph](https://langchain-ai.github.io/langgraph/tutorials/)
- [AI Agent Design Patterns](https://python.langchain.com/docs/tutorials/agents/)

## 🤝 Contributing

This educational project welcomes contributions! Here's how you can help:

### Types of Contributions
- **Educational Content**: Improve documentation and learning materials
- **Code Examples**: Add more agent patterns and examples
- **Bug Fixes**: Fix issues and improve reliability
- **Features**: Add new agent capabilities or integrations

### Development Process
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes following the coding standards
4. Run quality checks (`make check`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📋 Roadmap

Future educational enhancements planned:

- [ ] **Multi-Agent Systems**: Demonstrate agent-to-agent communication
- [ ] **Tool Integration**: Add external tool calling capabilities
- [ ] **Memory Systems**: Implement persistent conversation memory
- [ ] **Web Interface**: Create a simple web UI for the agent
- [ ] **AWS Integration**: Add actual AWS service integrations
- [ ] **Advanced Patterns**: Implement more complex agent architectures
- [ ] **Deployment**: Add containerization and deployment examples

## 🐛 Troubleshooting

### Common Issues

**1. GitHub Token Error**
```
ValueError: GITHUB_TOKEN environment variable not set.
```
- **Solution**: Ensure your `.env` file contains a valid GitHub token

**2. Import Errors**
```
ModuleNotFoundError: No module named 'src.aws_agent'
```
- **Solution**: Install the package in development mode with `pip install -e .`

**3. API Rate Limits**
- **Solution**: GitHub Models has rate limits; wait a moment between requests

### Getting Help

- **Issues**: [Open an issue](https://github.com/dhakalu/aws-agent/issues) for bugs or questions
- **Discussions**: Use GitHub Discussions for general questions
- **Documentation**: Check the inline code documentation for implementation details

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for the excellent AI framework
- [GitHub Models](https://github.com/marketplace/models) for providing accessible AI model APIs
- The AI/ML community for continuous innovation and knowledge sharing

---

**Happy Learning! 🎉**

This project is designed to be your stepping stone into the world of AI agent development. Experiment, break things, fix them, and most importantly - have fun learning!
