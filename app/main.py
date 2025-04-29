from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>FluxCD Demo</title>
            <style>
                body {
                    background: linear-gradient(135deg, #2980b9, #6dd5fa, #ffffff);
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    text-align: center;
                    padding: 80px;
                    color: #2c3e50;
                }
                .container {
                    background-color: #ffffffcc;
                    padding: 40px;
                    border-radius: 12px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.2);
                    display: inline-block;
                }
                h1 {
                    font-size: 36px;
                    margin-bottom: 20px;
                }
                p {
                    font-size: 20px;
                    margin-top: 10px;
                    color: #34495e;
                }
                .footer {
                    margin-top: 40px;
                    font-size: 14px;
                    color: #7f8c8d;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 GitHub Actions + FluxCD Demo</h1>
                <p>Deployed successfully to your Kubernetes cluster</p>
                <p><strong>Timestamp:</strong> {}</p>
            </div>
            <div class="footer">Made with ❤️ for DevOps demo</div>
        </body>
    </html>
    '''.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/healthz')
def health():
    return jsonify(status="ok", time=datetime.utcnow().isoformat())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


