# Portfolio Activity: Security Incident Report - Malicious Redirect & Brute Force

## 📝 Objective
The objective of this activity was to investigate a website compromise by analyzing network traffic logs (`tcpdump`), identifying the network protocols used in the attack, and documenting the incident. Finally, the goal was to recommend actionable security controls to prevent future brute-force attacks.

## 🛠️ Skills Demonstrated
- Network Traffic Analysis (`tcpdump`)
- Protocol Identification (HTTP, DNS, TCP)
- Incident Investigation and Documentation
- Vulnerability Identification (Default Credentials)
- Threat Mitigation & Access Control (Brute Force Prevention)

## 🏢 Scenario: Website Compromise and Malware Distribution
**Situation:** 
As a cybersecurity analyst for an e-commerce website (`yummyrecipesforme.com`), I was tasked with investigating a critical security event. Customers reported downloading a file from the site that caused their computers to run slowly, and the website owner was simultaneously locked out of the administrative panel. 

**Task:** 
My task was to use a sandbox environment and a network protocol analyzer to recreate the user experience, capture the network traffic, determine how the attack was executed, and draft a formal incident report with remediation steps.

## 🚀 Action Taken
To investigate and document the incident, I performed the following steps:
1. **Traffic Analysis:** Executed `tcpdump` in a sandbox environment while navigating to the compromised URL to capture the data packets.
2. **Protocol Tracking:** Traced the logs to observe the connection sequence. I identified the initial DNS resolution, followed by an **HTTP GET request (Port 80)** to the legitimate site.
3. **Malware Identification:** Observed the network traffic initiating an unprompted file download, followed immediately by a new DNS request and subsequent HTTP traffic redirecting the browser to a malicious domain (`greatrecipesforme.com` at IP `192.0.2.17`).
4. **Root Cause Analysis:** Correlated the traffic analysis with the web server logs, confirming that a threat actor used an automated brute-force attack to exploit default admin credentials. The attacker then embedded a malicious JavaScript payload to force the redirect and malware download.
5. **Reporting & Remediation:** Drafted a comprehensive incident report detailing the attack vector (HTTP protocol) and the sequence of events. I provided specific, actionable recommendations to secure the administrative panel, including enforcing strong password policies, changing default credentials, and implementing CAPTCHA/account lockout thresholds.

## 📈 Results
The completed incident report clearly outlined the timeline and mechanics of the attack for management. The recommended remediation steps provided a direct roadmap for the IT team to lock down the administrative portal, effectively mitigating the risk of future automated brute-force attacks and securing the web server against unauthorized access.

## 📁 Files Included
*   `[Security-incident-report.pdf]` - The formal incident report detailing the traffic analysis, attack vector, and remediation strategies.
*   `[tcpdump-traffic-log.pdf]` - Logs.



