# network.py 
# contains network related functions

import subprocess
import sys
import time
import ipfs
import requests
import ipfsapi

def ipfs_daemon_init():
    # opens new terminal shell and initailizes the IPFS daemon
    subprocess.Popen([sys.executable, 'ipfsdaemon.py'], creationflags = subprocess.CREATE_NEW_CONSOLE)
    # pause to allow ipfs daemon to begin 
    time.sleep(3)
    # print ipfs data and daemon init confirmation
    ipfs.initialize_ipfsapi()

def ipfs_ledger_getter():
    network_hash = input('Network hash>\t')
    ipfs_daemon_init()
    api = ipfsapi.connect('127.0.0.1', 5001)
    req = requests.get('https://gateway.ipfs.io/ipfs/' + network_hash)
    network_ledger_data = req.text
    print(network_ledger_data)
    rawdata = api.cat(network_hash)
    return rawdata, network_hash