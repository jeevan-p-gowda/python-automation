.ONESHELL:
SHELL := /bin/bash

setup:
	@echo "🚀 Setting up the project..."
	@if [ -n "$$JENKINS_HOME" ]; then \
		echo "Running in Jenkins - cleaning up existing directories..."; \
		rm -rf .env .auth; \
	fi
	@mkdir -p .env
	@mkdir -p .auth
	@curl -LsSf https://astral.sh/uv/install.sh | sh
	@uv venv
	@source .venv/bin/activate
	@uv sync
	@playwright install chromium
	@echo "✅ Setup complete!"