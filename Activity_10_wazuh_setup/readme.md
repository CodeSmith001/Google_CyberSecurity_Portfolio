# Portfolio Activity: Wazuh SIEM Deployment and Log Ingestion

## 📝 Objective
The objective of this project was to build a fully functional Security Information and Event Management (SIEM) lab environment from the ground up using the open-source platform, Wazuh. This involved deploying the SIEM on a local virtual machine, troubleshooting host system incompatibilities, configuring a data ingestion pipeline, and successfully loading a sample dataset for analysis.

## 🛠️ Skills Demonstrated
- **SIEM Deployment:** Wazuh
- **Virtualization:** Oracle VirtualBox
- **Linux System Administration:** Command Line Interface (CLI), Permissions
- **Technical Troubleshooting:** Kernel Module Management (DKMS), Graphics Controller Configuration
- **Log Ingestion & Parsing:** Filebeat, YAML Configuration
- **Network & System Configuration**

## 🏢 Scenario: Building a Personal Security Lab
**Situation:** 
To gain practical, hands-on experience in threat detection and log analysis, I needed a robust SIEM environment. Commercial SIEMs have restrictive trial periods, so I chose the powerful, open-source platform Wazuh to build my own security analysis lab.

**Task:** 
My task was to deploy the official Wazuh OVA appliance in VirtualBox on my Zen Linux host machine. I needed to configure the virtual machine, ingest a provided `tutorialdata.zip` dataset, and verify that the logs were successfully parsed and searchable within the Wazuh dashboard.

## 🚀 Action Taken
I executed the project in four distinct phases: deployment, troubleshooting, data ingestion, and verification.

1.  **Initial Deployment:** I imported the Wazuh `.ova` file into VirtualBox and configured the virtual machine settings, critically assigning it **4096 MB (4 GB) of RAM** to ensure stable operation.

2.  **Host System Troubleshooting:** Upon first boot, I encountered a `VERR_SUPDRV_COMPONENT_NOT_FOUND` error. I identified this as a kernel module incompatibility between VirtualBox and my host system's **Zen kernel**. I resolved this by:
    *   Installing the specific kernel headers for my running kernel:
        `sudo pacman -S linux-zen-headers`
    *   Ensuring the DKMS host modules were installed to allow for on-the-fly driver compilation:
        `sudo pacman -S virtualbox-host-dkms`
    *   Rebuilding the kernel modules to align with my system:
        `sudo dkms autoinstall`

3.  **Data Ingestion:** With the VM running, I configured a VirtualBox Shared Folder to transfer the `tutorialdata` logs into the appliance. Inside the VM, I used `nano` to create a `ingest.yml` configuration file and then executed the **Filebeat** command to process the logs and send them to Wazuh:
    `/usr/share/filebeat/bin/filebeat -c ingest.yml -e`

4.  **Verification:** I navigated to the Wazuh dashboard in my web browser, went to the "Discover" tab, and set an absolute time range to include all historical data. The successful appearance of o


## 📁 Files Included
*   `[wazhu_setup.pdf]` - The formal vulnerability assessment and remediation strategy document.
