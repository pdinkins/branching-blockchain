# This module is used to created a new ledger 
# aswell as parse and write changes to it

import csv
import node_server
 
class NewLedger:
    # This class creates a new ledger file:  'legdername'.file 
    # CALLING THE ENTIRE CLASS WILL GIVE ERRORS
    def __init__(self, name):
        self.name = name
        self.filename = name + '.csv'
        self.file = self.generate_new_ledger()
    # creates ledger file with name given in class creation
    def generate_new_ledger(self):
        open(self.filename, mode='w')


class Ledger:
    # class is strictly for storing ledger file names
    # allows user to not have to type '.csv' when they enter ledger name
    def __init__(self, name):
        self.name = name
        self.filename = name + '.csv'


##### Do not touch this function 
## this function is used by the node_server.py file 
def ledger_parse(ledger_file_name):
    '''
    Parse the ledger and append the values to respective list for 
    easy access in future computations
    
    #TODO: re-work the function to allow for dynamic parsing only 
            needed parts of the ledger to save memory and cpu power
    '''
    # dump the previous dynamic lists
    node_server.dynamic_data_dump()
    try:
        with open(ledger_file_name) as ledger:
            reader = csv.reader(ledger)
            for row in reader:
                node_server.trusted_hashes.append(row[0])
    except FileNotFoundError:
        print('ERROR: LEDGER__NOT__FOUND')


def ledger_constructor(ledger_file_name, block_to_write):
    '''
    ledger_file_name = Ledger().file
    
    block_to_write = [previous hash, current hash, next hash]

    Add a single block to the ledger
    
    #TODO: seperate function the checks to make sure the block
            to be added doesnt already exist on the ledger
    '''
    try:
        with open(ledger_file_name, 'a', newline='') as ledger:
            writer = csv.writer(ledger)
            writer.writerow([block_to_write[0],
                             block_to_write[1],
                             block_to_write[2]])
    except FileNotFoundError:
        print('ERROR: LEDGER__NOT__FOUND')
    