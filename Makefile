setup:
	@echo "🚀 Setting up the project..." 
	@mkdir -p .env
	@mkdir -p .auth
	@curl -LsSf https://astral.sh/uv/install.sh | sh
	@uv venv
	@source .venv/bin/activate
	@uv sync
	@playwright install chromium
	@echo "✅ Setup complete!"