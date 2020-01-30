#!/usr/bin/env python3
# 1/29/2020
# Cracking the Coding Interview Question 2.5 (Linked Lists)
# Sum Lists: You have two numbers represented by a linked list,
# where each node contains a single digit. The digits are stored in 
# reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as
# a linked list
# EXMAPLE:
# Input: (7 > 1 > 6) + (5 > 9 > 2). That is 617 + 295
# Output: 2 > 1 > 9. That is 912

import Doubly_Linked_List
first_list = Doubly_Linked_List.doubly_linked_list()
first_list.append(7)
first_list.append(1)
first_list.append(6)
first_list.display()

second_list = Doubly_Linked_List.doubly_linked_list()
second_list.append(5)
second_list.append(9)
second_list.append(2)
second_list.display()

second_list.reverseOrder()
