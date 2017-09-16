#!/usr/bin/env python
""" Python script that takes a given wordlist, uses a the rng.py script, then
    produces a string of a given number of words,
    thus creating a randomized word string.

    Terminology:
        - 'words' are used to denote a list of cleaned words
        - 'word' is any cleaned string that contains a wordlist word

    TODO:
        - More variety of helper functions for different input circumstances...
            - File path input
            - File input
            - Generic 'collection' type input
            - std_in input
            - Single string input
            - Byte input
            - Unclean string input
            - Base64 input
        - Proper Exception handling for all functions & main execution
        - External unit tests
        - External timing evaluation for optimization
        - External randomness evaluation
        - Some evaluation of if the file or std_in is actually a wordlist
"""

################################################################################
## Imports
################################################################################

import optparse
from os import path
from re import sub, compile
import rng
from sys import exit



################################################################################
## Module Functions
################################################################################

def get_file(file_path):
    """ Reads a file path after validating it in ways relevant to this module
        
        Args:
            file_path (str): takes a string representing a file path.
                file_path gets validated for being an existing file or link.
                If, a non-valid file is reached an exception is thrown
        Returns:
            words_file (os.path.file): a python-read filetype
    """
    # TODO: Add input type validation
    # first check to see if the input file exists
    if not path.isfile(words_path):
        print()
        print("[ERROR]: The given input file path, doesn't lead to a file!")
        print("======== Please try again with a valid file path to a wordlist")
        print()
        exit(1)

    # get the file
    return open(file_path, "r")

def read_file_lines(file):
    """ Reads opened wordlist file into lines & validates it as a file

    Args:
        file (TextIOWrapper): a python-opened file as an IOWrapper
            ie. what results from open()

    Returns:
        [str]: returns a validated list of strings

    TODO:
        - Perform some basic filetype validation for being a wordlist file
    """
    # TODO: Validate the file
    return file.readlines()

def clean_word(dirty_word):
    """ Reads a single word string from unwanted characters

    Args:
        dirty_word (str): a string of a word that could have unwanted chars.
    
    Returns:
        str: a string of a cleaned/filtered version of dirty_word

    TODO:
        - Take in a regex pattern to clean word with
        - Perform some classification algorithm to improve cleaning
        - GPGPU acceleration
    """
    

def read_words(words_string=None, word_lines=None, 
        words_file=None, words_path):
    """ A flexible version of previous functions that 'intelligently'
        interprets the input source and returns a clean list of words

    Args:
        words (many datatypes): A data source of words that may or may not
        be either clean or an intelligible wordlist. Depending on how it
        gets interpreted, it will either return a clean list of words, or
        throw exceptions

    Returns:
        [str]: A list of cleanly parsed word strings

    TODO:
        - Inteligent-ish input source heuristics or learned classification
        of input to evaluate how and if it should be interpreted
    """
    # trim out all non-alphabetic characters
    # TODO: explore options of including non-alphas and remove only file indeces
    # this could be useful for creating, for example, 1337 $p3@k wordlists
    #trim_nonalpha = lambda s: re.sub('^[a-zA-z]',s)


def search_word(pattern, words, case_sensitive=False):
    """ Searches for a string pattern within a list of strings and returns its index

    Args:
        pattern (str): a string pattern for the substring to be searched after.
        words ([str]): a list of words to search for 


################################################################################
## Main Execution
################################################################################

if __name__ == '__main__':
    # main execution
    
    # Parse arguments
    parser = optparse.OptionParser()
    help_strings = { 
        "input": "specifies the path to the wordlist file [default = ./wordlist.txt]",
        "output": "specifies the path to the random generated words file " +
        "[default = ./random.txt]",
        "number": "specifies the number of words to string together [default = 5]",
        }
    
    parser.add_option('-i', '--input', '--file',
            dest='input', help=help_strings["input"], type="string", default="./wordlist.txt")
    parser.add_option('-o', '--output',
            dest='output', help=help_strings["output"], type="string", default="./random.txt")
    parser.add_option('-n', '--words', '--number', '--count',
            dest='number', help=help_strings["number"], type=int, default=5)
   
    (opts, args) = parser.parse_args()

    words_path = opts.input
    out_file = opts.output
    num_words = opts.number

    # check to make sure a valid number of words has been given
    if num_words < 1:
        print()
        print("[ERROR]: Can't generate less than one random words!")
        print("======== Please enter a number greater than 0")
        print()
        exit(1)

    # check to see if the output path already has a file
    # prompt the user to see if they want it replaced
    if path.isfile(out_file):
        print()
        print("File " + out_file + " already exists!")
        ans = print("Replace it? ([y]/n): ").lower()
        isinvalid = True
        yesses = ["y", "yes", "ys", "ye", "yeah", "yea", "ya", ""]
        nos = ["n", "no", "nay", "ne", "na", "nah"]
        isyes = False
        isno = False
        while isinvalid:
            for valid_ans in yesses:
                if valid_ans == ans:
                    isyes = True
                    isinvalid = False
            for valid_ans in nos:
                if valid_ans == ans:
                    isno = True
                    isinvalid = False
            ans = print(
                    "Not a valid response, please enter (y/n) or enter to confirm: ")
        if isno:
            print()
            print("Not replacing file " + out_file + " , re-run with a new file path")
            print()
            exit(1)

    # read in the wordlist
    words = get_wordlist(words_path)
    print(str(words[:5]))

"""
