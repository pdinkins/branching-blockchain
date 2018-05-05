#!/usr/bin/env python

# Data and functions for users
class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.reputation = 0.0
        self.fullname = self.fullname_construction()

    # fullname
    def fullname_construction(self):
        return '{}{}'.format(self.first, self.last)
        
    # method for determining user network location
    def location(self):
        pass
        
    # method for storing user reputation status
    def reputation_calc(self):
        category_rep = self.reputation

# Data and functions for ideas
class Idea:
    
    def __init__(self, title, category, value, creator):
        self.title = title
        self.category = category
        self.value = value
        self. creator = creator     # userfullname

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        pass
    
    @staticmethod
    def hash(block):
        pass
    
    @property
    def last_block(self):
        pass
