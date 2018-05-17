import socket

while True:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(('192.168.1.4', 12345))

    client_input = input('input: ')
    if client_input != 'quit':
        soc.send(client_input.encode('utf8'))
        result_b = soc.recv(4096)
        result_s = result_b.decode('utf8')
        print(result_s)
    else:
        break
