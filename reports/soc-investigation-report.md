
# SOC Incident Investigation Report

## 1. Project Overview

Project: Windows Security Log Analysis and Threat Detection

Role: Junior SOC Analyst

Environment: Kali Linux

Dataset: Simulated Windows Security Event Logs

Analysis Tool: Python 3

## 2. Investigation Objective

The objective of this investigation was to analyze Windows Security Event Logs, identify suspicious authentication activity, detect possible brute-force patterns, and document security findings.

## 3. Events Investigated

| Event ID | Description |
|---|---|
| 4624 | Successful Login |
| 4625 | Failed Login |
| 4740 | Account Lockout |
| 4634 | Account Logout |
| 4720 | User Account Created |

## 4. Investigation Results

| Activity | Total |
|---|---:|
| Successful Logins | 3 |
| Failed Logins | 7 |
| Account Lockouts | 1 |

## 5. Suspicious Activity Identified

Source IP: 203.0.113.50

Target Account: admin

Failed Login Attempts: 5

Account Lockout: Yes

Observation:

Five failed login attempts were recorded from the same source IP against the admin account within a 20-second period.

An account lockout event was subsequently recorded at 09:15:00.

This activity is consistent with a possible brute-force login attempt.

## 6. Additional Observation

Source IP: 198.51.100.25

Target Account: administrator

Failed Login Attempts: 2

Observation:

Two failed login attempts were recorded against the administrator account.

These attempts did not reach the configured alert threshold of five.

## 7. Detection Method

A Python script was developed to:

- Read CSV security event logs.
- Identify failed login events.
- Count failed login attempts by source IP.
- Detect IP addresses reaching five failed attempts.
- Identify successful logins.
- Identify account lockout events.

## 8. Recommended Security Actions

1. Review the affected admin account.
2. Investigate the source of repeated failed login attempts.
3. Verify whether any unauthorized access occurred.
4. Enforce strong passwords and multi-factor authentication.
5. Monitor repeated authentication failures.
6. Review account lockout policies.

## 9. Conclusion

The investigation identified a possible brute-force pattern involving five failed login attempts from 203.0.113.50 against the admin account.

An account lockout event was also identified.

The Python detection script successfully identified suspicious login activity and generated an alert based on the configured threshold.

No successful compromise was established by this dataset.

Note: This project uses simulated security logs for educational purposes. The source IP addresses are documentation-only examples and do not represent real attackers.

## 10. Project Status

SOC Security Log Analysis and Threat Detection - Completed.
