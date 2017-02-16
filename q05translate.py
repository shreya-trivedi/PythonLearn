#!/usr/bin/python3.5

'''Write a function translate() that will translate a text into 
"rvarsprket" (Swedish for "robber's language"). That is,
double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun")should return the string 
"tothohisos isos fofunon".'''

import sys

def translate(str1):
    for char in str1:
        if char not in "aieou":
            str1 = char + 'o' + char
            print str1

translate("this is a cat")
