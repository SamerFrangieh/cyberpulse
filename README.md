# CyberPulse – Network Security Monitoring Dashboard

CyberPulse is a full-stack network scanner built with Flask and Nmap. It scans public or local IPs, fetches Shodan data, and presents a real-time dashboard of open ports and services.

## 🚀 Features
- Fast Nmap scanning with port/service/product detection
- Shodan API integration for threat intelligence
- Clean UI styled with TailwindCSS
- JSON-based results with optional PDF export (commented)
- Ready for Docker and cloud deployment

## 🛠️ Tech Stack
- Python, Flask
- Nmap, python-nmap
- Shodan API
- TailwindCSS
- SQLite (via SQLAlchemy)
- JavaScript

## 📦 Setup

```bash
git clone https://github.com/YOUR_USERNAME/cyberpulse-network-monitor.git
cd cyberpulse-network-monitor
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
