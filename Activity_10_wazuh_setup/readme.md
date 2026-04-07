# Portfolio Activity: Wazuh SIEM Deployment and Advanced Log Ingestion

## 📝 Objective
The objective of this project was to deploy a local Security Information and Event Management (SIEM) environment using Wazuh. This project demonstrated full-stack technical competency, including virtualization management, network-based file transfer, Linux system administration, and the resolution of complex software-kernel conflicts.

## 🛠️ Skills Demonstrated
- **SIEM Platform:** Wazuh (OpenSearch-based)
- **Virtualization:** VMware Workstation
- **Network Services:** Python HTTP Server, SSH, `wget`
- **Linux Security:** Troubleshooting Seccomp (Secure Computing Mode)
- **Data Engineering:** Filebeat, YAML Configuration, Index Pattern Management
- **Troubleshooting:** Identifying and bypassing kernel-level syscall conflicts

## 🏢 Scenario: SIEM Infrastructure Engineering
**Situation:** 
To practice high-volume log analysis, I needed to ingest a dataset of over 100,000 logs into a Wazuh SIEM. The standard ingestion methods faced hypervisor-level constraints and security policy conflicts within the virtualized environment.

**Task:** 
My task was to deploy the Wazuh OVA on VMware, securely transfer 100k+ logs from the host to the guest VM using a Python-based web server, and configure a Filebeat pipeline that could bypass security-call (seccomp) crashes common on custom Linux kernels.

## 🚀 Action Taken
1. **Infrastructure Setup:** Imported the Wazuh appliance into VMware and configured network connectivity. I used `ssh` to manage the VM remotely for better workflow efficiency.
2. **Network Data Transfer:** Rather than using traditional shared folders, I hosted a **Python HTTP server** on my host machine and utilized `wget` on the VM to pull the `tdata.zip` file across the local network.
3. **Pipeline Configuration & Troubleshooting:** I authored a custom `ingest.yml` for Filebeat. Critically, I diagnosed a `SIGABRT` crash caused by a conflict between the Go-based Filebeat runtime and the host's Zen Linux kernel. I resolved this by explicitly disabling **seccomp** (`seccomp.enabled: false`) in the configuration.
4. **Data Management:** I manually created the `filebeat-*` index pattern within the Wazuh Management dashboard to map the raw Elasticsearch data to the OpenSearch-based UI.

## 📈 Results
The project resulted in the successful ingestion and indexing of **109,867 security logs**. By resolving hardware-level virtualization errors and kernel-level software crashes, I demonstrated the ability to maintain and troubleshoot enterprise-grade security tools under realistic technical constraints.

## 📁 Files Included
*   '[wazuh-setup.pdf]' - Formal technical report containing the full command history and success screenshots.

*(Note: This activity was completed as part of the Google Cybersecurity Professional Certificate).*
