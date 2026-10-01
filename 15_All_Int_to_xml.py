from ncclient import manager

FILTER = """
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface/>
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
    print(reply.data_xml)

    with open('Al_int_2.xml', 'w') as SAVE:
        SAVE.write(reply.data_xml)
