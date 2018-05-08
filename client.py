import app.menu as menu
import pynetwork.serverclient as sc


def setup():
    new_wallet()

def new_wallet():
    import pynetwork.wallet as wallet
    wallet.generate_new_wallet()
    wallet.write_cwf()


menu_dict = {'Setup': setup,
            'connect to node': sc.connect_to_node, 
            'quit': menu.quit_menu}

menu.initialize_menu(menu_dict, 'Network Client')