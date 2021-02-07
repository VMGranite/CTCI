#!/usr/bin/env python3
# 1/27/2020
# Cracking the Coding Interview Question 2.1 (Linked Lists)
# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP: How would you solve this problem if a temporay buffer is not allowed?

import Linked_List

my_list = Linked_List.linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(1)
my_list.append(3)
my_list.append(1)
my_list.append(4)
my_list.append(4)
my_list.append(4)
my_list.display()

def remove_duplicates(my_list, item):
    my_list.findEqualTo(item)
    # Specify item to check for duplicates. 
    # Keeps one instance of the item, and remove all others
    my_list.removeThisDuplicate(item)

def remove_all_duplicates(my_list, items):
    # Specify list of items to check for duplicates. 
    # Keeps one instance of the item, and remove all others
    my_list.removeAnyDuplicates(items)

# This should find the duplicates, instead of specifying item to search for
def find_and_remove_all_duplicates(my_list):
    my_list.removeAnyDuplicates(my_list.findDuplicates())


#remove_duplicates(my_list, 1)
#remove_all_duplicates(my_list, [1,4])
find_and_remove_all_duplicates(my_list)
my_list.display()
