import re
import os
from collections import defaultdict

# Base directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Log and report paths
LOG_FILE = os.path.join(BASE_DIR, "../logs/real_auth.log")
REPORT_FILE = os.path.join(BASE_DIR, "../reports/security_alert_report.txt")

# Data structures
ip_attempts = defaultdict(int)
user_attempts = defaultdict(int)

# Regex patterns (IPv4 + IPv6, valid & invalid users)
ip_regex = re.compile(r'from ([0-9a-fA-F:.]+)')
user_regex = re.compile(r'Failed password for (invalid user )?(\w+)')

# Parse log file
with open(LOG_FILE, "r") as log:
    for line in log:
        if "Failed password" in line:
            ip_match = ip_regex.search(line)
            user_match = user_regex.search(line)

            if ip_match:
                ip_attempts[ip_match.group(1)] += 1

            if user_match:
                user_attempts[user_match.group(2)] += 1

# Generate report
with open(REPORT_FILE, "w") as report:
    report.write("Security Alert Report\n")
    report.write("=====================\n\n")

    report.write("Suspicious IP Activity:\n")
    for ip, count in ip_attempts.items():
        severity = "HIGH" if count >= 5 else "MEDIUM"
        report.write(f"IP Address      : {ip}\n")
        report.write(f"Failed Attempts : {count}\n")
        report.write(f"Severity        : {severity}\n")
        report.write("-----------------------------\n")

    report.write("\nTargeted User Accounts:\n")
    for user, count in user_attempts.items():
        if count >= 3:
            report.write(f"Username        : {user}\n")
            report.write(f"Failed Attempts : {count}\n")
            report.write("Severity        : MEDIUM\n")
            report.write("-----------------------------\n")
