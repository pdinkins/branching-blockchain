# ipfs.py
# interact with the ipfs network 

import ipfsapi
from pprint import pprint
import requests



ipfsid = ['Addresses', 'ID', 'AgentVersion', "ProtocolVersion", "PublicKey" ]
IPFS_API_CONFIG = ['127.0.0.1', 5002]

def initialize_ipfsapi():
    api = ipfsapi.connect(IPFS_API_CONFIG[0], IPFS_API_CONFIG[1])
    apiid = api.id()
    ipfs_addresses = apiid[ipfsid[0]]
    for i in range(1, len(ipfsid)):
        print(ipfsid[i],'\n' + apiid[ipfsid[i]] + '\n')
    print(ipfsid[0])
    for i in range(0, len(ipfs_addresses)):
        print(ipfs_addresses[i])


def add_file(filename):
    api = ipfsapi.connect('127.0.0.1', 5002)
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
    api = ipfsapi.connect('127.0.0.1', 5002)
    req = requests.get('https://gateway.ipfs.io/ipfs/' + network_hash)
    network_ledger_data = req.text
    print(network_ledger_data)
    rawdata = api.cat(network_hash)
    return rawdata, network_hash