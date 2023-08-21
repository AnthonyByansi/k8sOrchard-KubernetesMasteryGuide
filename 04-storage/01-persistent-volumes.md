# Persistent Volumes in Kubernetes

## Overview

In this section, we'll explore **Persistent Volumes (PVs)** in Kubernetes. PVs provide a way to manage durable storage resources that can be shared across Pods and retained even when Pods are terminated.

## Key Concepts

### Persistent Volume (PV)

A **Persistent Volume (PV)** is a piece of storage that has been provisioned in a cluster. It's a resource that exists independently of Pods and can be claimed by Persistent Volume Claims (PVCs).

### Persistent Volume Claim (PVC)

A **Persistent Volume Claim (PVC)** is a request for storage by a user or Pod. It binds to a PV that matches the requested criteria, allowing the Pod to use the PV for storage.

## PV Types

Kubernetes supports various types of PVs:

- **HostPath:** Uses a local path on the node's filesystem.
- **NFS:** Network File System, for network-based storage.
- **AWS EBS, GCP PD, Azure Disk:** Cloud provider-specific block storage.
- **CSI Drivers:** Container Storage Interface for third-party storage.

## Dynamic Provisioning

PVs can be provisioned statically or dynamically. With **Dynamic Provisioning**, the storage is created automatically when a PVC is requested and no suitable PV exists.

## Reclaim Policies

PVs have different **Reclaim Policies**:

- **Retain:** PV data is retained even after release.
- **Delete:** PV data is deleted when released.
- **Recycle:** Not recommended and is deprecated.

## Using PVs and PVCs

1. Define a PV with the appropriate storage backend.
2. Create a PVC that specifies the desired storage class and resources.
3. Pods can then use the PVC to access the storage.

## Conclusion

Persistent Volumes provide a way to manage storage resources in Kubernetes, ensuring data durability and shared access across Pods.

**Next:** Dive into **Persistent Volume Claims** to see how they interact with PVs to provide storage for Pods.

---

Master the art of managing durable storage resources for your Pods using Kubernetes Persistent Volumes with the Kubernetes Mastery Guide.
