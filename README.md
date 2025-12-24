# Security Log Analysis & Alerting Tool (Python)

## Overview
Security Log Analysis & Alerting Tool is a Python-based defensive security project
designed to simulate core Security Operations Center (SOC) activities.
The tool analyzes real Linux SSH authentication logs to detect brute-force
login attempts and suspicious authentication behavior.

It correlates failed login attempts by source IP address and username,
assigns severity levels based on defined thresholds, and generates structured
security alert reports for analyst review.

---

## Key Features
- Analyzes real Linux SSH authentication logs
- Detects brute-force login attempts
- Correlates activity by IP address and targeted user accounts
- Supports both IPv4 and IPv6 addresses
- Assigns severity levels based on failed login thresholds
- Generates SOC-style text and CSV security reports
- Automatically creates required directories for logs and reports

---

## Project Structure
security-log-analysis/
├── src/
│ └── log_analyzer.py
├── logs/ # Ignored (contains real SSH logs)
├── reports/ # Ignored (generated reports)
├── README.md
├── requirements.txt
└── .gitignore

yaml
Copy code

---

## Requirements
- Python 3.x
- Linux system (tested on Kali Linux)
- SSH service enabled
- systemd journal access

---

## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/abhimanyu0810/security-log-analysis.git
cd security-log-analysis
2. Install Dependencies
bash
Copy code
pip3 install -r requirements.txt
(This project uses standard Python libraries only.)

3. Export SSH Authentication Logs
bash
Copy code
mkdir -p logs
sudo journalctl -u ssh > logs/real_auth.log
sudo chown $USER:$USER logs/real_auth.log
4. Run the Tool
bash
Copy code
python3 src/log_analyzer.py
5. View Generated Reports
bash
Copy code
ls reports
cat reports/security_alert_report.txt
cat reports/security_alert_report.csv
Output
The tool generates:

A text-based SOC-style security alert report

A CSV report suitable for further analysis or dashboards

Example detections include:

High-severity alerts for repeated failed login attempts from a single IP

Medium-severity alerts for repeated attacks against specific user accounts

How It Works
Reads SSH authentication logs from the system journal

Identifies failed login attempts

Correlates IP addresses and usernames

Applies severity thresholds

Generates structured security alert reports

Security Analyst Relevance
This project demonstrates practical skills in:

Log collection and analysis

Incident detection and investigation

Brute-force attack identification

Risk severity classification

SOC-style security reporting

Defensive security automation using Python

Disclaimer
This project is intended for educational and defensive security purposes only.
All logs were generated and analyzed in a controlled lab environment.
Do not use this tool for unauthorized monitoring or offensive activities.

License
MIT License

yaml
Copy code

---

## ✅ AFTER YOU COMMIT

Your GitHub page will show:
- Full description
- Clear installation steps
- Proper formatting
- Professional documentation

This is **exactly what recruiters expect**.

---

## 🧠 FINAL CONFIRMATION

Reply with:
**“README pasted and committed successfully”**

After that, I can:
- Do a **final recruiter-style GitHub review**
- Convert this project into **perfect CV bullets**
- Prepare **Security Analyst interview answers**

You did the right thing asking for a single copy-paste file 👌










