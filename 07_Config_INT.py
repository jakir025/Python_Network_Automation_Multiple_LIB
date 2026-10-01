from ncclient import manager

CONFIG = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <GigabitEthernet>
        <name>2</name>
        <ip>
          <address>
            <primary>
              <address>22.22.22.22</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </GigabitEthernet>
    </interface>
  </native>
</config>
"""

# Filter to verify the change afterward
FILTER = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
    <GigabitEthernet>
      <name>2</name>
    </GigabitEthernet>
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

    reply = CSR_MGR.edit_config(target='running', config=CONFIG)
    print("=== edit-config reply ===")
    print(reply.xml)

    verify = CSR_MGR.get_config(source='running', filter=('subtree', FILTER))
    print("\n=== Verification ===")
    print(verify.data_xml)
