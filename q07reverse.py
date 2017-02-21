#!/usr/bin/python2.7

'''Define a function reverse() that computes the reversal of a string.
For example,
reverse("I am testing") should return the string "gnitset ma I".'''

data = input("enter a string:")

def reverse(data):
    ''' Function to reverse a string'''
    i = len(data)
    data1 = ""
    while i:
        i -= 1
        data1 += data[i]
    print data1

reverse(data)
