#!/usr/bin/python3.5

'''Write a function translate() that will translate a text into
"rvarsprket" (Swedish for "robber's language"). That is,
double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun")should return the string
"tothohisos isos fofunon".'''

import sys

def translate(str1):
    '''Function to translate string.
    Args
        str1 : String to be converted.
    Returns
        Converted string.'''

    str2 = ""
    for char in str1:
        if char not in "aieou ":
            str1 = char + 'o' + char
            str2 += str1
        else:
            str1 = char
            str2 += char
    print str2

translate(sys.argv[1])
