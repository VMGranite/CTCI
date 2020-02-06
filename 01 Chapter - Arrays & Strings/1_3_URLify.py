#!/usr/bin/env python3
# 1/9/2020
# Cracking the Coding Interview Question 1.3 (Strings, Arrays, Hashtables)
# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.

def replace_spaces ( url ):
    urlArray = []
    for char in url:
        urlArray.append(char)

    print(urlArray)
    for char in urlArray:
        if char == " ":
            print("Found Space")
            index = urlArray.index(char)
            urlArray[index] = "%20"
            print(urlArray)

    print ("REPLACED SPACES: " + ''.join(urlArray))

replace_spaces("A B C D E")
