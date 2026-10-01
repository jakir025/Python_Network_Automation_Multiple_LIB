from ncclient import manager

CONFIG = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>NEW-CSR</hostname>
  </native>
</config>
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
)as CSR_MGR:
    reply = CSR_MGR.edit_config(target='running', config=CONFIG)
    print(reply.xml)
