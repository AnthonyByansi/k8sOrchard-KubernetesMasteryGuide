# Hands-on Lab: Performing Rolling Updates

Welcome to the **Performing Rolling Updates** hands-on lab! In this lab, you'll gain practical experience in updating applications deployed on a Kubernetes cluster using the rolling update strategy.

## Lab Overview

In this lab, you will:

1. Deploy an initial version of an application.
2. Perform a rolling update to a new version of the application.
3. Observe how the rolling update strategy ensures minimal downtime.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- A Kubernetes cluster set up and configured.
- `kubectl` command-line tool installed and configured to access your cluster.
- Docker images for both the initial and new versions of the application.

## Lab Steps

### Step 1: Deploy Initial Application

1. Clone the lab repository: `git clone https://github.com/AnthonyByansi/lab-repo.git`
2. Navigate to the lab directory: `cd lab-repo/12-hands-on-labs/lab-03-rolling-updates`
3. Apply the initial Deployment: `kubectl apply -f initial-deployment.yaml`

### Step 2: Perform Rolling Update

1. Open the `new-version-deployment.yaml` file.
2. Replace `your-new-version-image` with the image of the new version.
3. Apply the new version Deployment: `kubectl apply -f new-version-deployment.yaml`

### Step 3: Observe Rolling Update

1. Monitor the Pods using `kubectl get pods -w`.
2. Watch how Pods are gradually replaced with the new version.

## Conclusion

Congratulations! You've successfully completed the **Performing Rolling Updates** hands-on lab. This lab allowed you to experience the rolling update strategy in action, ensuring smooth transitions between different versions of an application. You now have the skills to update applications in your Kubernetes cluster with minimal disruption.

**Next:** Continue exploring hands-on labs to enhance your understanding of Kubernetes concepts and practices.

