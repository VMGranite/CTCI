#!/usr/bin/env python3
# 1/9/2020
# Cracking the Coding Interview Question 1.2 (Strings, Arrays, Hashtables)
# Given 2 strings, write a method to decide if one is a permutation of the other.
# Permutation Example: ABC, ACB, BCA <== Same letters, but rearranged
# NOT Permutation Example: ABB, CCA, AGD

def permutation_check ( x, y ):
    print("Input x: " + x)
    print("Input y: " + y)
    permutation = False

    # check if strings are the same length
    if len(x) != len(y):
        print("NOT A PERMUTATION: These strings are not the same length.")
    elif x == y:
        print("NOT A PERMUTATION: These strings match exactly.")
    else:
        xSorted = "".join(sorted(x))
        print("Sorted x: " + xSorted)
        ySorted = "".join(sorted(y))
        print("Sorted y: " + ySorted)
        if xSorted == ySorted :
            print("PERMUTATION - Permutation alphabetically")
            permutation = True
        else:
            print("NOT A PERMUTATION: Strings do not match")
    print("-----------------------------")

    # Going through strings without alphabetically sorting
    if permutation:
        xList = list(x)
        yList = list(y)
        print("Original: ")
        print(xList)


        for yLetter in yList:
            #find if letter in y is found in x
            if yLetter in xList:
                print("Letter Found: " + yLetter)
                print(xList)
                #remove letter if found
                xList.remove(yLetter)

        if len(xList) == 0:
            print("PERMUTATION - Permutation find matching letter")


permutation_check("QWTY", "QWTYYY")
permutation_check("QWERTY", "YWTGRE")
permutation_check("QWERTY", "YWTQRE")
permutation_check("ABAAB", "AABBA")
