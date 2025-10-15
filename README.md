# AWS Notes API (Showcase)

A secure Flask REST API deployed on AWS using:
- **EC2 (Ubuntu)** for hosting Flask
- **RDS (PostgreSQL)** for data storage
- **Application Load Balancer (ALB)** for HTTPS
- **ACM** for certificates
- **Route 53** for DNS

> This repository is **for showcase purposes only**.  
> It contains the structure, code, and documentation of a working AWS deployment but **no live credentials** or AWS connections.

---

## Live Demo
🔗 **https://notes.shadow1231.com**  
(API write operations are protected by an API key.)

---

## Features
- `GET /notes` → read notes (public)
- `POST /notes` → add a note (requires `X-API-KEY`)
- API key protection for write routes
- Backed by RDS PostgreSQL
- HTTPS via ALB + ACM

---

## Architecture
Client → Route53 (A/ALIAS) → ALB (443) → EC2 (Flask:5000) → RDS (5432)

---

## Local Development
```bash
pip install -r requirements.txt
export DB_HOST=db-endpoint-placeholder.rds.amazonaws.com
export DB_USER=postgres
export DB_PASS=fakepassword
export API_KEY=fakeapikey
python app.py
```
---

## AWS Deployment Summary

Create RDS PostgreSQL and table (see sql/init.sql).

Launch EC2 (Ubuntu), install Python, copy app.

ALB → Target Group (port 5000, health /).

ACM → Issue SSL cert for subdomain.

Route 53 → A record (Alias) → ALB.

EC2 → Flask systemd service (deploy/flaskapp.service.example).

---

## Security

.env excluded from version control

API key required for write methods

HTTPS enforced through ALB

Port 5000 accessible only from ALB security group
