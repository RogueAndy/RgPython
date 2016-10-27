import socket
import traceback
import sys

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

ClientSock, ClientAddr = s.accept()
while 1:
    try:
        buf = ClientSock.recv(1024)
        if len(buf):
            print("he say: " + buf)
        data = raw_input("I say: ")
        ClientSock.sendall(data)
    except:
        print("Dialogue Over")
        ClientSock.close()
        sys.exit(0)