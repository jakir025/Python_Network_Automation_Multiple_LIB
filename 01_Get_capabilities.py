from ncclient import manager

CSR_MGR = manager.connect(
    host='192.168.184.140',
    port=830,
    username='jakir',
    password='Hoss1234',
    hostkey_verify=False,
    look_for_keys=False,
    allow_agent=False,
    device_params={'name': 'csr'}
)
for RTR_Capabilities in CSR_MGR.server_capabilities:
    print(RTR_Capabilities)

CSR_MGR.close_session()
