###### 0_NODE_SERVER ######
'''
This is a level 0 node server. This node contains the entire software
stack and can execute every network function. Gate keeper for private
networks. Facilitates custom user functions. 

IPFS Daemon must be running 
IPFSAPI_IP: 127.0.0.1:5001/5002

Config file is required
    > network config
    > ipfs id
    > node wallet
        > trusted peers
        > data store hashes
'''


#### DYNAMIC DATA ####
trusted_hashes = []
handshake = []

# dumps data from 
def dynamic_data_dump():
    trusted_hashes.clear()
    handshake.clear()



#### IMPORT ####
try:
    import logging
    import datetime
    import sys
    import socketserver
    import socket
    import inspect
    from threading import Thread
    
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    def log(message):
        function = inspect.currentframe().f_back.f_code
        logging.debug("{}\t{}\t{}".format(
            datetime.datetime.now(),
            function.co_filename,
            message))
    
    log('INITIAL_IMPORT_SUCCESSFUL')
except:
    log('INITIAL_IMPORT_ERROR')
    print(sys.exc_info())
    sys.exit()



#### SERVER ####

def open_connection():
    # open socket to accept connection
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    log('0_NODE_connection_socket')
    
    # bind socket to local network IP and forward port
    try:
        _socket.bind(('192.168.1.5', 1234)) # add dynamic naming
        log('0_NODE_socket_bind')
    except socket.error as message:
        log(message)
        print(sys.exc_info())
        sys.exit()

    # listen for incoming connection
    _socket.listen(10)
    log('0_NODE_socket_listening')

    # incoming connection 
    conn, addr = _socket.accept()
    ip, port = str(addr[0]), str(addr[1])
    d = '0_Handshake' + ip + ':' + port
    log(d)

    # pass connection to thread for incoming packet analysis
    try:
        Thread(target=client_thread, args=(conn, ip, port)).start()
    except:
        import traceback
        log('ERROR_THREADING')
        traceback.print_exc()
    
    # close the socket
    _socket.close()


def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 4096):
    # incoming packet data
    incoming_chash = conn.recv(MAX_BUFFER_SIZE)
    log('CAPTURE__C_HASH')
    
    # check size of incoming chash
    chash_size = sys.getsizeof(incoming_chash)
    if chash_size >= MAX_BUFFER_SIZE:
        log('ERROR_chash_2_large')
        log('TERMINATING_THREAD')
        # pipe to end thread
        conn.close()

    else:
        # decode the incoming data
        chash_r = incoming_chash.decode('utf-8')
        log(chash_r)

        #send chash to be analyzed



def chash_analyzer(incoming_chash):
    # check if incoming client hash is a trusted hash
    # parse trusted hash file
    # append trusted hashes to dynamic list
    pass
    



open_connection()