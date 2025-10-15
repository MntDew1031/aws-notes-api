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
