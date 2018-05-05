# client.py 
# environment for interacting with the network

import menu
import generate
import writer
import chain
import network
import ipfs

def help_menu():
    '''
    TODO: Internal documentation for interacting with the client interface
    '''
    print('This is the help page')


def addblock():
    lfn = input('Ledger file name: ')
    generate.new_block(lfn)


def print_current_block():
    for i in range(0, len(chain.blockchain)):
        generate.print_block(chain.blockchain, i)

def ngc():
    name = input("name>\t")
    generate.initailize_new_genesis_chain(name)


main_menu = {
    'HELP MENU': help_menu,
    'Initailize IPFS': network.ipfs_daemon_init,
    'New Genesis Chain': ngc,
    'Upload genesis chain to IPFS': ipfs.upload_g_chain,
    'ipfs l decon': ipfs.ipfs_ledger_deconstruct,
    'New block': addblock,
    'Print current block': print_current_block,
    'Quit': menu.quit_menu
}




menu.initialize_menu(main_menu, 'BB Main Menu') 