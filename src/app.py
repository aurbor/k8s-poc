from flask import Flask, render_template_string
import os
import socket

app = Flask(__name__)

# HTML template with Tailwind CSS
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kubernetes Web App</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen">
    <div class="container mx-auto px-4 py-16">
        <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-8">
            <div class="text-center">
                <h1 class="text-4xl font-bold text-gray-900 mb-4">
                    Hello, Kubernetes! 🚀
                </h1>
                <div class="bg-green-100 text-green-700 px-4 py-2 rounded-md mb-6">
                    Server is running successfully
                </div>
                <p class="text-gray-600 mb-6">
                    This page is being served from a Flask application running in a Kubernetes cluster.
                </p>
                <div class="grid grid-cols-1 gap-4 mb-6">
                    <div class="bg-yellow-50 p-6 rounded-md border-2 border-yellow-200">
                        <h2 class="font-semibold text-yellow-700 mb-2">Pod Information</h2>
                        <p class="text-yellow-600">Hostname: {{ hostname }}</p>
                        <p class="text-yellow-600">Pod IP: {{ pod_ip }}</p>
                        <p class="text-yellow-600">Node Name: {{ node_name }}</p>
                    </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="bg-blue-50 p-4 rounded-md">
                        <h2 class="font-semibold text-blue-700">Server Info</h2>
                        <p class="text-blue-600">Port: 5000</p>
                    </div>
                    <div class="bg-purple-50 p-4 rounded-md">
                        <h2 class="font-semibold text-purple-700">Framework</h2>
                        <p class="text-purple-600">Flask + Tailwind CSS</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def hello_world():
    # Get pod information
    hostname = socket.gethostname()
    pod_ip = socket.gethostbyname(hostname)
    node_name = os.environ.get('NODE_NAME', 'Not available')
    
    return render_template_string(
        html_template,
        hostname=hostname,
        pod_ip=pod_ip,
        node_name=node_name
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
