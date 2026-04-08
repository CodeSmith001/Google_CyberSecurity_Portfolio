# Cybersecurity Portfolio

Welcome to my cybersecurity portfolio. This repository is a curated collection of practical projects, incident reports, and technical documentation I created while completing the Google Cybersecurity Professional Certificate. 

Rather than just studying theory, my goal over the last two months of intensive daily study was to build hands-on muscle memory. This repository serves as proof of my ability to deploy security tools, analyze network traffic, write automation scripts, and document complex technical issues for stakeholders.

## 🛠️ Core Skills Demonstrated
*   **SIEM Operations & Threat Hunting:** Wazuh, OpenSearch, Log Aggregation, Boolean Querying.
*   **Network Security:** Packet capture and analysis (`tcpdump`, Wireshark), Protocol Analysis (HTTP, DNS, ICMP, TCP), IDS alerts (Suricata).
*   **Endpoint & System Hardening:** Linux CLI, File Permissions (`chmod`, Principle of Least Privilege).
*   **Security Automation & Data Analysis:** Python (File I/O, Algorithms), SQL (Database querying, filtering).
*   **Incident Response & GRC:** NIST Cybersecurity Framework (CSF), NIST SP 800-30, Vulnerability Assessments, Threat Modeling.

---

## 📁 Projects Directory

Here is a breakdown of the projects contained in this repository. Click on any project title to view the full documentation, technical walkthrough, and associated files.

### 1. [My Professional Statement](./Activity_1_My_Professional_Statement)
*   **Description:** My core professional summary outlining my technical competencies, transferable skills, and career objectives as an aspiring SOC Analyst.

### 2. [Internal Security Audit & Compliance](./Activity_2_internal_security_audit_and_compliance)
*   **Description:** Performed an internal security audit for a fictional growing business. Evaluated current access controls against the NIST CSF and identified potential compliance liabilities regarding PCI-DSS and GDPR.

### 3. [Analyze Network Attacks](./Activity_3_analyze_network_attacks)
*   **Description:** Analyzed `.pcap` files to investigate a simulated network outage. Successfully identified a Denial of Service (SYN Flood) attack and compiled the findings into a formal Incident Report.

### 4. [Analyze Network Layer Communications](./Activity_4_analyze_network_layer_communications)
*   **Description:** Utilized `tcpdump` to capture and analyze data packets in transit, identifying specific DNS and ICMP protocol failures causing a web server outage.

### 5. [Apply OS Hardening Techniques](./Activity_5_apply_OS_hardening_techniques)
*   **Description:** Investigated a malicious redirect and brute-force attack. Analyzed HTTP traffic to trace the malware download and recommended OS-level remediation strategies.

### 6. [Use the NIST Cybersecurity Framework](./Activity_6_use_the_NIST_cybersecurity_framework)
*   **Description:** Mapped a Denial of Service (ICMP Flood) attack to the five core functions of the NIST CSF (Identify, Protect, Detect, Respond, Recover) to build a proactive defense strategy.

### 7. [Linux File Permissions](./Activity_7_use_linux_commands_to_manage_file_permissions)
*   **Description:** Audited a simulated research team's Linux directory. Used the Bash command line to identify unauthorized access vectors and modified 10-character permission strings using `chmod` to enforce the Principle of Least Privilege.

### 8. [Apply Filters to SQL Queries](./Activity_8_apply_filters_to_SQL_queries)
*   **Description:** Crafted complex SQL `SELECT` queries utilizing logical operators (`AND`, `OR`, `NOT`) and wildcards (`LIKE`) to investigate after-hours login anomalies and identify specific employee machines for security patching.

### 9. [Vulnerability Assessment & Risk Management](./Activity_9_vulnerability_assessment_&_risk_management)
*   **Description:** Conducted a qualitative risk assessment on an exposed database. Utilized the NIST SP 800-30 framework to identify threat sources, calculate risk scores, and draft an actionable remediation strategy for stakeholders.

### 10. [Wazuh SIEM Setup](./Activity_10_wazuh_setup) *(Featured Project)*
*   **Description:** Deployed a local Wazuh SIEM using VMware. Troubleshot Linux kernel/seccomp conflicts, built a Filebeat ingestion pipeline using a Python HTTP server, and ingested 100,000+ logs. Wrote targeted queries to isolate an SSH brute-force attack.

### 11. [The Incident Handler's Journal](./Activity_11_incident-handler's-journal)
*   **Description:** A formalized running log of security investigations. Documents the practical usage of OSINT tools (VirusTotal) for malware analysis, JSON log parsing (`jq`) for Suricata IDS alerts, and incident response reflections.

### 12. [Python Security Automation](./Activity_12_update_a_file_through_a_Python_algorithm)
*   **Description:** Developed a Python algorithm to automate the updating of network access controls. The script parses an IP allow list, compares it against a removal list, and overwrites the configuration file to revoke access.
