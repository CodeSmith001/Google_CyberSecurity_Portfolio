# Portfolio Activity: Network Traffic Analysis (DNS and ICMP)

## 📝 Objective
The objective of this activity was to use a network protocol analyzer (`tcpdump`) to capture and analyze network traffic in transit. The goal was to investigate a reported website outage, analyze the resulting logs, and identify the specific network protocols and services affected by a cybersecurity incident.

## 🛠️ Skills Demonstrated
- Network Traffic Analysis
- Packet Sniffing via `tcpdump`
- Protocol Analysis (DNS, UDP, ICMP)
- Identifying Network Service Failures
- Incident Reporting and Escalation

## 🏢 Scenario: IT Services Client Outage
**Situation:** 
As a cybersecurity analyst for an IT services company, I was notified that several customers were unable to access a client's website (`www.yummyrecipesforme.com`). Users reported receiving a "destination port unreachable" error. 

**Task:** 
My task was to troubleshoot the connection issue, capture the network data packets during the connection attempt, and analyze the logs to determine the root cause of the website outage.

## 🚀 Action Taken
To investigate the incident, I performed the following steps:
1. **Traffic Capture:** Attempted to connect to the client website while running the `tcpdump` network analyzer tool to capture the data packets in transit.
2. **Log Analysis:** Reviewed the `tcpdump` logs, identifying the source IP, destination IP, protocols used, and specific port numbers.
3. **Protocol Identification:** Traced the initial connection attempt. I observed the browser sending a **UDP** packet requesting an "A record" (IP address) from the **DNS** server (IP 203.0.113.2) on **Port 53**.
4. **Error Diagnosis:** Identified the immediate response in the logs: an **ICMP** packet returning the error message `"udp port 53 unreachable"`. 
5. **Root Cause Determination:** Concluded that the website outage was not an issue with the web server itself, but rather a failure of the DNS service. Because the DNS server was not listening on Port 53, the domain name could not be resolved to an IP address, preventing the HTTPS request from ever being sent.
6. **Reporting:** Drafted an incident report escalating the issue to security engineers, noting that the DNS failure was likely caused by a targeted DDoS attack or a recent firewall misconfiguration.

## 📈 Results
By successfully capturing and interpreting the raw `tcpdump` data, I was able to rapidly isolate the failure point in the TCP/IP networking model (the Internet layer/ICMP and Application layer/DNS). The resulting incident report provided security engineers with the exact IP addresses, timestamps, and protocol errors needed to begin immediate remediation of the DNS server.

## 📁 Files Included
*   `[Cybersecurity-incident-report-network-traffic-analysis.pdf]` - The formal incident report detailing the network traffic analysis and findings.


