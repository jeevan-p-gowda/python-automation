setup:
	@echo "🚀 Setting up the project..." 
	@mkdir -p .env
	@curl -LsSf https://astral.sh/uv/install.sh | sh
	@uv venv
	@source .venv/bin/activate
	@uv sync
	@echo "✅ Setup complete!"