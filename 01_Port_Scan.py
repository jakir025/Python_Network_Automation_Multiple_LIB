import socket

socket.setdefaulttimeout(.5)

destination = ('192.168.184.140', 22)
DEVICE_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#result_of_check = DEVICE_SOCKET.connect(destination)
result_of_check = DEVICE_SOCKET.connect_ex(destination)
print(result_of_check)

if result_of_check == 0:
    print("Listening on port")
    DEVICE_SOCKET.close()
else:
    print("Is not listening on port")
    DEVICE_SOCKET.close()
    
