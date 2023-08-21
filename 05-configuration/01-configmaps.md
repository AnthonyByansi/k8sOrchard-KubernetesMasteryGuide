
# ConfigMaps in Kubernetes

## Overview

Welcome to the section on **ConfigMaps** in Kubernetes. In this chapter, we'll explore how ConfigMaps enable you to decouple configuration data from your application code and manage configuration settings more efficiently.

## Key Concepts

### ConfigMap

A **ConfigMap** is an API object that stores configuration data in key-value pairs or as configuration files. It allows you to separate configuration concerns from the application logic.

### Use Cases

ConfigMaps are useful for:

- Storing environment variables.
- Providing configuration data to applications.
- Customizing application behavior without code changes.

## Creating ConfigMaps

You can create ConfigMaps using:

1. **Imperative Commands:** Using `kubectl create configmap` or `kubectl create configmap --from-file` commands.
2. **Declarative YAML:** Defining a ConfigMap in a YAML file and applying it using `kubectl apply -f`.

### Example ConfigMap using YAML:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DB_URL: "db.example.com"
  API_KEY: "your-api-key"
```

## Using ConfigMaps in Pods

To consume ConfigMap data in Pods:

1. Reference the ConfigMap in the Pod's configuration.
2. Access the ConfigMap data as environment variables or as mounted files.

### Example Pod using ConfigMap environment variables:

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

## Updating ConfigMaps

ConfigMap data can be updated using the `kubectl edit configmap` command or by editing the YAML file and applying it again.

## Conclusion

ConfigMaps provide a convenient way to manage configuration data separately from your application logic. They enhance flexibility and maintainability in Kubernetes applications.

**Next:** Explore **Secrets** to securely manage sensitive information and credentials.

---

Master the art of managing configuration data for your Kubernetes applications using ConfigMaps with the Kubernetes Mastery Guide.
