#!/usr/bin/env python3
# 1/11/2020
# Cracking the Coding Interview Question 1.4 (Strings, Arrays, Hashtables)
# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check
# if they are one edit ( or zero edits ) away.
# EXAMPLE
# pale, ple -> TRUE
# pales, pale -> TRUE
# pale, bale -> TRUE
# pale, bake -> FALSE

def oneEditAway (first, second):
    print("-----START----- \n")
    print("First String Input: " + first)
    print("Second String Input: " + second)
    print("")
    firstLength = len(first)
    secondLength = len(second)
    firstList = list(first)
    secondList = list(second)

    #Check if the strings are exactly the same
    if first == second:
        print ("These strings match exactly already. \n")
    else:
        if  firstLength == secondLength:
            print ("ACTION > Check to Edit ONE character \n")
            editReplace(firstList, secondList)
        # Check if there is only a one character difference in length
        elif abs(firstLength - secondLength) == 1:
            print ("ACTION > Add ONE character \n") #or Remove
            editInsert(firstList, secondList)
        else:
            print ("Requires more than one addition or removal. \n")

    print("------END------ \n")

def editReplace(firstList, secondList):
    numberToReplace = 0
    for i in range(len(firstList)):
        if firstList[i] != secondList[i]:
            numberToReplace += 1
    if numberToReplace == 1:
        for i in range(len(firstList)):
            print("First Letter at Index {}: {}".format(i + 1, firstList[i]))
            print("Second Letter at Index {}: {}".format(i + 1, secondList[i]))
            if firstList[i] != secondList[i]:
                secondList[i] = firstList[i]
                print("^ Change Required Here")
            print("")
        print("ORIGINAL First String: " + "".join(firstList))
        print("UPDATED Second String: " + "".join(secondList) + "\n")
    else:
        print("More than One Away - Requires (" + str(numberToReplace) + ") replacements. \n")

def editInsert(firstList, secondList):
    longerString = firstList if len(firstList) > len(secondList) else secondList
    shorterString = secondList if len(firstList) > len(secondList) else firstList

    print("Longer String: " + str(longerString))
    print("Shorter String: " + str(shorterString))
    print("")

    for i in range(len(longerString)):
        if longerString[i] != shorterString[i]:
            shorterString.insert(i, longerString[i])
            print("ACTION > Inserted Missing Character Here.")

        print("Longer String Letter at Index {}: {}".format(i + 1, longerString[i]))
        print("Shorter String Letter at Index {}: {}".format(i + 1, shorterString[i]))
        print("")
    print("ORIGINAL Longer String: " + "".join(longerString))
    print("UPDATED Shorter String: " + "".join(shorterString) + "\n")

# Adding missing character
oneEditAway("ABDCC", "ABCC")
oneEditAway("ABCC", "ABDCC")
# Exact Strings
oneEditAway("dog", "dog")
# Replace Letter
oneEditAway("Male", "Make")
oneEditAway("Make", "Male")
# Requires too many replacements
oneEditAway("Mail", "Male")
