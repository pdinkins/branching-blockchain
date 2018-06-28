'''
# CHAIN
# Stores current blockchain information and chain functions
# All storage is dynamic and is determined by the users actions

'''


class Blockchain:
    '''
    # contains block objects
    '''
    def __init__(self):
        self.chain = []
        self.current_transactions = []


    def new_block(self):
        pass

    @property
    def current_block(self):
        pass

    @property
    def last_block(self):
        pass

