#!/usr/bin/env python

# A python script that uses /dev/urandom to generate random numbers
# The input options determine the amount of numbers, 
# and the range of them 

from fabric.api import run

class random_numbers(object):
    """ A class to store random numbers as an ordered list
    Also includes properties like min, max, interval and number of randoms
    """
    
    """ Atrributes:
            numbers: a list of random numbers with the same attributes
            count: the length of the above array
            min: the minimum value of the numbers (inclusive)
            max: the maximum value of the numbers (inclusive)
            TODO: interval: (TBA) the interval between each possible number
    """

    def __init__(self, count=1, min=0, max=10):
        self.count      = count
        self.min        = min
        self.max        = max
        self.numbers = []
        
        for x in range(0, count):
            self.numbers.append(

if __name__ == '__main__':
    # main execution

