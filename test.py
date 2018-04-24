#!/usr/bin/env python

# for testing the current cpu build

'''
import os
def start():
    if os.name == 'Windows':
        os.system("python -i test.py")
    elif os.name == 'Darwin':
        os.system("py -i test.py")
    elif os.name == "Linux":
        os.system("py -i test.py")
start()
#'''

# initial import
try:
    import os, sys
    import platform
    from classes import User, Idea
except:
    print(sys.exc_info()[0])
    raise

# os var definitions
os_name = os.name
os_platform = platform.system() + platform.release()

# instantiation of User class
testuser = User('John', 'Doe')
testuser.u_os_plt = os_name + os_platform


