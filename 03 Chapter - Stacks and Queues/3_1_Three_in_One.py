#!/usr/bin/env python3
# 1/31/2020
# Cracking the Coding Interview Question 3.1 (Stacks and Queues)
# Three in One: Describe how you could use a single array to implement three stacks

# Python uses lists to create arrays
# Create 3 lists and treat them like stacks - only add to the end pf the list, and do not index
oneLongList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#Splot the oneLongList into 3 other lists
stackOne = oneLongList[0:4]
stackTwo = oneLongList[4:8]
stackThree = oneLongList[8:]

print("Original Stack: \n" + str(oneLongList))
print("Stack One: " + str(stackOne))
print("Stack Two: " + str(stackTwo))
print("Stack Three: " + str(stackThree))

print("\nPop Stack One: " + str(stackOne.pop()))
print("Stack One: " + str(stackOne))

print("\nPush|Append to Stack Two: " + str(1))
stackTwo.append(1)
print("Stack Two: " + str(stackTwo))
print("Push|Append to Stack Two: " + str(2))
stackTwo.append(2)
print("Stack Two: " + str(stackTwo))

print("\nPop Stack Three: " + str(stackThree.pop()))
print("Pop Stack Three: " + str(stackThree.pop()))
print("Pop Stack Three: " + str(stackThree.pop()))
print("Pop Stack Three: " + str(stackThree.pop()))
#Error will be thrown if you pop any more, because the list is now empty
print("Stack Three: " + str(stackThree))

print("\nOriginal Stack is still the same: \n" + str(oneLongList))

