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
    my_list.removeThisDuplicate(item)
    my_list.display()

# def remove_any_duplicates(my_list, items):
#     my_list.findEqualTo(item)
#     my_list.removeAnyDuplicates(item)
#     my_list.display()

remove_duplicates(my_list, 1)
#remove_any_duplicates(my_list, [1,4])
