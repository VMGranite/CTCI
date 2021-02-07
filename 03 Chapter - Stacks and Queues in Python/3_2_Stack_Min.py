#!/usr/bin/env python3
# 1/31/2020
# Cracking the Coding Interview Question 3.2 (Stacks and Queues)
# Stack Min: How would you design a stack which, in addition to
# push and pop, has a function which returns the minimum element?
# Push, pop and min should all operatue in O(1) time. 

# I would start by taking the first element and choosing that as the 
# smallest element. Then traverse through the list checking if the 
# next element was smaller. If it was smaller, that would become the 
# new min.

# min = 0
def findMin(unsortedList):
	print("Original List: \n" + str(unsortedList))
	minElement = unsortedList[0]
	print("\nCurrent Min: " + str(minElement))

	for element in unsortedList:
		if element < minElement:
			print("New min found! - " + str(element))
			minElement = element
	print("FINAL MIN: " + str(minElement))

	print("\nSearch Completed\n-------------------")

findMin([100, 44, 22, 500, 23, 14, 2, 55, 6, 1, 67])

findMin([0,1,2,3,4,5])

findMin([5,4,3,2,1,0])