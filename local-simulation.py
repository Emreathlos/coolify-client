#!/usr/bin/env python3
"""
Simple local server to simulate your Coolify app's /health endpoint
Run this in a separate terminal to test your Flask client locally
"""

from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "service": "coolify-simulation",
        "uptime": "5 minutes"
    })

@app.route('/health/detailed')
def detailed_health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "checks": {
            "database": "ok",
            "redis": "ok", 
            "external_api": "ok"
        },
        "metrics": {
            "cpu_usage": "23%",
            "memory_usage": "45%",
            "disk_usage": "12%"
        }
    })

if __name__ == '__main__':
    print("🚀 Starting Coolify simulation server...")
    print("📍 Health endpoint: http://localhost:8000/health")
    print("📍 Detailed health: http://localhost:8000/health/detailed")
    print("🔄 Use Ctrl+C to stop")
    app.run(debug=True, host='0.0.0.0', port=8000)