from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Hazem Soussi Portfolio API", version="1.0.0")

class Project(BaseModel):
    title: str
    desc: str
    link: str
    tech: str
    image: str

class Testimonial(BaseModel):
    name: str
    role: str
    message: str
    image: str

class Certification(BaseModel):
    name: str

class Experience(BaseModel):
    title: str
    description: str

# Sample data
projects = [
    {
        "title": "MERN Stack SaaS Platform",
        "desc": "Full-stack web app with cloud deployment on AWS, featuring secure authentication and scalable architecture.",
        "link": "https://github.com/hazem-soussi-HA/MERN-Stack-Tutorial",
        "tech": "React, Node.js, MongoDB, AWS",
        "image": "https://images.unsplash.com/photo-1637937459053-c788742455be?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y2xvdWQlMjBjb21wdXRpbmclMjBkZXZlbG9wbWVudHxlbnwwfHwwfHx8MA%3D%3D&fm=jpg&q=60&w=3000"
    },
    {
        "title": "DevSecOps CI/CD Pipeline",
        "desc": "Automated pipeline with security scanning, vulnerability assessment, and compliance checks for containerized apps.",
        "link": "https://github.com/hazem-soussi-HA/Kali-Linux-Container-on-Proxmox",
        "tech": "Jenkins, Docker, Kubernetes, OWASP ZAP",
        "image": "https://plus.unsplash.com/premium_photo-1683121079680-6f3f756f9f27?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGNsb3VkJTIwY29tcHV0aW5nJTIwZGV2ZWxvcG1lbnR8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000"
    },
    {
        "title": "Cloud AI Model Deployment",
        "desc": "Serverless deployment of LLMs on GCP with auto-scaling, monitoring, and cost optimization.",
        "link": "https://github.com/hazem-soussi-HA/ollama",
        "tech": "Python, GCP, Terraform, Prometheus",
        "image": "https://plus.unsplash.com/premium_photo-1714618828448-abf8732500c6?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8Y2xvdWQlMjBjb21wdXRpbmclMjBkZXZlbG9wbWVudHxlbnwwfHwwfHx8MA%3D%3D&fm=jpg&q=60&w=3000"
    }
]

testimonials = [
    {
        "name": "John Doe",
        "role": "CTO at TechCorp",
        "message": "Hazem transformed our infrastructure with his DevSecOps expertise. Highly recommended!",
        "image": "https://via.placeholder.com/100"
    },
    {
        "name": "Jane Smith",
        "role": "Project Manager at Innovate Solutions",
        "message": "Outstanding cloud architecture skills. Delivered scalable solutions on time.",
        "image": "https://via.placeholder.com/100"
    },
    {
        "name": "Alex Johnson",
        "role": "Founder at Startup ABC",
        "message": "Hazem's full-stack development brought our app to life. Professional and skilled.",
        "image": "https://via.placeholder.com/100"
    }
]

certifications = [
    "AWS Certified Solutions Architect",
    "Certified Kubernetes Administrator (CKA)",
    "Docker Certified Associate",
    "Certified DevSecOps Engineer",
    "CompTIA Security+",
    "Scrum Master Certification"
]

experiences = [
    {
        "title": "DevSecOps Engineer - TechCorp (2023-Present)",
        "description": "Implemented DevSecOps practices across enterprise applications, reducing security vulnerabilities by 60%. Led cloud migration to AWS with automated security scanning in CI/CD pipelines."
    },
    {
        "title": "Cloud Architect - Innovate Solutions (2021-2023)",
        "description": "Designed and deployed multi-cloud infrastructures on AWS and Azure, focusing on scalability, security, and cost optimization. Integrated DevSecOps tools for compliance automation."
    },
    {
        "title": "Full-Stack Developer - Startup ABC (2020-2021)",
        "description": "Developed secure web applications with React and Node.js, deployed on cloud platforms with basic DevOps practices."
    }
]

@app.get("/projects", response_model=List[Project])
def get_projects():
    return projects

@app.get("/testimonials", response_model=List[Testimonial])
def get_testimonials():
    return testimonials

@app.get("/certifications", response_model=List[Certification])
def get_certifications():
    return certifications

@app.get("/experiences", response_model=List[Experience])
def get_experiences():
    return experiences

@app.get("/")
def read_root():
    return {"message": "Welcome to Hazem Soussi Portfolio API"}