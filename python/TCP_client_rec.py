import socket
# PC is client, Cobot is server
# TCP_IP = '192.168.43.42'
TCP_IP = '192.168.0.4'
# TCP_PORT = 49532 
TCP_PORT = 10001
BUFFER_SIZE = 1024
MESSAGE = b"Hello, World!"

while(1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    temp = input("Enter: ")
    MESSAGE = bytes(temp, "ascii", "replace")

    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print("Received data:", data)