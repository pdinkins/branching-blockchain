'''
# IPFS
# interact with the ipfs network 
# 
# This module makes use of the py-ipfs-api to interact with
# an ipfs node. 


'''


import ipfsapi
import requests


class IpfsNode:
    '''
USE:
    # first initialize the connection
    ipfsnode = IpfsNode()

'''
    def __init__(self):
        # initial variables
        self.ipfslist = ['Addresses', 'ID', 'AgentVersion', "ProtocolVersion", "PublicKey" ]
        self.ipfsapi_ip = '127.0.0.1'
        self.ipfsapi_port = 5002

        # sub level variables
        self._api_connection = self.initialize_ipfsapi_connection()

    def initialize_ipfsapi_connection(self):
        # establish 
        self.api = ipfsapi.connect(self.ipfsapi_ip, self.ipfsapi_port)
        self.apiid = self.api.id()
        self.ipfs_addresses = self.apiid[self.ipfslist[0]]
        for i in range(1, len(self.ipfslist)):
            print(self.ipfslist[i],'\n' + self.apiid[self.ipfslist[i]] + '\n')
        print(self.ipfslist[0])
        for i in range(0, len(self.ipfs_addresses)):
            print(self.ipfs_addresses[i])
        
        # return the api connection instance 
        # adopted from the ipfsapi.connect class    
        return self.api
    
    def add_file(self, _file):
        self.file2add = self._api_connection.add(_file)
        self.__filehash = self.file2add["Hash"]
        print(self.__filehash)
        print(self._api_connection.cat(self.__filehash))

node = IpfsNode()

'''

def add_file(filename):
    api = ipfsapi.connect(ipfsapi_ip, ipfsapi_port)
    file2add = api.add(filename)
    filehash = file2add["Hash"]
    print(filehash)
    #print(api.cat(file2add['Hash']))
    req = requests.get('https://gateway.ipfs.io/ipfs/' + filehash)
    print(req.text)
    return filehash


def upload_g_chain():
    name = input('ledger>\t')
    ledger = writer.Ledger(name)
    add_file(ledger.filename)


def ipfs_ledger_deconstruct():
    data, nhash = ipfs_ledger_getter()
    #generate.initailize_new_genesis_chain(nhash)
    ledger = writer.Ledger(nhash)
    with open(ledger.filename, 'wb') as file:
        file.write(data)
    writer.ledger_parse(ledger.filename)
    print(chain.c_hash)


def ipfs_daemon_init():
    # opens new terminal shell and initailizes the IPFS daemon
    subprocess.Popen([sys.executable, 'ipfsdaemon.py'], shell=True)
    # pause to allow ipfs daemon to begin 
    time.sleep(3)
    # print ipfs data and daemon init confirmation
    initialize_ipfsapi()

def ipfs_ledger_getter():
    network_hash = input('Network hash>\t')
    ipfs_daemon_init()
    api = ipfsapi.connect(ipfsapi_ip, ipfsapi_port)
    req = requests.get('https://gateway.ipfs.io/ipfs/' + network_hash)
    network_ledger_data = req.text
    print(network_ledger_data)
    rawdata = api.cat(network_hash)
    return rawdata, network_hash

'''
