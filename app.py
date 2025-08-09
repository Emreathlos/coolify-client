from flask import Flask, render_template, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

COOLIFY_APP_URL = os.getenv('COOLIFY_APP_URL', 'http://localhost:8000')
REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '30'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-request', methods=['POST'])
def send_request():
    try:
        health_url = f"{COOLIFY_APP_URL.rstrip('/')}/health"
        response = requests.get(health_url, timeout=REQUEST_TIMEOUT)
        return jsonify({
            'success': True,
            'status_code': response.status_code,
            'response': response.text,
            'url': health_url
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', '5005'))
    app.run(debug=debug, host=host, port=port)