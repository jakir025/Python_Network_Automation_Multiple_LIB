import socket

# Print start banner
print('\n'+ '#'*50+'\n Started Executing Script from '+socket.gethostname()+ '\n'+ '#'*50)

def port_check(ip, port):
    print('~'*20)
    print('FQDN is  :'+socket.getfqdn(ip))

    try:
        print('IP is  :'+socket.gethostbyname(ip))
    except:
        print('Exception occured while getting IP ')
        pass

    try:
        DEVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_of_check = DEVICE_SOCKET.connect_ex((ip, port))

        if result_of_check == 0:
            print(str(ip)+'  is Listening on Port  '+ str(port))
            DEVICE_SOCKET.close()
        else:
            print(str(ip)+'  is not listening on Port  '+ str(port))
            DEVICE_SOCKET.close()

    except socket.gaierror:
        print('Could not resolve host : '+ ip)
        pass
    except:
        print('Exception occured')
        pass

# Execute port checks
port_check('192.168.184.140', 80)
port_check('qwe', 443)
port_check('192.168.184.141', 80)
port_check('192.168.0.10', 443)

# Print finish banner
print('\n'+ '#'*50+'\n Finished Executing Script'+ '\n'+ '#'*50)
