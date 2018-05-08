import app.menu as menu
import pynetwork.serverclient as sc
from pynetwork.tpls_server import start_handshake

NODE_STATUS = []

def setup():
    new_wallet()

def ns():
    try:
        n01 = int(input('node_status> '))
        return n01
    except TypeError:
        print('Invalid input')
        return

def node_server_run():
    ns = ns()
    NODE_STATUS.clear()
    NODE_STATUS.append(ns)
    start_handshake()

def new_wallet():
    import pynetwork.wallet as wallet
    wallet.generate_new_wallet()
    wallet.write_cwf()


menu_dict = {'Setup': setup,
            'start node server': node_server_run,
            'connect to node': sc.connect_to_node, 
            'quit': menu.quit_menu}

menu.initialize_menu(menu_dict, 'Network Client')