#!/usr/bin/env python3
# 1/29/2020
# Cracking the Coding Interview Question 2.3 (Linked Lists)
# Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node
# EXAMPLE: 
# Input: the node c from the linked list a > b > c > d > e > f 
# Result: nothing is returned, but the new linked list looks like 
#         a > b > d > e > f

import Linked_List
my_list = Linked_List.linked_list()
my_list.append('a')
my_list.append('b')
my_list.append('c')
my_list.append('d')
my_list.append('e')
my_list.append('f')
my_list.append('g')
my_list.append('h')
my_list.display()

def delete_middle_node(my_list, node):
    index = my_list.findFirstMatch(node)
    length = my_list.length()

    if index != 0 and index != (length-1):
        my_list.eraseByIndex(index)
        print("\nUpdated Linked List: ")
        print("Removed - Node " + node)
        my_list.display()
    elif index == 0:
        print("\nERROR - Cannot delete. This is the first node.")
        print("INDEX - " + str(index))
    elif index == (length - 1):
        print("\nERROR - Cannot delete. This is the last node.")
        print("INDEX - " + str(index))

delete_middle_node(my_list, 'a')
delete_middle_node(my_list, 'c')
delete_middle_node(my_list, 'e')
delete_middle_node(my_list, 'h')