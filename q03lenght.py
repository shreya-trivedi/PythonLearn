#!/usr/bin/python3.5

''' 
Problem Statement
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in,
but writing it yourself is nevertheless a good exercise.)
'''

def get_lenght(word):
    count = 0
    for char in word:
        count += 1
    return count

print(get_lenght('abhi'))

