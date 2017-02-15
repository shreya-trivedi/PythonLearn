#! /usr/bin/python3.5

'''
Problem Statement
Define a function max() that takes two numbers as arguments
and returns the largest of them. Use the if-then-else construct
available in Python. (It is true that Python has the max() function
built in, but writing it yourself is nevertheless a good exercise.)
'''
import sys

def max_num(num1, num2):
    """Function to find the larger number.

    Args:
        num1: The first parameter.
        num2: The second parameter.

    Returns:
        The larger number.
    """

    if num1 > num2:
        print "num1 %r is greater than num2 %r" % (num1, num2)
    elif num1 < num2:
        print "num2 %r is greater than num1 %r" % (num2, num1)
    else:
        print "num1 and num2 are equal"

max_num(sys.argv[1], sys.argv[2])
