#!/usr/bin/env python3
# 2/4/2020
# Cracking the Coding Interview Question 3.3 (Stacks and Queues)
# Stack of Plates: Image a (literal) stack of plates.
# If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the 
# previous stack exceeds some threshold. Implement a data structure 
# SetOfStacks that mimics this. SetOfStacks should be composed of 
# several stacks and shoudld create a new stack once the previous one 
# exceeds capacity. SetOfStacks.push() and .pop() should behave
# identically to a single stack (That is, pop() should return the same 
# values as it would if there were just a single stack)
# https://www.geeksforgeeks.org/stack-in-python/


from queue import LifoQueue 

class Stack:
	def __init__(self, heightOfStack):
		self.stack = LifoQueue(maxsize = heightOfStack) 


def createStacks(numOfStacks, heightOfStack):
	print("---Start---")
	print("Num of Stacks: " + str(numOfStacks))
	print("Height of Stacks: " + str(heightOfStack))
	stackIndex = 0
	setOfStacks = []
	print("\nSet of Stacks = " + str(len(setOfStacks)) + "\n")

	while numOfStacks > stackIndex:
		print("+ Created New Stack")
		setOfStacks.append(Stack(heightOfStack))

		for i in range(0, heightOfStack):
			setOfStacks[stackIndex].stack.put(i)

		stackIndex += 1

	print("\nSet of Stacks = " + str(len(setOfStacks)))

	while stackIndex > 0:
		stackIndex -= 1
		print("\n- Empty Stack (" + str(stackIndex + 1) + ") - ")
		for i in range(0, heightOfStack):
			print("Stack Pop '" + str(setOfStacks[stackIndex].stack.get()) + "'")

	print("---Complete---")

createStacks(3, 5)

