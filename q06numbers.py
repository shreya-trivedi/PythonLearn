#!/usr/bin/python3.5

'''Define a function sum() and a function multiply() that sums
and multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10,
and multiply([1, 2, 3, 4]) should return 24.'''

numbers = [1, 2, 3, 4]

def sumnum(numbers):
    total = 0
    for n in numbers:
        total += n 
    print "addition is ", total

def multiply(numbers):
    total = 1
    for n in numbers:
        total *= n
    print "multiplication is ", total

sumnum(numbers)
multiply(numbers)
