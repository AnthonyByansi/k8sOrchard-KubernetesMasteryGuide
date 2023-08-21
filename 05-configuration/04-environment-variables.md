# Environment Variables in Kubernetes

## Overview

In the **Environment Variables** section of Kubernetes, we'll explore how you can use environment variables to configure and customize your application's behavior within the cluster.

## Key Concepts

### Environment Variables

Environment variables are key-value pairs that provide runtime configuration to your application. They enable dynamic changes without modifying the code.

### Use Cases

- **Database URLs:** Configure connection strings.
- **API Keys:** Store sensitive keys without hardcoding.
- **Feature Flags:** Toggle functionality at runtime.

## Setting Environment Variables

You can set environment variables in Kubernetes in various ways.

### 1. Directly in Pod Specification:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
    - name: app-container
      image: my-app-image
      env:
        - name: DB_URL
          value: "database.example.com"
```

### 2. Using ConfigMaps:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
    - name: app-container
      image: my-app-image
      envFrom:
        - configMapRef:
            name: app-config
```

### 3. Using Secrets:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
    - name: app-container
      image: my-app-image
      envFrom:
        - secretRef:
            name: api-secret
```

## Managing Dynamic Configurations

Environment variables provide a way to manage dynamic configurations across different environments (e.g., development, testing, production) without code changes.

## Conclusion

Leveraging environment variables empowers you to customize your application's behavior within Kubernetes. They ensure flexibility and maintainability in different deployment scenarios.

**Next:** Dive into the concepts of **ConfigMaps** and **Secrets** for advanced configuration management.

---

Master the art of using environment variables to dynamically configure and customize your Kubernetes applications with the Kubernetes Mastery Guide.
