#!/usr/bin/python3.5

'''Define a function sum() and a function multiply() that sums
and multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10,
and multiply([1, 2, 3, 4]) should return 24.'''

nums = input("Enter in a list(comma saperated within square braces): ")

def sumnum(nums):
    ''' Function to get the sum of numbers.
    Args:
        nums: A list of numbers which are to be added.
    result:
        total: sum of the numbers.
    '''
    total = 0
    for n in nums:
        total += n
    print "addition is ", total

def multiply(nums):
    '''Fuction ti get the multiplication of the numbers.
    Args:
        nums: A list of numbers which are to be multiplied.
    result:
        total: multiplication of the numbers.
    '''
    total = 1
    for n in nums:
        total *= n
    print "multiplication is ", total

sumnum(nums)
multiply(nums)
