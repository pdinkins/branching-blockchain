#!/usr/bin/env python

# for testing the current local build


# initial import
try:
    import os, sys
    import platform
    from classes import User, Idea
    import ipfs
    import subprocess
    import time
    #import bloacks, bloacks, chain, client
    #import generate, menu, writer, ledger

except:
    print('FATALBUILDERROR')
    error = sys.exc_info()
    print(error)
    print(sys.exc_info()[0])
    raise

# os definitions
os_name = os.name
os_platform = platform.system() + platform.release()
os_id = os_name + os_platform
print(os_id)

def start():
    if os.name == 'Windows':
        os.system("python -i test.py")
    elif os.name == 'Darwin':
        os.system("py -i test.py")
    elif os.name == "Linux":
        os.system("py -i test.py")

# instantiation of User class
name = input('name>\t')
pin = input('pin>\t')
testuser = User(name, pin)
testuser.u_os_plt = os_name + os_platform
print(testuser.fullname)
print(testuser.u_os_plt)


subprocess.Popen([sys.executable, 'ipfsdaemon.py'], creationflags = subprocess.CREATE_NEW_CONSOLE)
time.sleep(3)
ipfs.initialize_ipfsapi()