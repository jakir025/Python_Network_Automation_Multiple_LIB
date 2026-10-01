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

print (CSR_MGR.get_config('running'))
CSR_MGR.close_session()
