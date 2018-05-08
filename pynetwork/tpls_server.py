# server.py
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s', )
import datetime as dt

local_ip = "192.168.1.5"
n_port = 1234
trusted_wallet_hash = '56b8ba882b6aeeb7fa43f9125d8d2909b8a734f82b46b67b3809105a28cfb05d'
handshake = []

def catch_input(input_string):  
    handshake.clear()
    autolog()
    packet = input_string
    if packet == trusted_wallet_hash:
        cs = 'CONNECTION SUCCESSFUL'
        handshake.append(1)
    else:
        handshake.append(0)
        cs = 'ERROR: CONNECTION UNSUCCESSFUL'
    print(dt.datetime.now(), cs)
    print(dt.datetime.now(), packet)
    return cs

def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 4096):
    # the input is in bytes, so decode it
    input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)

    # MAX_BUFFER_SIZE is how big the message can be
    # this is test if it's sufficiently big
    import sys
    siz = sys.getsizeof(input_from_client_bytes)
    if  siz >= MAX_BUFFER_SIZE:
        print("The length of input is probably too long: {}".format(siz))
    # decode input and strip the end of line
    input_from_client = input_from_client_bytes.decode("utf8")
    print(dt.datetime.now(), 'CLIENT HANDSHAKE HASH: ', input_from_client)
    res = catch_input(input_from_client)
    #print("Result of processing {} is: {}".format(input_from_client, res))

    vysl = res.encode("utf8")  # encode the result string
    conn.sendall(vysl)  # send it to client
    if handshake[0] == 1:
        print(dt.datetime.now(), 'HANDSHAKE SUCCESS')
        data_bytes = conn.recv(MAX_BUFFER_SIZE)
        siz = sys.getsizeof(input_from_client_bytes)
        if  siz >= MAX_BUFFER_SIZE:
            print("The length of input is probably too long: {}".format(siz))
        
        data = data_bytes.decode('utf-8')
        print(dt.datetime.now(), data)
        replyb = 'DATA TRANSFER COMPLETE'
        conn.sendall(replyb.encode('utf-8'))
       
    else:
        conn.close()  # close connection
    
    autolog()
    print(dt.datetime.now(), 'CONNECTION ' + ip + ':' + port + " TERMINATED")

def start_server():
    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    autolog()
    print(dt.datetime.now(), 'SOCKET CREATED')

    try:
        soc.bind((local_ip, n_port))
        print(dt.datetime.now(), 'SOCKET BIND COMPLETE')
    except socket.error as msg:
        import sys
        print(dt.datetime.now(), 'BIND_FAIL_ERROR: ' + str(sys.exc_info()))
        sys.exit()

    #Start listening on socket
    soc.listen(10)
    print(dt.datetime.now(), 'SOCKET LISTENING')
    autolog()
    # for handling task in separate jobs we need threading
    from threading import Thread

    # this will make an infinite loop needed for 
    # not reseting server for every client
    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print(dt.datetime.now(), 'ACCEPTING CONNECTIONS FROM ' + ip + ':' + port)
        autolog()
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            print(dt.datetime.now(), "Terible error!")
            import traceback
            autolog()
            traceback.print_exc()
    
    soc.close()

def autolog():
    import inspect, logging
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logging.debug("{} {} in {}:{}".format(
        dt.datetime.now(),
        func.co_name, 
        func.co_filename, 
        func.co_firstlineno
    ))

start_server()  