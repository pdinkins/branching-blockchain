# ipfs.py
# interact with the ipfs network 

import ipfsapi
from pprint import pprint
import requests
import writer
import network
import generate
import chain


ipfsid = ['Addresses', 'ID', 'AgentVersion', "ProtocolVersion", "PublicKey" ]


def initialize_ipfsapi():
    api = ipfsapi.connect('127.0.0.1', 5001)
    apiid = api.id()
    ipfs_addresses = apiid[ipfsid[0]]
    for i in range(1, len(ipfsid)):
        print(ipfsid[i],'\n' + apiid[ipfsid[i]])
        print()
    print(ipfsid[0])
    for i in range(0, len(ipfs_addresses)):
        print(ipfs_addresses[i])


def add_file(filename):
    api = ipfsapi.connect('127.0.0.1', 5001)
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
    data, nhash = network.ipfs_ledger_getter()
    #generate.initailize_new_genesis_chain(nhash)
    ledger = writer.Ledger(nhash)
    with open(ledger.filename, 'wb') as file:
        file.write(data)
    writer.ledger_parse(ledger.filename)
    print(chain.c_hash)
