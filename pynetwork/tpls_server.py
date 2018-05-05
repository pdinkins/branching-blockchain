# server.py
import logging
logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s', )
logger = logging.getLogger(__name__)
import datetime as dt

local_ip = "192.168.1.5"
n_port = 1234

def catch_input(input_string):  
    dt.datetime.now(), autolog()
    return input_string[::-1]

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
    input_from_client = input_from_client_bytes.decode("utf8").rstrip()

    res = catch_input(input_from_client)
    #print("Result of processing {} is: {}".format(input_from_client, res))

    vysl = res.encode("utf8")  # encode the result string
    conn.sendall(vysl)  # send it to client
    conn.close()  # close connection
    dt.datetime.now(), autolog()
    print(dt.datetime.now(), 'Connection ' + ip + ':' + port + " ended")

def start_server():
    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    dt.datetime.now(), autolog()
    print(dt.datetime.now(), 'Socket created')

    try:
        soc.bind((local_ip, n_port))
        print(dt.datetime.now(), 'Socket bind complete')
    except socket.error as msg:
        import sys
        print(dt.datetime.now(), 'Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    #Start listening on socket
    soc.listen(10)
    print(dt.datetime.now(), 'Socket now listening')

    # for handling task in separate jobs we need threading
    from threading import Thread

    # this will make an infinite loop needed for 
    # not reseting server for every client
    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print(dt.datetime.now(), 'Accepting connection from ' + ip + ':' + port)
        print(conn)
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            print(dt.datetime.now(), "Terible error!")
            import traceback
            traceback.print_exc()
    
    soc.close()

def autolog():
    import inspect, logging
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logging.debug("%s in %s:%i" % (
        func.co_name, 
        func.co_filename, 
        func.co_firstlineno
    ))

start_server()  