'''
Created on Aug 28, 2018

# msdie.py
# Class definition for an n-sided die.

To Class the class from file do the following

from msdie import MSDie


@author: ECOLINNA
'''

from random import randrange

class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1
        
    def roll(self):
        self.value = randrange(1, self.sides+1)
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
        
