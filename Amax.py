'''
Problem Statement
Define a function max() that takes two numbers as arguments
and returns the largest of them. Use the if-then-else construct
available in Python. (It is true that Python has the max() function
built in, but writing it yourself is nevertheless a good exercise.)
'''
def max_num(num1, num2):
    if num1 > num2:
        print "num1 %d is greater than num2 %d" % (num1, num2)
    elif num1 < num2:
        print "num2 %d is greater than num1 %d" % (num2, num1)
    else:
        print "num1 and num2 are equal"

max_num(4, 3)
