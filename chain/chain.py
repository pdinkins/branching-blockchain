'''
# CHAIN
# Stores current blockchain information and chain functions
# All storage is dynamic and is determined by the users actions

'''

# contains block objects
blockchain = []

# data generated in the ledger_parse function
p_hash = []     # previous hash
c_hash = []     # current hash
n_hash = []     # next hash


# clears all data from lists so they can be re-initailized
def dynamicdump():
    blockchain.clear()
    p_hash.clear()
    c_hash.clear()
    n_hash.clear()
