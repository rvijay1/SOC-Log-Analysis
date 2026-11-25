
# SOC Log Analysis and Threat Detection

## Project Overview

This project demonstrates beginner-level Security Operations Center (SOC) activities through Windows Security Event Log analysis.

The objective is to identify suspicious authentication activity, investigate repeated failed login attempts, detect possible brute-force patterns, and generate a security investigation report.

## Tools and Technologies

- Kali Linux
- Python 3
- Linux Commands
- CSV Security Event Logs

## Project Features

- Windows Security Event Log analysis
- Successful login identification
- Failed login identification
- Suspicious IP address detection
- Possible brute-force activity detection
- Account lockout investigation
- Automated Python log analysis
- SOC incident report preparation

## Windows Event IDs Analyzed

| Event ID | Description |
|---|---|
| 4624 | Successful Login |
| 4625 | Failed Login |
| 4740 | Account Lockout |
| 4634 | Account Logout |
| 4720 | User Account Created |

## Key Findings

| Investigation | Result |
|---|---:|
| Successful Logins | 3 |
| Failed Logins | 7 |
| Account Lockouts | 1 |
| Primary Suspicious IP | 203.0.113.50 |

The investigation identified five failed login attempts from 203.0.113.50 against the admin account, followed by an account lockout event.

This pattern was classified as possible brute-force activity.

## Project Structure

```text
Soc-Log-Analysis/
├── evidence/
│   ├── account_lockouts.txt
│   ├── failed_logins.txt
│   ├── successful_logins.txt
│   └── suspicious_ips.txt
├── logs/
│   └── security_events.csv
├── reports/
│   └── soc-investigation-report.md
├── scripts/
│   └── log_analyzer.py
└── README.md
```

## How to Run

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd Soc-Log-Analysis
```

Run the Python detection script:

```bash
python3 scripts/log_analyzer.py
```

## Learning Outcomes

- Understanding Windows Security Event IDs
- Analyzing authentication logs
- Identifying repeated failed login attempts
- Detecting possible brute-force activity
- Using Python for basic security automation
- Preparing SOC investigation reports

## Disclaimer

This project uses simulated Windows Security Event Logs for educational and training purposes.

The IP addresses are documentation-only example addresses and do not represent real attackers or actual security incidents.
