# Prometheus Monitoring in Kubernetes

## Introduction

Welcome to the **Prometheus Monitoring** section in Kubernetes. In this chapter, we'll deep-dive into Prometheus, an open-source monitoring system widely used in Kubernetes environments, and learn how to set it up for effective cluster monitoring.

## Key Concepts

### Prometheus Overview

**Prometheus** is a powerful time-series-based monitoring and alerting system. It collects metrics from various sources and provides a flexible querying language.

### Metrics Collection

Prometheus scrapes metrics from endpoints exposed by monitored targets, such as Pods, nodes, and services.

## Setting Up Prometheus

### Prometheus Deployment

You can deploy Prometheus using Kubernetes manifests or tools like Helm.

### Service Discovery

Prometheus supports **service discovery**, automatically discovering and scraping targets based on label selectors.

### Example Prometheus Configuration:

```yaml
scrape_configs:
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app]
        action: keep
        regex: your-app-name
```

## PromQL - Prometheus Query Language

### Querying Metrics

Prometheus offers a powerful querying language called **PromQL** to retrieve and manipulate metrics.

### Example PromQL Query:

```promql
rate(http_requests_total{job="api"}[5m])
```

## Alerting with Prometheus

### Alerting Rules

Prometheus allows you to define alerting rules based on metric conditions. When a rule triggers, alerts are sent to alert managers.

### Example Alerting Rule:

```yaml
groups:
  - name: your-alert-group
    rules:
      - alert: HighErrorRate
        expr: http_errors / http_requests > 0.5
        for: 5m
        labels:
          severity: critical
```

## Conclusion

Prometheus is a versatile monitoring system that empowers you to gain deep insights into your Kubernetes cluster and applications. By setting up Prometheus, writing PromQL queries, and defining alerting rules, you can proactively manage and monitor your environment.

**Next:** Explore **Grafana** to visualize and create interactive dashboards for Prometheus metrics.

---

Master the art of monitoring your Kubernetes applications and infrastructure using Prometheus with the Kubernetes Mastery Guide.
