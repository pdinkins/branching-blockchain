import socket

SERVER_IP = "70.171.11.105"
SERVER_PORT = 1234

# establish socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# connect to open socket server
soc.connect((SERVER_IP, SERVER_PORT))

import packet
p2s = packet.packet_genesis()


# raw data to send
clients_input = p2s[0]
# send encoded data
soc.send(clients_input.encode("utf8")) # we must encode the string to bytes  
# received data
result_bytes = soc.recv(4096) # the number means how the response can be in bytes  
# decoded data
result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode

<<<<<<< HEAD
print("data for server> {}".format(result_string))   

if result_string == 'Connection success':
    soc.send(clients_input[1].encode('utf-8'))
=======
print("data for server> {}".format(result_string))     
>>>>>>> 9c5cdb23fece3c836842e32ca8efbf37a0e1bf3d
