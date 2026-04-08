# Portfolio Activity: Python Algorithm for File Updates

## 📝 Objective
The objective of this project was to automate the updating of network access controls using Python. The goal was to write an algorithm that securely parses a text file containing an IP allow list, compares it against a list of IP addresses that require removal, and automatically updates the file to revoke access.

## 🛠️ Skills Demonstrated
- **Python Programming**
- **File I/O Operations:** Opening, reading, and writing to text files using `with open()`.
- **Data Structure Manipulation:** Converting strings to lists (`.split()`) and lists back to strings (`.join()`).
- **Control Flow:** Utilizing `for` loops and conditional `if` statements to iterate through data.
- **Security Automation:** Applying the Principle of Least Privilege.

## 🏢 Scenario: Healthcare Access Control Automation
**Situation:** 
As a security professional at a healthcare organization, I am responsible for managing access to a restricted subnetwork containing Protected Health Information (PHI). When employees leave the company or change departments, their IP addresses must be promptly removed from the network's allow list to prevent unauthorized access.

**Task:** 
My task was to create a Python script capable of automating this process. The script needed to read a text file (`allow_list.txt`), identify any IP addresses that matched a provided `remove_list`, eliminate those IPs from the active structure, and permanently overwrite the original file with the updated security parameters.

## 🚀 Action Taken
To automate this access control measure, I developed the following algorithmic logic:
1. **File Ingestion:** Utilized the `with open()` statement in `"r"` (read) mode to securely open the allow list and read its contents into a string variable.
2. **Data Parsing:** Applied the `.split()` method to convert the continuous string of IP addresses into a Python list, enabling individual element evaluation.
3. **Iterative Evaluation:** Designed a `for` loop to iterate through the target `remove_list`. Inside the loop, an `if` statement evaluated whether the current target existed in the parsed allow list.
4. **Access Revocation:** If a match was found, the `.remove()` method was executed to delete the IP address from the active list.
5. **File Update:** Employed the `.join()` method to convert the sanitized list back into a string (separated by newline characters `\n`). Finally, the `with open()` statement was used in `"w"` (write) mode to overwrite the original text file with the newly secured allow list.

## 📈 Results
The resulting Python algorithm successfully automates the revocation of network access. By programmatically updating the allow list, the script reduces the risk of human error during offboarding processes, ensures strict adherence to the Principle of Least Privilege, and actively protects sensitive patient data (PHI) from unauthorized internal access.

## 📁 Files Included
*   `[Algorithm-for-file-updates-in-Python.pdf]` - Detailed walkthrough of the algorithm logic and methodology.
*   `[algorithm_for_file_updates.py]` - The raw Python code demonstrating the access control automation.
