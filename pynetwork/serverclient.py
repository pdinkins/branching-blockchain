# client.py

import socket

# establish socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# connect to open socket server
soc.connect(("70.171.11.105", 1234))
# raw data to send
clients_input = input("input> \n")  
# send encoded data
soc.send(clients_input.encode("utf8")) # we must encode the string to bytes  
# received data
result_bytes = soc.recv(4096) # the number means how the response can be in bytes  
# decoded data
result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode

print("data for server> {}".format(result_string))  