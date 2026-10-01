from ncclient import manager
from lxml import etree

SAVE_RPC = '<save-config xmlns="http://cisco.com/yang/cisco-ia"/>'

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
    rpc_doc = etree.fromstring(SAVE_RPC)
    reply = CSR_MGR.dispatch(rpc_doc)
    print(reply.xml)
