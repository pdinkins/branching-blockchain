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
hs_key = 'orion'


# dumps data from 
def dynamic_data_dump():
    trusted_hashes.clear()
    handshake.clear()

import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
def log(message):
    logging.debug("{}\t{}".format(
            datetime.datetime.now(),
            message))

#### IMPORT ####
try:
    import logging
    import datetime
    import sys
    import socketserver
    import socket
    import inspect
    from threading import Thread
    import writer
    import ipfsapi
    import setup
    log('INITIAL_IMPORT_SUCCESSFUL')
except:
    log('INITIAL_IMPORT_ERROR')
    print(sys.exc_info())
    sys.exit()

#### SETUP ####

node_0 = setup.UserBuild()
node_0



#### SERVER ####

def open_connection():
    # open socket to accept connection
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    log('0_NODE_connection_socket')
    
    # bind socket to local network 
    # 
    # 0 and forward port
    try:
        _socket.bind(('192.168.1.4', 1234)) # add dynamic naming
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
        log('_INCOMING_CLIENT_HASH___\t' + chash_r)
        #send chash to be analyzed
        hs = chash_analyzer(chash_r)
        hsb = hs.encode('utf-8')
        conn.sendall(hsb)

        if hs == 0:
            log('REFUSE INCOMING CONNECTION')
            response = 'Connection refused'
            conn.sendall(response.encode('utf-8'))
            conn.close()

        elif hs == hs_key:
            log('INCOMING CONNECTION ACCEPTED')
            fidb = conn.recv(MAX_BUFFER_SIZE)
            # check size TODO: make this a seperate function for easy reuse 
            fidb_size = sys.getsizeof(fidb)
            if fidb_size >= MAX_BUFFER_SIZE:
                log('ERROR_fidb > maxbuffersize')
                log('TERMINATING_THREAD')
                # pipe to end thread
                conn.close()
            # decode the incoming function id data
            fid_data = fidb.decode('utf-8')
            log(fid_data)
            # TODO pipe to fid analyer
            node_res = fid_analyze(fid_data)
            
            # reponse
            reply_bytes = node_res.encode('utf-8')
            conn.sendall(reply_bytes)

            arnold = 'CONNECTION ' + ip + ':' + port + " TERMINATED"
            log(arnold)
            # restart the process
            open_connection()

def fid_analyze(fid_d):
    while fid_d == 'orion':
        log(fid_d)
        response = 'fid analyzed the fid and this is the fcking'
        
        return response


def chash_analyzer(incoming_chash):
    # check if incoming client hash is a trusted hash
    # create file abject TODO: make this object in the setup script 
    thfile = writer.Ledger('trustedhashes')
    # parse trusted hash file and append trusted hashes to dynamic list
    writer.ledger_parse(thfile.filename)
    log('BEGIN HASH CHECK')
    for i in range(0, len(trusted_hashes)):
        if incoming_chash != trusted_hashes[i]:
            log('CHASH CHECK FAIL')
            handshake.clear()
            handshake.append(0)
            return 'fail'
        elif incoming_chash == trusted_hashes[i]:
            log('CHASH CHECK PASS')
            # hs_key is setup function contained in the setup script 
            handshake.clear()
            handshake.append(hs_key)
            return hs_key
        else:
            log('CHASH CHECK COMPLETELY FAILED')
            handshake.clear()
            handshake.append(0)
            return 'fail'


open_connection()