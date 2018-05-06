import sys
from socket import socket, AF_INET, SOCK_STREAM

SERVER_IP   = '70.171.11.105'
PORT_NUMBER = 1234
SIZE = 4096
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

dataa = input('data to send> ')

while True:
        mySocket = socket( AF_INET, SOCK_STREAM )
        mySocket.connect((SERVER_IP, PORT_NUMBER))
        mySocket.send(dataa.encode('utf8'))
        d = mySocket.recv(SIZE)
        dd = d.decode('utf8')
        print(dd)

sys.exit()
