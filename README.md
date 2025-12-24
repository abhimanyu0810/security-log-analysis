# Security Log Analysis & Alerting Tool (Python)

## Overview
This project is a Python-based security monitoring tool designed to simulate
Security Operations Center (SOC) activities. It analyzes real Linux SSH
authentication logs to detect brute-force login attempts and suspicious
authentication behavior.

The tool correlates failed login attempts by source IP address and username,
assigns severity levels based on thresholds, and generates structured
security alert reports for analyst review.

---

## Key Features
- Analyzes real Linux SSH authentication logs
- Detects brute-force login attempts
- Correlates activity by IP address and username
- Supports IPv4 and IPv6 addresses
- Assigns severity levels based on failed login thresholds
- Generates SOC-style text and CSV reports
- Automatically creates required directories for logs and reports

---

## Project Structure
