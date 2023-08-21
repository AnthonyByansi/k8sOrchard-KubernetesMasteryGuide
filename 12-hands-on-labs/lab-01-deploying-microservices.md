# Hands-on Lab: Deploying Microservices in Kubernetes

Welcome to the **Deploying Microservices in Kubernetes** hands-on lab! In this lab, you'll have the opportunity to apply the knowledge you've gained from the Kubernetes Mastery Guide by deploying a microservices application on a Kubernetes cluster.

## Lab Overview

In this lab, you will:

1. Create Kubernetes Deployments for frontend and backend microservices.
2. Configure Services to expose the application externally.
3. Observe the application running and test its functionality.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- A Kubernetes cluster set up and configured.
- `kubectl` command-line tool installed and configured to access your cluster.
- Docker images for the frontend and backend microservices available in a container registry.

## Lab Steps

### Step 1: Deploy Frontend and Backend

1. Clone the lab repository: `git clone https://github.com/AnthonyByansi/lab-repo.git`
2. Navigate to the lab directory: `cd lab-repo/12-hands-on-labs/lab-01-deploying-microservices`

### Step 2: Create Deployments

1. Open the `app-deployment.yaml` file.
2. Replace `your-frontend-image` and `your-backend-image` with actual image names.
3. Apply the Deployment: `kubectl apply -f app-deployment.yaml`

### Step 3: Expose the Application

1. Open the `service.yaml` file.
2. Apply the Service: `kubectl apply -f service.yaml`

### Step 4: Verify Deployment

1. Get the Service external IP: `kubectl get svc microservices-service`
2. Access the application in your web browser using the external IP.

## Conclusion

Congratulations! You've successfully completed the **Deploying Microservices in Kubernetes** hands-on lab. This lab provided practical experience in deploying microservices on a Kubernetes cluster. You can now explore further and apply the skills you've gained to more complex scenarios.

**Next:** Continue with the hands-on labs to dive deeper into Kubernetes concepts and challenges.
