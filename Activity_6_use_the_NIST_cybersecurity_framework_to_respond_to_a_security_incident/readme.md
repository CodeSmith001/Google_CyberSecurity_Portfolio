# Portfolio Activity: NIST Cybersecurity Framework (CSF) Incident Analysis

## 📝 Objective
The objective of this activity was to analyze a network security incident using the **National Institute of Standards and Technology Cybersecurity Framework (NIST CSF)**. The goal was to document a Denial of Service (DoS) attack and map the organization's response and future mitigation strategies to the five core functions of the framework: Identify, Protect, Detect, Respond, and Recover.

## 🛠️ Skills Demonstrated
- Application of the NIST Cybersecurity Framework (CSF)
- Incident Response Planning and Documentation
- Network Security Controls (Firewall Rules, IDS/IPS)
- Threat Analysis (ICMP Flood / DoS Attacks)
- Post-Incident Review and Process Improvement

## 🏢 Scenario: ICMP Flood Attack on a Multimedia Company
**Situation:** 
As a cybersecurity analyst for a multimedia company, I was tasked with investigating a recent Denial of Service (DoS) attack. An attacker exploited an unconfigured firewall to launch an ICMP flood (ping flood), overwhelming the network and causing a total service outage that lasted for two hours. 

**Task:** 
My task was to analyze the security event and create a comprehensive incident report and improvement plan based on the NIST CSF to ensure a proactive, structured approach to the organization's future network security.

## 🚀 Action Taken
I structured my analysis and recommendations around the five pillars of the NIST CSF:
1. **Identify:** Audited network logs to confirm the attack vector—a flood of ICMP pings bypassing an unconfigured firewall, causing a two-hour disruption to all internal and external services.
2. **Protect:** Recommended and documented the implementation of rate-limiting firewall rules for ICMP packets and Source IP verification to block spoofed addresses.
3. **Detect:** Outlined the deployment of network monitoring software to baseline traffic and an IDS/IPS to identify and filter suspicious ICMP signatures.
4. **Respond:** Documented the containment strategy, which included blocking inbound ICMP traffic, prioritizing critical services, and executing a stakeholder communication plan.
5. **Recover:** Verified the restoration of essential services without data loss and highlighted the need to improve Mean Time to Respond (MTTR) for future incidents.

## 📈 Results
By applying the NIST CSF, I transformed a reactive incident response into a proactive security strategy. The resulting report not only documented the mitigation of the immediate DoS threat but also established long-term administrative and technical controls (like IDS/IPS and strict firewall configurations) to prevent similar attacks from succeeding in the future.

## 📁 Files Included
*   `[Incident-report-analysis.pdf]` - The formal incident analysis and mitigation plan mapped to the NIST CSF.


