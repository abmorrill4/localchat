# Ultra-Minimal Local AI Chat

A lightweight, LAN-only, Dockerized chat UI for running local LLMs via LM Studio.  
No external dependencies, no cloud, no bloat—just pure Flask, HTML, and simple multi-user authentication.

## Features

- **Web 1.0 Vibe:** Pure HTML and minimal CSS, no JavaScript frameworks or client-side dependencies.
- **Multi-User Login:** Passwords stored securely (hashed, not plaintext), login/logout supported.
- **Per-User Chat History:** Each user’s chat is persistent across sessions, stored locally.
- **Dockerized:** One-command setup with Docker Compose, reproducible and portable.
- **Privacy-First:** No data ever leaves your network. Designed for home labs and tinkerers.
- **LM Studio Integration:** Works with any local model accessible via LM Studio’s API.



## Quickstart

### **Prerequisites**
- **GoingMerry:** Linux host with Docker and Git installed.
- **Theseus:** Windows PC running LM Studio, with the API enabled on your LAN.
- Both hosts must be on the same network.

### **Setup Instructions**

#### 1. Clone this repo to your Linux box:
```bash
git clone https://github.com/abmorrill4/localchat.git
cd localchat
