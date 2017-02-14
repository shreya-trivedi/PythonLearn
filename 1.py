# - -coding: utf- 8 -

import sys

#num1 = 4
#num2 = 5

#num1 = input("enter first number: ")
#num2 = input("enter second number: ")

def max_num(num1, num2):
	if (num1 > num2):
	  print "num1 %d is greater than num2 %d" % (num1, num2)
	elif (num1 < num2):
	  print "num2 %d is greater than num1 %d" % (num2, num1)
	else:
	  print "num1 and num2 are equal"

max_num(4,3)
#max_num(sys.argv[1],sys.argv[2])
