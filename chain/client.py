# client.py 
# environment for interacting with the network

import menu, test
import blocks, chain, classes
import ipfs, ipfsdaemon, ledger


def help_menu():
    '''
    TODO: Internal documentation for interacting with the client interface
    '''
    print('This is the help page')


# MAIN MENU DICT 
# menu.py for more documentation
main_menu = {
    'HELP MENU': help_menu,
    'Quit': menu.quit_menu
}

# Launch the terminal menu interface 
menu.initialize_menu(main_menu, 'BB Main Menu') 