from ncclient import manager
import xml.etree.ElementTree as ET

FILTER = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
    <GigabitEthernet/>
  </interface>
</native>
"""

with manager.connect(
    host='192.168.184.140',
    port=830,
    username='jakir',
    password='Hoss1234',
    hostkey_verify=False,
    look_for_keys=False,
    allow_agent=False,
    device_params={'name': 'csr'}
) as CSR_MGR:
    reply = CSR_MGR.get_config(source='running', filter=('subtree', FILTER))

root = ET.fromstring(reply.data_xml)

# Define the XML namespace dictionary
ns = {'ios': 'http://cisco.com/ns/yang/Cisco-IOS-XE-native'}

# Find all GigabitEthernet interfaces safely using XPath
interfaces = root.findall('.//ios:interface/ios:GigabitEthernet', ns)

if not interfaces:
    print("No GigabitEthernet interfaces found.")
    exit()

print(f"Found {len(interfaces)} GigabitEthernet interfaces.")
n = int(input(f"Enter Interface Number (1 to {len(interfaces)}): "))
target_index = n - 1

if 0 <= target_index < len(interfaces):
    target_int = interfaces[target_index]

    # Safely extract the Name/Number
    name_elem = target_int.find('ios:name', ns)
    int_number = name_elem.text if name_elem is not None else "Unknown"

    # Safely navigate to the IP address element
    ip_elem = target_int.find('.//ios:ip/ios:address/ios:primary/ios:address', ns)
    int_ip = ip_elem.text if ip_elem is not None else "No IP Assigned"

    print(f"GigabitEthernet {int_number} - IP Address: {int_ip}")
else:
    print("Invalid selection.")
