# **Cisco Network Interface Management Script**
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Netmiko](https://img.shields.io/badge/library-netmiko-blue)
![License](https://img.shields.io/github/license/cadencejames/NetworkModules)
![Last Commit](https://img.shields.io/github/last-commit/cadencejames/NetworkModules)
![Contributors](https://img.shields.io/github/contributors/cadencejames/NetworkModules)
[![Network Tool](https://img.shields.io/badge/network-tool-green)](https://github.com/cadencejames/NetworkModules)

This Python script connects to Cisco devices via SSH, retrieves detailed information about network interfaces, and outputs this data for further analysis. The script supports extracting interface status, IP configuration, description, duplex, speed, and switchport settings.

---

## **Features**
- Connects to Cisco devices using SSH with user-provided credentials.
- Retrieves summary interface information (`show ip interface brief`).
- Fetches detailed interface configurations (`show run interface <interface>`).
- Displays detailed information, including interface status, IP, description, duplex, speed, and switchport configurations.
- Easily configurable for different IPs, interfaces, and device types.

---

## **Workflow**
1. **Establish SSH Connection**  
   - The script connects securely to the Cisco device using SSH, based on provided credentials.
   
2. **Retrieve Interface Summary**  
   - The script executes the command `show ip interface brief` to gather basic interface details, such as IP addresses, interface status, and protocol status.
   
3. **Retrieve Interface Details**  
   - The script fetches detailed interface configuration using `show run interface <interface>`. It parses and extracts:
     - Interface description.
     - Duplex settings.
     - Speed settings.
     - Switchport configurations, such as mode, VLANs, and trunk settings.
   
4. **Display Output**  
   - The script prints the gathered interface details for each specified interface.

---

## **Requirements**
- **Python Version:** Python 3.6+
- **Libraries:**  
  - `netmiko`: For SSH connections. Install via pip: `pip install netmiko`
  - `getpass`: For securely entering passwords (Python standard library).
  
- **Input Files:**  
  - None (credentials and IP addresses are provided at runtime).
  
- **Output:**  
  - The script will print interface details to the console.

---

## **Usage**
1. Clone the repository and navigate to the script directory.
2. Install the required dependencies if not already installed:
   ```bash
   pip install netmiko
    ```
3. Run the script:
   ```bash
   python NetworkModules.py
   ```
4. Enter the SSH username and password when prompted.
5. The script will retrieve and display the interface details for the specific device and interface (e.g. `FastEthernet0/1`).

## **Example Output**
After running the script for a specific interface (e.g. `FastEthernet0/1`), you might see output like this:
```yaml
ip: 192.168.1.1
interface: FastEthernet0/1
description: Uplink to Core Switch
duplex: full
speed: 1000
switchport: Mode: access, Access VLAN: 10
```
## **Error Handling**
- If there are any issues with the SSH connection or fetching interface details, the script will print the error message and raise an exception.
- You can catch errors for troublshooting by wrapping the function calls in try-except blocks.
## **License**
This script is provided under the MIT License. See `License` for more details.
## **Contributing**
Feel free to fork this repository and submit pull requests if you'd like to improve the script, add new features, or fix bugs. Contributions are welcome!
