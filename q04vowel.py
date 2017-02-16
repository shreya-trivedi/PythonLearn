#!/usr/bin/python3.5

''' Write a function that takes a character
(i.e. a string of length 1) and returns True
if it is a vowel, False otherwise. '''

import sys

def vowel(char):
    ''' Function to find if a character is a vowel or not.

    Args:
        char = a charachter

    Returns:
        True if character is a vowel.
    '''
    if char in "aeiou":
        print "True"
    else:
        print "False"

vowel(sys.argv[1])
