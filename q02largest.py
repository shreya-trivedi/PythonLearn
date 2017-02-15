'''
Problem Statement
Define a function max_of_three() that takes three numbers
as arguments and returns the largest of them.
'''

import sys

def larnum(num1, num2, num3):
    """Function to find the larger number.

    Args:
        num1: The first parameter.
        num2: The second parameter.
        num3: The third parameter.

    Returns:
        The largest number.
    """

    largest = num1

    if num2 > largest:
        largest = num2

    if num3 > largest:
        largest = num3

    print "the largest number is", largest
    return largest

larnum(sys.argv[1], sys.argv[2], sys.argv[3])
