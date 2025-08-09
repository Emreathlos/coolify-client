# Coolify Client

A simple Python Flask web application that sends health check requests to your Coolify-hosted application.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment (copy .env.example to .env and modify):
   ```bash
   cp .env.example .env
   # Edit .env with your actual Coolify app URL
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and go to http://localhost:5000

## Usage

Click the "Check Health Status" button to send a GET request to your Coolify application's `/health` endpoint and see the response displayed on the webpage.

## Local Testing/Simulation

To test the application locally without a real Coolify app:

### Method 1: Using the simulation script
1. In one terminal, start the simulation server:
   ```bash
   python local-simulation.py
   ```
   This runs a mock Coolify app on http://localhost:8000 with `/health` endpoint

2. In another terminal, start the main app:
   ```bash
   python app.py
   ```

3. Visit http://localhost:5000 and click the button to test

### Method 2: Using a simple HTTP server
```bash
# Terminal 1: Create a simple health endpoint
python -c "
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'message': 'Service is healthy'})

app.run(port=8000)
"

# Terminal 2: Run the main app
python app.py
```

### Method 3: Using Docker
1. Build the image:
   ```bash
   docker build -t coolify-client .
   ```

2. Run with environment variables:
   ```bash
   docker run -p 5000:5000 -e COOLIFY_APP_URL=https://your-app.com coolify-client
   ```

## Environment Variables

- `COOLIFY_APP_URL`: URL of your Coolify application (default: http://localhost:8000)
- `FLASK_DEBUG`: Enable/disable debug mode (default: True)
- `FLASK_HOST`: Host to bind to (default: 0.0.0.0)
- `FLASK_PORT`: Port to run on (default: 5000)
- `REQUEST_TIMEOUT`: Timeout for requests in seconds (default: 30)