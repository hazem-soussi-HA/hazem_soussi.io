# Hazem Soussi SaaS Landing Page

A modern single-page SaaS-style landing page showcasing services in Cloud Computing and DevOps, built with Python and Streamlit.

## Features

- Hero section with call-to-action
- Services & Skills showcase with progress indicators
- Featured projects gallery
- Certifications display
- Professional experience timeline
- Testimonials section
- Contact form and downloadable CV
- Links to professional profiles

## Featured Projects

### MERN Stack SaaS Platform
Full-stack web app with cloud deployment on AWS, featuring secure authentication and scalable architecture.

**Technologies:** React, Node.js, MongoDB, AWS

[View on GitHub](https://github.com/hazem-soussi-HA/MERN-Stack-Tutorial)

### DevSecOps CI/CD Pipeline
Automated pipeline with security scanning, vulnerability assessment, and compliance checks for containerized apps.

**Technologies:** Jenkins, Docker, Kubernetes, OWASP ZAP

[View on GitHub](https://github.com/hazem-soussi-HA/Kali-Linux-Container-on-Proxmox)

### Cloud AI Model Deployment
Serverless deployment of LLMs on GCP with auto-scaling, monitoring, and cost optimization.

**Technologies:** Python, GCP, Terraform, Prometheus

[View on GitHub](https://github.com/hazem-soussi-HA/ollama)

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Run the FastAPI backend for dynamic data:
   ```bash
   uvicorn api:app --reload
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

## Data Sources

- GitHub profile scraped for repos and bio
- CV files for download