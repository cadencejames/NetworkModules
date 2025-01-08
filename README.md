# **Cisco Network Interface Management Script**
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Netmiko](https://img.shields.io/badge/library-netmiko-blue)
![License](https://img.shields.io/github/license/cadencejames/NetworkModules)
![Last Commit](https://img.shields.io/github/last-commit/cadencejames/NetworkModules)
![Contributors](https://img.shields.io/github/contributors/cadencejames/NetworkModules)
[![Network Tool](https://img.shields.io/badge/network-tool-green)](https://github.com/cadencejames/NetworkModules)

This Python module provides various functions for managing and configuring Cisco devices through SSH. The module is designed to be extendable and can easily be imported into other scripts for specific network management tasks. Current functionalities include retrieving interface details, but additional features can be added in the future to cover other network configuration tasks.

---
## **Features**
- **Modular Design**: Designed as a network management module, allowing you to add new functions as needed.
- **SSH Connectivity**: Securely connects to Cisco devices via SSH using the `netmiko` library.
- **Retrieving Interface Information**: Fetches basic and detailed interface configurations.
- **Future Extensibility**: New network-related functions can be added easily, such as retrieving configurations, setting interfaces, managing VLANs, and more.

---
## **Current Functions**
1. **ShowInterfaces**  
   - Retrieves basic interface details using the `show ip interface brief` command.
   - Parses interface status, IP address, method, protocol, and description.
   
2. **ShowInterfaceDetails**  
   - Retrieves detailed configuration for a specific interface using `show run interface <interface>`.
   - Collects settings such as description, duplex, speed, and switchport configuration.

---
## **Future Functionality**
This script is intended to grow into a full network management toolkit. Future functionalities might include:
- **ConfigureInterfaces**: To configure interface settings (e.g., enable/disable, speed, duplex).
- **ManageVLANs**: Retrieve and configure VLAN information.
- **SaveConfigurations**: Save or backup Cisco device configurations.
- **RebootDevices**: Reboot Cisco devices remotely.

---
## **Requirements**
- **Python Version:** Python 3.6+
- **Libraries:**  
  - `netmiko`: For SSH connections. Install via pip: `pip install netmiko`
  - `getpass`: For securely entering passwords (Python standard library).
  
- **Input Files:**  
  - None (credentials and IP addresses are provided at runtime).
  
- **Output:**  
  - The script will print interface details to the console. Future updates may add the ability to output to different types of files.

---
## **Usage as a Module**
1. Clone the repository and navigate to the script directory.
2. Install the required dependencies if not already installed:
   ```bash
   pip install netmiko
   ```
3. Import the module into your own scripts. For example:
   ```
   from NetworkModules import ShowInterfaces, ShowInterfaceDetails
   device = {
     'device_type': 'cisco_ios',
     'host': '192.168.1.1',
     'username': 'your_username',
     'password': 'your_password'
   }
   ```

   # Fetch interfaces information
   ```
   interfaces = ShowInterfaces("192.168.1.1", device)
   for interface in interfaces:
       print(interface)
	```
   # Fetch detailed information for a specific interface
   ```
   interface_details = ShowInterfaceDetails("192.168.1.1", device, "FastEthernet0/1")
   for item in interface_details:
       for subitem in item:
           print(f"{subitem}: {item[subitem]}")
	```

4. You can also extend the module by adding new functions, such as configuring interfaces, managing VLANs, or saving configurations. Simply define a new function in the `NetworkModules.py` script and call it from your main script.

---
## **Error Handling**
- If there are any issues with the SSH connection or any of the modules, the script will print the error message and raise an exception.
- You can catch errors for troublshooting by wrapping the function calls in try-except blocks.
## **License**
This script is provided under the MIT License. See `License` for more details.
## **Contributing**
Feel free to fork this repository and submit pull requests if you'd like to improve the script, add new features, or fix bugs. Contributions are welcome!
