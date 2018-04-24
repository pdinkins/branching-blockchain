# client.py 
# environment for interacting with the network

import menu
import generate
import writer
import chain

def end_client():
    quit()


def help_menu():
    '''
    TODO: Internal documentation for interacting with the client interface
    '''
    print('This is the help page')


def addblock():
    lfn = input('Ledger file name: ')
    generate.new_block(lfn)


def print_chain():
    for i in range(0, len(chain.blockchain)):
        generate.print_block(chain.blockchain, i)


main_menu = {
    'HELP MENU': help_menu,
    'New Genesis Chain': generate.initailize_new_genesis_chain,
    'New block': addblock,
    'Print Genesis chain': print_chain,
    'Quit': end_client
}



while True:
    menu.initialize_menu(main_menu, 'BB Main Menu') 