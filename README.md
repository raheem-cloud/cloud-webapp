# Cloud-Based Web Application Deployment on AWS EC2

A responsive, production-ready web application built with Python Flask, served through Gunicorn WSGI, and actively managed by systemd on an AWS EC2 instance.

## Live Deployment
- **Public IP URL:** `http://13.235.76.168`
- **Cloud Provider:** Amazon Web Services (AWS)
- **Region:** `ap-south-1` (Mumbai)
- **Compute Instance:** `t2.micro` (Ubuntu 24.04 LTS)
- ### Live Application Preview
![Live Demo](live-demo.png)

### Service Status on EC2
![Service Status](service-status.png)

---

## Architecture & Technology Stack
- **Frontend:** Responsive HTML5, CSS3, JavaScript (interactive deep-dive modals and AI assistant widget).
- **Backend Framework:** Python 3, Flask.
- **WSGI Application Server:** Gunicorn (2 worker processes bound to port 80).
- **Process Manager:** Linux `systemd` (`webapp.service`) for automatic daemonization and failure recovery.
- **Security Group:** Inbound TCP port 80 (HTTP) and port 22 (SSH).

---

## Directory Structure
```text
cloud-webapp/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
