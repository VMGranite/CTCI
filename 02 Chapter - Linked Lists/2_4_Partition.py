#!/usr/bin/env python3
# 1/--/2020
# Cracking the Coding Interview Question 2.4 (Linked Lists)
# Partition: Write code to partition a linked list around a value x,
# such that all nodes less than x come before all node greater than
# or equal to x. If x is contained within the list, the values
# of x only need to be after the elements less than x (see below).
# The partition element x can appear anywhere in the "right partition"
# it does not need to appear between the left and right partitions
# EXAMPLE:
# Input: 3 > 5 > 8 > 5 > 10 > 2 > 1 [Partition 5]
# Output: 3 > 1 > 2 > 10 > 5 > 5 > 8

import Linked_List
my_list = Linked_List.linked_list()
my_list.append(3)
my_list.append(5)
my_list.append(8)
my_list.append(5)
my_list.append(10)
my_list.append(2)
my_list.append(1)
my_list.display()