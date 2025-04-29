from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get current timestamp for dynamic content
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return render_template('index.html', time=current_time)

@app.route('/healthz')
def health():
    # Health check for Kubernetes readiness
    return jsonify(status="ok", time=datetime.utcnow().isoformat())

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error starting the application: {e}")

