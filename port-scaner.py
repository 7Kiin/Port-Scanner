import socket

ip = input("Enter the IP direction to scan: ")

for port in range(1,65535):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print("Open port: " + str(port))
        sock.close()
    else:
        print("Closed port: " + str(port))
