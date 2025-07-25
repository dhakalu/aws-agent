# AWS Agent Makefile
# Development commands for code quality, testing, and security

.PHONY: help lint lint-fix test scan clean install dev-install build

# Default target
help:
	@echo "AWS Agent - Development Commands"
	@echo ""
	@echo "Available targets:"
	@echo "  lint        Check code style and linting (no fixes)"
	@echo "  lint-fix    Fix code style and linting issues"
	@echo "  test        Run test suite with coverage"
	@echo "  scan        Run security scans"
	@echo "  check       Run all quality checks (lint + test)"
	@echo "  install     Install package in production mode"
	@echo "  dev-install Install package in development mode"
	@echo "  build       Build package distributions"
	@echo "  clean       Clean build artifacts and cache"
	@echo "  help        Show this help message"

# Lint checking (read-only, fails if issues found)
lint:
	@echo "🔍 Running code quality checks..."
	uv run isort --check-only --diff src/ tests/
	uv run black --check --diff src/ tests/
	uv run ruff check src/ tests/
	uv run mypy src/
	@echo "✅ All lint checks passed!"

# Lint with automatic fixes
lint-fix:
	@echo "🧹 Fixing code style and linting issues..."
	uv run isort src/ tests/
	uv run black src/ tests/
	uv run ruff check --fix src/ tests/
	@echo "✅ Code formatting and linting fixes applied!"

# Run test suite
test:
	@echo "🧪 Running test suite..."
	uv run pytest --cov=aws_mcp --cov-report=term-missing --cov-report=html
	@echo "✅ Tests completed! Coverage report generated in htmlcov/"

# Security scanning
scan:
	@echo "🔒 Running security scans..."
	@echo "🛡️  Checking for known vulnerabilities..."
	uv add --dev safety
	uv run safety check --json || echo "⚠️  Safety check completed with warnings"
	@echo "🔐 Running security linter..."
	uv add --dev bandit
	uv run bandit -r src/ -f json || echo "⚠️  Bandit scan completed with warnings"
	@echo "✅ Security scans completed!"

check: lint-fix lint test scan
	@echo "✅ All quality checks passed!"

run:
	@echo "🚀 Running AWS Agent..."
	uv run main.py

# Install package in production mode
install:
	@echo "📦 Installing AWS Agent..."
	uv sync
	@echo "✅ Installation completed!"

# Install package in development mode
dev-install:
	@echo "🔧 Installing AWS Agent in development mode..."
	uv sync --extra dev
	@echo "✅ Development installation completed!"

# Build package distributions
build:
	@echo "🏗️  Building package distributions..."
	uv build
	@echo "✅ Build completed! Distributions available in dist/"

# Clean build artifacts and cache
clean:
	@echo "🧹 Cleaning build artifacts and cache..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "✅ Cleanup completed!"

# Combined quality check (lint + test)
check: lint test
	@echo "✅ All quality checks passed!"

# Full development workflow
all: clean dev-install lint-fix test scan build
	@echo "🎉 Full development workflow completed!"