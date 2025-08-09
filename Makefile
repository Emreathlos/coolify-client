.PHONY: help install terminal1 terminal2 docker-build docker-run setup clean

help:
	@echo "Available commands:"
	@echo "  install      - Install Python dependencies"
	@echo "  setup        - Copy .env.example to .env"
	@echo "  terminal1    - Start the simulation server (port 8000)"
	@echo "  terminal2    - Start the main Flask app (port 5000)"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run   - Build and run Docker container"
	@echo "  clean        - Remove Python cache files"
	@echo ""
	@echo "For local testing:"
	@echo "  1. Run 'make terminal1' in one terminal"
	@echo "  2. Run 'make terminal2' in another terminal"
	@echo "  3. Visit http://localhost:5000"

install:
	pip install -r requirements.txt

setup:
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "Created .env file from .env.example"; \
		echo "Please edit .env with your actual Coolify app URL"; \
	else \
		echo ".env file already exists"; \
	fi

terminal1:
	@echo "🚀 Starting Coolify simulation server on http://localhost:8000"
	@echo "📍 Health endpoint: http://localhost:8000/health"
	@echo "🔄 Use Ctrl+C to stop"
	python3 local-simulation.py

terminal2:
	@echo "🚀 Starting Flask client app on http://localhost:5000"
	@echo "🔄 Use Ctrl+C to stop"
	python3 app.py

docker-build:
	docker build -t coolify-client .

docker-run: docker-build
	@echo "🚀 Running Docker container on http://localhost:5000"
	@echo "🔄 Use Ctrl+C to stop"
	docker run --rm -p 5000:5000 \
		-e COOLIFY_APP_URL=${COOLIFY_APP_URL} \
		-e FLASK_DEBUG=False \
		coolify-client

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete