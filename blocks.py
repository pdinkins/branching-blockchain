# block creation related functions

import hashlib as hasher
import datetime


class Genesis_Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.current_hash = self.hash_block()
        self.next_hash = self.next_bhash()
    
    def next_bhash(self):
        shha = hasher.sha256()
        shha.update(str(self.previous_hash).encode('utf-8') +
                    str(self.current_hash).encode('utf-8'))
        return shha.hexdigest()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') + 
                   str(self.timestamp).encode('utf-8') + 
                   str(self.data).encode('utf-8') + 
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


class Genesis_Chain:
    '''
    TODO: allow for dynamic starting info
    '''
    def __init__(self):
        self.g_index = 0

    @classmethod
    def generate_genesis_block(self):
        self.g_index = 0
        self.g_ts = datetime.datetime.now()
        self.g_d = "data: Genesis Block"
        self.g_hash = "GENESIS BLOCK BEGINNING HASH"
        return Genesis_Block(self.g_index, self.g_ts, self.g_d, self.g_hash)


class Block:
    def __init__(self, previoushash, currenthash):
        self.previous_hash = previoushash
        self.current_hash = currenthash
        self.next_hash = self.next_bhash()

    def next_bhash(self):
        shha = hasher.sha256()
        shha.update(str(self.previous_hash).encode('utf-8') +
                    str(self.current_hash).encode('utf-8'))
        return shha.hexdigest()

