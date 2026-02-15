# 📸 Auto-Grayscale Magic

A production-oriented full-stack application that enables users to upload images and automatically convert them to grayscale in real time.

This project demonstrates modern cloud-native development practices using **Next.js, FastAPI, Docker, Kubernetes, Terraform, and GitHub Actions**, with a fully containerized and reproducible infrastructure.

---

## 🚀 Project Overview

Auto-Grayscale Magic showcases:

* Full-stack architecture (Frontend + Backend separation)
* Real-time image processing
* Containerized microservices
* Kubernetes-based deployment
* Infrastructure as Code (Terraform)
* Multi-architecture CI/CD pipeline (amd64 / arm64)

Designed as a DevOps-ready portfolio project reflecting production workflows.

---

## 🛠 Tech Stack

| Category                   | Technology           | Purpose                                     |
| -------------------------- | -------------------- | ------------------------------------------- |
| **Frontend**               | Next.js (TypeScript) | Modern React framework with App Router      |
|                            | Tailwind CSS         | Utility-first responsive styling            |
| **Backend**                | FastAPI (Python)     | High-performance REST API                   |
|                            | Pillow               | Image processing (grayscale transformation) |
| **Database**               | SQLite               | Metadata storage                            |
| **Containerization**       | Docker               | Application packaging                       |
| **Orchestration**          | Kubernetes           | Pod & service management                    |
| **Infrastructure as Code** | Terraform            | Declarative environment provisioning        |
| **CI/CD**                  | GitHub Actions       | Automated multi-platform Docker builds      |

---

## 🏗 Architecture

Frontend and Backend are independently containerized and deployed to Kubernetes.

* Frontend communicates with Backend via Kubernetes Service DNS.
* Backend handles image processing and metadata storage.
* Docker images are built automatically and pushed through GitHub Actions.
* Terraform manages infrastructure resources declaratively.

---

## 📂 Project Structure

```
.
├── .github/workflows/      # CI/CD pipelines (multi-arch Docker builds)
├── backend/                # FastAPI application
│   ├── routes/             # API modules (Auth, Image Processing)
│   ├── uploads/            # Processed image storage
│   └── main.py             # Entry point
├── frontend/               # Next.js (App Router)
│   ├── src/components/     # UI components
│   └── src/app/            # Routing & layout
├── k8s/                    # Kubernetes manifests
└── terraform/              # Infrastructure as Code
    ├── main.tf
    ├── variables.tf
    └── outputs.tf
```

---

## ⚙️ Key Features

### 🎨 Real-Time Image Processing

* Image upload via frontend
* Server-side grayscale conversion using Pillow
* Processed images stored and retrievable

### 🏗 Infrastructure as Code

* Terraform provisions and manages Docker-related resources
* Reproducible local development environment

### 🤖 Automated CI/CD

* GitHub Actions builds Docker images for:

  * amd64 (Intel)
  * arm64 (Apple Silicon / M-series)
* Automatic image push to Docker Hub

### 🌐 Kubernetes Service Communication

* Internal DNS-based service discovery
* No hardcoded IP configuration
* Clean microservice abstraction

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

* Docker Desktop (Kubernetes enabled)
* Terraform CLI
* kubectl

---

### 2️⃣ Infrastructure Setup

```bash
cd terraform
terraform init
terraform apply
```

---

### 3️⃣ Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

Force refresh deployment:

```bash
kubectl rollout restart deployment frontend-app
kubectl rollout restart deployment backend-app
```

---

### 4️⃣ Access the Application

| Service                  | URL                        |
| ------------------------ | -------------------------- |
| Frontend                 | http://localhost:3000      |
| Backend API (Swagger UI) | http://localhost:8000/docs |

---

## 📦 Engineering Highlights

* Clean separation of concerns (UI / API / Infra)
* Modular FastAPI routing structure
* Production-style CI/CD workflow
* Multi-architecture container support
* Declarative infrastructure management
* Cloud-native architecture principles

---

## 🎯 Why This Project Matters

This project is designed to reflect real-world DevOps and full-stack engineering workflows, including:

* Container-first design
* Kubernetes-native deployment
* Infrastructure automation
* Cross-platform build pipelines
* Scalable service communication patterns

It serves as a strong foundation for DevOps, SRE, and Cloud Engineer portfolios.

---
