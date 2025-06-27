# Phishing-Simulation
Phishing Simulation


Ethical Phishing Simulation Platform

A Python Flask-based Ethical Phishing Simulation Platform for cybersecurity labs, awareness training, and ethical phishing simulations in controlled environments.

🚀 Features

✅ Web Interface: Send phishing simulation emails easily via a browser.✅ Unique Tracked Links: Generates unique tracked phishing links for each target.✅ SQLite Tracking: Records whether a target user clicked the phishing link.✅ Awareness Landing Page: Displays a safe, educational landing page upon clicking.✅ Reporting: Provides a report of user interactions to measure awareness levels.

🎯 Use Cases

Ethical phishing awareness training within organizations.

Cybersecurity lab environments for demonstrating phishing techniques.

Training SOC and Red Team members on phishing workflows ethically.

Building your ethical phishing service pipeline.

🛠️ Tech Stack

Language: Python 3

Framework: Flask

Database: SQLite (lightweight and portable)

Email: SMTP integration (Gmail/Office 365/SendGrid)

⚙️ Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/ethical-phishing-simulation-platform.git
cd ethical-phishing-simulation-platform

2️⃣ Set Up Virtual Environment

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

pip install flask

4️⃣ Configure Email Credentials

Edit the SMTP_USER and SMTP_PASS in the Python file to match your lab SMTP credentials for sending simulation emails.

5️⃣ Run the Application

python3 ethical_phishing_platform.py

Visit http://localhost:5000 to start sending ethical phishing simulations.

📈 Reporting

Access http://localhost:5000/report to view:

List of target emails.

Whether the user clicked the phishing link.

Use this to identify areas for further awareness training.

