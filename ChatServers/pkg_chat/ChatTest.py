import socket
import sys

host = '10.248.27.23'
# host = raw_input("Plz imput destination IP:")
# data = raw_input("Plz imput what you want to submit:")
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
except socket.gaierror as e:
    print("Address-related error connecting to server: %s" % e)
    sys.exit(1)
except socket.error as e:
    print("Connection error: %s" % e)
    sys.exit(1)

while 1:
    try:
        data = raw_input("I say: ")
        s.send(data)
        buf = s.recv(1024)
        if len(buf):
            print("he say: " + buf)
    except:
        print("Dialogue Over")
        s.close()
        sys.exit(0)