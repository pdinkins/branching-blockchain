import sys
from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP   = '192.168.1.17'
PORT_NUMBER = 12345
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.connect(('192.168.1.17', 12345))

dataa = input('data to send> ')

while True:
        mySocket.sendto(dataa.encode('utf8'),(SERVER_IP,PORT_NUMBER))
sys.exit()