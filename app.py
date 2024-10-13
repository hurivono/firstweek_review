from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    pod_name = os.environ.get('POD_NAME', 'Unknown Pod')
    node_name = os.environ.get('NODE_NAME', 'Unknown Pod')
    pod_namespace = os.environ.get('POD_NAMESPACE', 'Unknown Namespace')
    
    return f'Pod Name: {pod_name}<br>Node Name: {node_name}<br>Pod Namespace: {pod_namespace}, version: 241013_01'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
