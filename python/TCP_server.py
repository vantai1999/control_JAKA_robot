import socket
# PC is server, Cobot is client
TCP_IP = "192.168.0.3"
TCP_PORT = 555
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)

while (1):
    data = conn.recv(BUFFER_SIZE)
    if data:
        print("Received data:", data)
    
    temp = input("Enter: ")
    '''
    <pos_pick><...>
    <pos_pick><[-300, -49.9999, 482.315, -180, 5.25451e-06, 90]>    #Obj_1
    <pos_pick><[-300, 100, 482.315, -180, 7.99944e-06, 90]>         #Obj_2
    <pos_pick><[-300, 250, 482.315, -180, 8.19733e-06, 90]>         #Obj_3

    <pos_place><[...]>
    <pos_place><[215.010, 400.000, 482.315, 180, 0, 0]>         #Place_1
    <pos_place><[115.010, 400.000, 482.315, 180, 0, 0]>         #Place_2
    <pos_place><[15.000, 400.000, 482.315, 180, 0, 0]>          #Place_3
    '''
    MESSAGE = bytes(temp, "ascii", "replace")
    conn.send(MESSAGE)
    
conn.close()