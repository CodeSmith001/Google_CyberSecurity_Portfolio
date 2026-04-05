# Portfolio Activity: Linux File Permissions & System Hardening

## 📝 Objective
The objective of this project was to utilize the Linux Command Line Interface (CLI) to audit and update file and directory permissions. The goal was to secure a research team's project directory by identifying unauthorized access levels and applying the **Principle of Least Privilege** in compliance with organizational security policies.

## 🛠️ Skills Demonstrated
- Linux Command Line Interface (Bash)
- Access Control and Authentication
- System Hardening
- Managing File/Directory Permissions (`chmod`, `ls -la`)
- Translating Security Policies into Technical Controls

## 🏢 Scenario: Securing the Research Directory
**Situation:** 
As a security professional, I was tasked with auditing a shared Linux environment used by a research team. I discovered that several files and directories within the `projects` folder had overly permissive settings, potentially allowing unauthorized users to read, modify, or execute sensitive project files.

**Task:** 
My task was to examine current permissions, identify gaps against the company's security policies, and use Linux commands to restrict access to hidden files, standard project files, and restricted directories.

## 🚀 Action Taken
To secure the file system, I executed the following steps via the Linux CLI:
1. **Auditing:** Ran `ls -la` to display all directory contents, including hidden files, and analyzed the 10-character permission strings (e.g., `drwxrwxrwx`) to determine current user, group, and other access levels.
2. **Restricting Global Access:** Identified a file (`project_k.txt`) with global write access. I used `chmod o=r project_k.txt` to revoke write privileges from "others," setting it to read-only.
3. **Securing Archived Data:** Identified a hidden archived file (`.project_x.txt`) that needed to be locked down. I used `chmod u=r,g=r .project_x.txt` to explicitly set the user and group permissions to read-only, preventing accidental modification.
4. **Directory Hardening:** Discovered that the `drafts/` directory was accessible to the entire group. To restrict access solely to the file owner, I executed `chmod g= drafts/`, stripping all read, write, and execute permissions from the group.
5. **Verification:** Executed a final `ls -la` command to verify that all newly applied permissions successfully aligned with the requested security policies.

## 📈 Results
The project directory is now properly hardened. By systematically utilizing the `chmod` command, I successfully eliminated unauthorized access vectors and ensured that sensitive research files and directories strictly adhere to the principle of least privilege. 

## 📁 Files Included
*   `[Linux_Permissions_Report.pdf]` - Detailed report containing CLI commands, annotated screenshots, and explanations of permission string modifications.
