# Kubernetes Flask Web App Demo

A demonstration project showing how to deploy a Flask web application to Kubernetes using Helm, with both Nginx Ingress Controller and Traefik Gateway API support.

## Overview

This project deploys a simple Flask web application that displays basic pod information. The application is accessible through:
- http://k8s-poc.dev.local (via Nginx Ingress on port 80)
- http://k8s-poc.api.dev.local (via Traefik Gateway API on port 8000)

## Prerequisites

- Docker
- Kubernetes cluster (e.g., minikube, kind, or k3d)
- Helm v3
- kubectl
- Local DNS setup (add the following to your `/etc/hosts`):
  ```
  127.0.0.1 k8s-poc.dev.local
  127.0.0.1 k8s-poc.api.dev.local
  ```

## Components

- **Web Application**: Python Flask app showing pod information
- **Helm Charts**:
  - `web-app`: Main application deployment
  - `gateway`: Traefik Gateway API configuration

## Installation

1. Start your local Kubernetes cluster (eg. Docker Desktop or minikube)

2. Install the Nginx Ingress Controller:
   ```bash
   helm upgrade --install ingress-nginx ingress-nginx --repo https://kubernetes.github.io/ingress-nginx --namespace ingress-nginx --create-namespace
   ```

3. Install Traefik:
   ```bash
   helm upgrade --install traefik ./charts/traefik --namespace traefik --create-namespace
   ```

4. Build and load the web application Docker image:
   ```bash
   docker build -t web-app:1.2 src/
   ```

5. Deploy the web application:
   ```bash
   helm upgrade --install web-app ./charts/web-app --namespace default
   ```

## Verification

1. Check if pods for the web app, ingress-nginx and traefik are running:
   ```bash
   kubectl get pods --all-namespaces
   ```

2. Access the application:
   - Via Nginx Ingress: http://k8s-poc.dev.local
   - Via Traefik Gateway: http://k8s-poc.api.dev.local:8000

3. Verify the API Gateway response header:
   - Access http://k8s-poc.api.dev.local:8000 in your browser
   - Open Chrome Developer Tools (F12 or Right Click → Inspect)
   - Go to the Network tab
   - Click on the request to the domain
   - Look for the `X-Api-Gateway` response header in the Headers section
   - You should see: `X-Api-Gateway: Served by Traefik`

## Configuration

The application can be configured through the Helm values files:
- `charts/web-app/values.yaml`: Main application configuration
- `charts/gateway/values.yaml`: Traefik Gateway configuration

Key configurations include:
- Number of replicas
- Image version
- Service ports
- Ingress/Gateway settings

## Development

To make changes to the application:

1. Modify the Flask application in `src/app.py`
2. Build a new Docker image with an updated tag
3. Update the image tag in `charts/web-app/values.yaml`
4. Upgrade the Helm release:
   ```bash
   helm upgrade web-app ./charts/web-app
   ```

## Cleanup

To remove the deployment:

``` bash
helm uninstall web-app
helm uninstall gateway -n gateway
helm uninstall ingress-nginx -n ingress-nginx
```

## License

[MIT License](LICENSE)