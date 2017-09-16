#!/usr/bin/env python

# A python script that uses /dev/urandom to generate random numbers
# The input opts.determine the amount of numbers, 
# and the range of them 

#! 

# TODO: delete unnecessary modules and find a cleaner way to do system stuff
from collections import Counter
from functools import reduce
from math import log10
#import numpy as np # TODO: change self.numbers into a numpy array
import optparse
import os
import secrets
from statistics import mean, median, pstdev, pvariance, stdev, variance
import sys
#import subprocess

def lazy_property(fn):
    '''Decorator that makes a property lazy-evaluated.
    '''
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazy_property

class RandomNumbers(object):
    """ A class that generates, stores, and gets information about
	cryptographically safe random numbers

	Atrributes:
            numbers: a list of random numbers with the same attributes
            count: the length of the above array
            min: the minimum value of the numbers (inclusive)
            max: the maximum value of the numbers (inclusive)
            TODO: interval: (TBA) the interval between each possible number
                - Validate min, max, count
    """
    def __init__(self, count=1, min=1, max=10):
        self.count  = count
        self.min    = min
        self.max    = max
        self.range  = max - min
        rnd         = lambda: secrets.randbelow(self.range + 1) + self.min
        self.numbers  = [rnd() for null in range(self.count)]

    def __str__(self):
        """ return the numbers only, in a space delimited string
        """
        string = ""
        for x in self.numbers:
            string += str(x) + " "
        return string

    @lazy_property
    def avg(self):
        return mean(self.numbers)

    @lazy_property
    def pvar(self):
        return pvariance(self.numbers)

    @lazy_property
    def std_dev(self):
        return self.var**0.5

    @lazy_property
    def pstd_dev(self):
        return pstdev(self.numbers)

    @lazy_property
    def med(self):
        return median(self.numbers)

    def print_frequency(self, ispercent=True):
        """ prints an output showing the frequencies of each number
        """
        #count the occurences
        freqs = Counter(self.numbers)
        # convert into a percentage
        if ispercent:
            freqs = [(i, freqs[i] / len(self.numbers) * 100.0) for i in freqs]

        out_str = "Frequencies of Numbers:\n"
        out_str += "-----------------------\n"
        for x in freqs:
            if x[0] > 0: chars = 1 + int(log10(x[0]))
            elif x[0] < 0: chars = 2 + int(log10(abs(x[0])))
            else: chars = 1
            out_str += "  "
            out_str += str(x[0]) + ":"
            padding = 8 - chars
            for i in range(0, padding):
                out_str += " "
            out_str += "{0:.2f}".format(x[1])
            out_str += "\n"
        print(out_str)

    def print_stats(self):
        # TODO: % diff from uniform dev
        print("mean: {:.2f}".format(self.avg))
        print("pvariance: {:.2f}".format(self.pvar))
        print("p-std-dev: {:.2f}".format(self.pvar**0.5))
        print("uniform-dev: {:.2f}".format(self.range/(12**0.5)))
        print("median: {}".format(self.med))
        self.print_frequency()



if __name__ == '__main__':
    # main execution
    
    # FIRST check that the host OS has a 
    #   cryptographically secure method to generate random numbers
    # If not, exit with an error message
    while True:
        try:
            temp = os.urandom(1)
            break
        except NotImplementedError:
            print("[ERROR]: Your host operating system can't create safe random numbers")
            sys.exit(1)

    parser = optparse.OptionParser()
    help_strings = { 
        "min": "sets the minimum value (inclusive) of random numbers [default = 1]",
        "max": "sets the maximum value (inclusive) of random numbers [default = 10]",
        "count": "sets the amount of random numbers to generate [default = 1]",
        "stats": "print out the stats of the given random numbers"
        }

    parser.add_option('-f', '--min',
            dest='min', help=help_strings["min"], type=int, default=1)
    parser.add_option('-c', '--max',
            dest='max', help=help_strings["max"], type=int, default=10)
    parser.add_option('--count', '--number', '-n',
            dest='count', help=help_strings["count"], type=int, default=1)
    parser.add_option('-s', '--stats',
            dest='stats', help=help_strings["stats"], action="store_true", default=False)

    (opts, args) = parser.parse_args()
    numbers = RandomNumbers(count=opts.count, min=opts.min, max=opts.max)

    if opts.stats:
        numbers.print_stats()
    else:
        print(numbers)

    


