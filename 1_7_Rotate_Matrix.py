#!/usr/bin/env python3
# 1/--/2020
# Cracking the Coding Interview Question 1.7 (Strings, Arrays, Hashtables)
# Rotate Matrix: Given an image represented by an NxN matrix,
# where each pixel in the image is 4 bytes, write a method to 
# rotate the image by 90 degrees. Can you do this in place?2

def rotate_matrix(matrix):
	print("Current Matrix:")
	for row in matrix:
		print(row)

	#get the dimensions of the current matrix
	numOfRows = len(matrix)
	numOfColumns = len(matrix[0])
	print("\nNumber of Rows: " + str(numOfRows))
	print("Number of Columns: " + str(numOfColumns) +"\n")
	print("-----------------")

	#create new matrix
	print("Empty Rotated Matrix:")
	#For more information on 2D Matrices in Python
	#https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
	rotatedMatrix = [[0 for i in range(numOfRows)] for j in range(numOfColumns)]
	for row in rotatedMatrix: 
   		print(row) 
	print("\nNumber of Rows: " + str(numOfColumns))
	print("Number of Columns: " + str(numOfRows) +"\n")

   	
	#iterate through the current matrix and update the new rotated matrix
	#the rotated matrix will show that the current column is the new row
	print("-----------------")
	for row in range(0, numOfRows): 
		print(matrix[row])

		for r in rotatedMatrix: 
   			print(r)

		for column in range(0, numOfColumns):
			print("---Row: " + str(row))
			print("---Column: " + str(column))
			print("-Item: " + matrix[row][column])
			print("New Row: " + str(column))
			print("New Column: " + str(row))
			rotatedMatrix[column][row] = matrix[row][column]
			print(rotatedMatrix[column])

		print("-----Row: " + str(row))

	print("-----------------")


	#create new matrix
	print("Updated Rotated Matrix:")
	for row in rotatedMatrix: 
   		print(row)

# This is a list with lists to make a matrix
alphabetical_matrix = [['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L']]
#alphabetical_matrix = [['A','B','C'], ['D','E','F'], ['G','H','I']]
rotate_matrix(alphabetical_matrix)