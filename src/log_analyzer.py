import os
import re
from collections import defaultdict

# ==============================
# Path Configuration
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "../logs")
REPORT_DIR = os.path.join(BASE_DIR, "../reports")

LOG_FILE = os.path.join(LOG_DIR, "real_auth.log")
TEXT_REPORT = os.path.join(REPORT_DIR, "security_alert_report.txt")
CSV_REPORT = os.path.join(REPORT_DIR, "security_alert_report.csv")

# Ensure required directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# ==============================
# Detection Thresholds
# ==============================
IP_THRESHOLD = 5
USER_THRESHOLD = 3

# ==============================
# Data Structures
# ==============================
ip_attempts = defaultdict(int)
user_attempts = defaultdict(int)

# ==============================
# Regex Patterns (IPv4 + IPv6)
# ==============================
ip_regex = re.compile(r'from ([0-9a-fA-F:.]+)')
user_regex = re.compile(r'Failed password for (invalid user )?(\w+)')

# ==============================
# Log Parsing
# ==============================
if not os.path.exists(LOG_FILE):
    print("[!] Log file not found. Please export SSH logs to logs/real_auth.log")
    exit(1)

with open(LOG_FILE, "r") as log:
    for line in log:
        if "Failed password" in line:
            ip_match = ip_regex.search(line)
            user_match = user_regex.search(line)

            if ip_match:
                ip_attempts[ip_match.group(1)] += 1

            if user_match:
                user_attempts[user_match.group(2)] += 1

# ==============================
# Text Report Generation
# ==============================
with open(TEXT_REPORT, "w") as report:
    report.write("Security Alert Report\n")
    report.write("=====================\n\n")

    report.write("Suspicious IP Activity:\n")
    for ip, count in ip_attempts.items():
        severity = "HIGH" if count >= IP_THRESHOLD else "MEDIUM"
        report.write(f"IP Address      : {ip}\n")
        report.write(f"Failed Attempts : {count}\n")
        report.write(f"Severity        : {severity}\n")
        report.write("-----------------------------\n")

    report.write("\nTargeted User Accounts:\n")
    for user, count in user_attempts.items():
        if count >= USER_THRESHOLD:
            report.write(f"Username        : {user}\n")
            report.write(f"Failed Attempts : {count}\n")
            report.write("Severity        : MEDIUM\n")
            report.write("-----------------------------\n")

# ==============================
# CSV Report Generation
# ==============================
with open(CSV_REPORT, "w") as csv:
    csv.write("Type,Identifier,Failed_Attempts,Severity\n")

    for ip, count in ip_attempts.items():
        severity = "HIGH" if count >= IP_THRESHOLD else "MEDIUM"
        csv.write(f"IP,{ip},{count},{severity}\n")

    for user, count in user_attempts.items():
        if count >= USER_THRESHOLD:
            csv.write(f"USER,{user},{count},MEDIUM\n")

print("[+] Log analysis completed successfully.")
print("[+] Reports generated in the 'reports/' directory.")
