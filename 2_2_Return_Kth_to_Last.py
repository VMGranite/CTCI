#!/usr/bin/env python3
# 1/28/2020
# Cracking the Coding Interview Question 2.2 (Linked Lists)
# Return Kth to Last: Implement an algorithm to find the 
# kth to last element of a singly linked list.

import Linked_List

my_list = Linked_List.linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)
my_list.append(8)
my_list.append(9)
my_list.display()

# find the Kth from the last element

def find_kth_to_last_element(my_list, k):
	length = my_list.length()
	kOffset = length - k 
	element = my_list.getByIndex(kOffset)
	print("Element " + str(element) + " is the " + str(k) + "th element from the last")

# Example: K = 4, The 4th element from the last is 6 (Node.data = 6)
find_kth_to_last_element(my_list, 4)
# Example: K = 6, The 4th element from the last is 4 (Node.data = 4)
find_kth_to_last_element(my_list, 6)
# Example: K = 8, The 4th element from the last is 2 (Node.data = 2)
find_kth_to_last_element(my_list, 8)