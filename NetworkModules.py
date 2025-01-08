from netmiko import ConnectHandler
from getpass import getpass

def ShowInterfaces(ip, device):
  import re
  interface_list = []
  try:
    # Set the target device's IP for the connection
    device['host'] = ip
    # Establish SSH Connection using netmiko
    connection = ConnectHandler(**device)
    # Send the 'show ip interface brief' command to get interface summaries
    interfaces_output = connection.send_command("show ip interface brief")
    # Send the 'show interface description' command to get interface descriptions
    descriptions_output = connection.send_command("show interface description")
    # Close the SSH connection after retrieving data
    connection.disconnect()
    # Split the output of both commands into lines for easier processing
    interfaces_lines = interfaces_output.splitlines()
    descriptions_lines = descriptions_output.splitlines()
    # Define regex patterns to parse the output
    interfaces_pattern = r"(.+?)\s+(.+?)\s+(\S+)\s+(\S+)\s+(.+?)\s+(\S+)"
    descriptions_pattern = r"(.+?)\s+(.+?)\s+(.+?)\s+(.+)"
    # Process the lines, skipping the headers and matching interface details
    for intfc_line, desc_line in zip(interfaces_lines[1:], descriptions_lines[1:]):
      interface = {
        'interface': '',
        'ip': ip,
        'ok': '',
        'method': '',
        'status': '',
        'protocol': '',
        'description': ''
      }
      # Match the lines using regex patterns
      intfc_match = re.match(interfaces_pattern, intfc_line)
      desc_match = re.match(descriptions_pattern, desc_line)
      if intfc_match and desc_match:
        # Extract details from regex match groups and update interface dictionary
        interface = {
          "interface": intfc_match.group(1).strip(),
          "ip": intfc_match.group(2).strip(),
          "ok": intfc_match.group(3).strip(),
          "method": intfc_match.group(4).strip(),
          "status": intfc_match.group(5).strip(),
          "protocol": intfc_match.group(6).strip(),
          "description": desc_match.group(4).strip(),
        }
        # Append the interface details to the list
        interface_list.append(interface.copy())
    return interface_list  # Return the list of interface details
  except Exception as e:
    # Handle any exceptions and print the error message
    print(f"Error getting interfaces info: {e}")
    raise # Raise the exception again for further handling

def ShowInterfaceDetails(ip, device, intfc):
  interface_details = []
  # Initialize the interface dictionary with default values
  interface = {
    'ip': ip,
    'interface': intfc,
    'description': 'Not Set',
    'duplex': 'Default',
    'speed': 'Default',
    'switchport': 'Not Set'
  }
  try:
    # Set the target device's IP for the connection
    device['host'] = ip
    # Establish SSH connection using netmiko
    connection = ConnectHandler(**device)
    # Send the 'show run interface <interface>' command to get detailed config
    interface_output = connection.send_command(f"show run interface {intfc}")
    # Close the SSH connection after retrieving data
    connection.disconnect()
    # Split the output into lines for easier parsing
    interface_lines = interface_output.splitlines()
    # Process each line of the interface configuration
    for intfc_line in interface_lines:
      # Parse the description line if it exists
      if "description" in intfc_line:
        desc = intfc_line.split()[1:] # Extract the description part
        interface['description'] = ' '.join(desc) # Join the parts and update
      # Parse duplex settings if present
      if "duplex" in intfc_line:
        duplex = intfc_line.split()[1:] # Extract duplex value
        interface['duplex'] = ' '.join(duplex) # Update duplex value
      # Prase speed settings if present
      if "speed" in intfc_line:
        speed = intfc_line.split()[1:] # Extract speed value
        interface['speed'] = ' '.join(speed) # Update speed value
      # Parse switchport settings if present
      if "switchport mode" in intfc_line:
        mode = intfc_line.split()[-1] # Extract the mode (access or trunk)
        interface['switchport'] = f"Mode: {mode}" + interface['switchport'] # Update switchport
      elif "switchport access vlan" in intfc_line:
        vlan = intfc_line.split()[-1] # Extract the access VLAN
        interface['switchport'] += f", Access VLAN: {vlan}" # Append access VLAN to switchport
      elif "switchport voice vlan" in intfc_line:
        vlan = intfc_line.split()[-1] # Extract the voice VLAN
        interface['switchport'] += f", Voice VLAN: {vlan}" # Append voice VLAN to switchport
      elif "switchport trunk allowed vlan" in intfc_line:
        vlans = " ".join(intfc_line.split()[4:]) # Extract trunk allowed VLANs
        interface['switchport'] += f", Trunk Allowed VLANs: {vlans}" # Append trunk VLANs
      else:
        continue # Skip lines that don't match switchport configurations
    # If switchport was modified, remove the default "Not Set" string
    if interface['switchport'] != "Not Set":
      interface['switchport'] = interface['switchport'].replace("Not Set", "")
    # Append the interface details to the list
    interface_details.append(interface.copy())
    return interface_details # Return the interface details
  except Exception as e:
    # Handle any exceptions and print the error message
    print(f'Error getting detailed interface info: {e}')
    raise # Raise the exception again for further handling

# Main program entry point
if __name__ == "__main__":
  # Prompt user for username and password
  username = input("Username: ")
  password = getpass("Password: ")
  # Define device connection details
  device = {
    'device_type': 'cisco_ios', # Cisco IOS device type
    'host': '0.0.0.0', # Placeholder for IP address, to be set later
    'username': username,
    'password': password
  }
  try:
    ip = "192.168.1.1" # IP address of the device
    # interfaces = ShowInterfaces(ip, device) # Optionally fetch basic interface info
    # for interface in interfaces:
      # print(interface) # Optionally print interfaces info
    # Fetch detailed intformation for a specific interface (example: FastEthernet0/1
    interfaceDetails = ShowInterfaceDetails(ip, device, "FastEthernet0/1")
    for item in interfaceDetails:
      for subitem in item:
        print(f"{subitem}: {item[subitem]}")
    # print(interfaceDetails) # Optionally print the details dictionary
  except Exception as e:
    # Handle any exceptions that occur in the main block
    print(f"Error in main: {e}")
