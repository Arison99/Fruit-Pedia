# Fruit Encyclopedia

A simple Flask application that provides information about various fruits. The app fetches data from the Fruityvice API and allows users to search for fruits by name, family, or genus.

## Features

- Fetches fruit data from the Fruityvice API
- Displays fruit information including name, family, order, genus, and nutrition
- Search functionality to filter fruits by name, family, or genus

## Prerequisites

- Docker
- Kubernetes (optional, for deployment)

## Running the App Locally

### Step 1: Clone the Repository

```sh
git clone https://github.com/your-username/fruit-encyclopedia.git
cd fruit-encyclopedia
```
### Step 2: Create a Virtual Environment (Optional)

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

 ```

### Step 3: Install Dependencies
 ```sh
 pip install -r [requirements.txt](http://_vscodecontentref_/1)
 ```
### Step 4: Run the Flask App
```sh
python [app.py](http://_vscodecontentref_/2)
```
### The app will be running at http://127.0.0.1:5000.

### Running the App with Docker
```sh
python [app.py](http://_vscodecontentref_/2)
```
### Step 1: Build the Docker Image
```sh
docker build -t your-username/fruit-encyclopedia:latest .
```
### Step 2: Run the Docker Container

```sh
docker run -p 5000:5000 your-username/fruit-encyclopedia:latest
```
### The app will be accessible at http://localhost:5000.

### Deploying the App to Kubernetes
### Step 1: Ensure Kubernetes is Running
 Make sure your Kubernetes cluster is running. If you're using Docker Desktop, ensure that Kubernetes is enabled and running.

### Step 2: Apply the Deployment and Service YAML Files
```sh
kubectl apply -f [deployment.yaml](http://_vscodecontentref_/3)
kubectl apply -f [service.yaml](http://_vscodecontentref_/4)
```
### Step 3: Access the Application
```sh
kubectl get services
```
Check the status of the service to get the external IP:

Access the application using the external IP provided by the LoadBalancer service.

### Troubleshooting
If you encounter issues with dependencies, ensure that your requirements.txt file is up to date.
For Docker-related issues, ensure Docker is running and properly configured on your machine.
For Kubernetes-related issues, ensure your cluster is running and kubectl is configured correctly.