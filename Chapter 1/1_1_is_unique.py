#!/usr/bin/env python3
# 1/9/2020
# Cracking the Coding Interview Question 1.1 (Strings, Arrays, Hashtables)
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# https://www.geeksforgeeks.org/python-find-keys-with-duplicate-values-in-dictionary/

def unique_string_characters ( inputString ):
    inputStringDict = {}
    duplicatesDict = {}
    index = 0

    #iterate through string and populate dictionary
    for letter in inputString:
        inputStringDict[index] = letter
        index += 1

    for key, value in inputStringDict.items():
        # setdefault() will find if value is in the dictionary
        # set() will be the value type used
        # add() will add key to the matching set value
        # print(duplicatesDict)
        duplicatesDict.setdefault(value, set()).add(key)
        # READS AS
        # from duplicatesDict get this VALUE
        # make VALUE into a SET
        # if unique KEY, add to this VALUE SET

    # create an array called RESULT
    # populate the array with the KEY that has more than one VALUE
    result = [key for key, values in duplicatesDict.items()
                              if len(values) > 1]

    for key, values in duplicatesDict.items():
        if len(values) > 1:
            print('"' + key + '"')
            print(values)

    print(duplicatesDict)
    print("duplicate values", result)

unique_string_characters("aaa bb c eeee")
