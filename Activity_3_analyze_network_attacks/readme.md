# Portfolio Activity 3: Incident Report - SYN Flood DoS Attack

## 📝 Objective
The objective of this activity was to analyze network traffic to identify the root cause of a server outage and to draft a formal incident report for management. This involved understanding TCP/IP protocols, identifying malicious network behavior, and executing immediate containment strategies.

## 🛠️ Skills Demonstrated
- Network Traffic Analysis & Packet Sniffing
- TCP/IP Protocol Analysis (TCP 3-Way Handshake)
- Identifying Denial of Service (DoS) Attacks (SYN Flood)
- Incident Response & Containment
- Technical Communication & Incident Reporting

## 🏢 Scenario: Travel Agency Web Server Outage
**Situation:** 
As a security analyst for a travel agency, I received an automated alert regarding a problem with the company's web server. Employees use this site heavily to book vacation packages for customers. Upon investigation, attempting to load the website resulted in a browser connection timeout error, indicating a complete disruption of service.

**Task:** 
My task was to investigate the cause of the connection timeouts, mitigate the immediate issue to restore normal business operations, and draft an incident report to brief management on the attack, its impact, and recommended next steps.

## 🚀 Action Taken
To investigate and contain the incident, I performed the following steps:
1. **Traffic Analysis:** Deployed a network packet sniffer to capture and inspect data packets traveling to and from the web server.
2. **Identification:** Analyzed the captured traffic and discovered an abnormally high volume of TCP SYN (Synchronize) requests originating from a single, unfamiliar IP address. 
3. **Diagnosis:** Determined that the web server was the victim of a **SYN Flood Denial of Service (DoS) attack**. The server was overwhelmed by half-open connections, exhausting its resources and preventing it from responding to legitimate employee traffic.
4. **Containment:** Temporarily took the web server offline to allow it to recover and clear the half-open connections.
5. **Mitigation:** Configured the company's network firewall to block the malicious IP address responsible for the abnormal SYN requests.
6. **Reporting:** Drafted a comprehensive incident report to alert management. I detailed the attack mechanism, the impact on business operations, and highlighted the need for long-term solutions, noting that simple IP blocking is insufficient against attackers who spoof IP addresses.

## 📈 Results
The immediate threat was successfully contained, and the web server was restored to normal operating status. The resulting incident report provided management with clear, non-technical explanations of the event and actionable recommendations for implementing robust, long-term DoS protection strategies.

## 📁 Files Included
*   `[Cybersecurity-incident-report.pdf]` - The formal cybersecurity incident report detailing the SYN flood analysis and response.
*   `[HTTP-log.pdf]` - logs.

