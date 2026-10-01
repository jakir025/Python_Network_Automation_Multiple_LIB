import socket

socket.setdefaulttimeout(.5)

print('\n'+ '#'*50+'\n Started Executing Script\n'+'#'*50)
def port_check(ip,port):

    DEVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result_of_check = DEVICE_SOCKET.connect_ex((ip,port))

    if result_of_check == 0:
        print(str(ip)+ ' Is Listening on Port' + str(port))
        DEVICE_SOCKET.close()
    else:
        print(str(ip)+ ' Is Not Listening on Port' + str(port))
        DEVICE_SOCKET.close()

port_check('192.168.184.140',80)
port_check('192.168.184.140',443)
port_check('192.168.184.142',80)
port_check('192.168.184.142',801)

print('\n'+ '#'*50+'\n Finished Executing Script\n'+'#'*50)
