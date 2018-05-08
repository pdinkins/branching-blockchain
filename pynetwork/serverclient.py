import socket

testips = ["192.168.0.9", "70.171.11.105"]
# tip = int(input('ip_id>\t'))
tip = 1
SERVER_IP = testips[tip]
SERVER_PORT = 1234

# establish socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
# connect to open socket server
soc.connect((SERVER_IP, SERVER_PORT))

import packet
p2s = packet.packet_genesis()


# raw data to send
clients_input = p2s
# send encoded data
soc.send(clients_input[0].encode("utf8")) # we must encode the string to bytes  
# received data
result_bytes = soc.recv(4096) # the number means how the response can be in bytes  
# decoded data
result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode

print("data for server> {}".format(result_string))   

if result_string == 'Connection success':
    rdi = str(input('>\t')).encode('utf-8')
    d2s = [clients_input[1], rdi]


    soc.send(d2s[1])
    reply = soc.recv(4096)
    print(reply.decode('utf-8'))

