
import csv
from collections import Counter

log_file = "/home/kali/Soc-Log-Analysis/logs/security_events.csv"

failed_logins = []
successful_logins = []
account_lockouts = []

# Read security event logs
with open(log_file, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, skipinitialspace=True)

    reader.fieldnames = [name.strip() for name in reader.fieldnames]

    for row in reader:
        event_id = row["EventID"].strip()

        if event_id == "4625":
            failed_logins.append(row)

        elif event_id == "4624":
            successful_logins.append(row)

        elif event_id == "4740":
            account_lockouts.append(row)

# Count failed login attempts by IP
ip_counts = Counter(
    row["SourceIP"].strip() for row in failed_logins
)

print("===== SOC SECURITY LOG REPORT =====")

print("\nTotal Failed Logins:", len(failed_logins))
print("Total Successful Logins:", len(successful_logins))
print("Total Account Lockouts:", len(account_lockouts))

print("\n===== FAILED LOGIN ANALYSIS =====")

for ip, count in ip_counts.most_common():
    print(ip, ":", count, "failed attempts")

print("\n===== SUSPICIOUS ACTIVITY =====")

for ip, count in ip_counts.items():
    if count >= 5:
        print("[ALERT] Possible brute-force activity")
        print("Suspicious IP:", ip)
        print("Failed attempts:", count)

print("\n===== ACCOUNT LOCKOUT ANALYSIS =====")

for event in account_lockouts:
    print("Locked Account:", event["Username"])
    print("Source IP:", event["SourceIP"])
    print("Time:", event["Timestamp"])

print("\n===== INVESTIGATION COMPLETED =====")

