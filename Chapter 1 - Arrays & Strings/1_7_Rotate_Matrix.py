#!/usr/bin/env python3
# 1/--/2020
# Cracking the Coding Interview Question 1.7 (Strings, Arrays, Hashtables)
# Rotate Matrix: Given an image represented by an NxN matrix,
# where each pixel in the image is 4 bytes, write a method to 
# rotate the image by 90 degrees. Can you do this in place?2

def rotate_matrix(matrix):
	isIrregular = False
	print("\n**======Start=======**")
	print("\nCurrent Matrix:")
	for row in matrix:
		print(row)

	# Get the dimensions of the current matrix: 
	numOfRows = len(matrix)
	# Here we are getting the maximum column length of the 
	# longest column incase the matrix is an irregular length
	numOfColumns = 0
	for row in matrix:
		#find the longest list to find the max column length
		columnLength = len(row)
		if columnLength > numOfColumns:
			numOfColumns = columnLength

	# If the matrix is an irregular shape, we will need to fill in the missing spots
	# Otherwise we cannot rotate the matrix
	for row in matrix:
		if len(row) < numOfColumns:
			while len(row) < numOfColumns:
				row.append(None)
				isIrregular = True


	if isIrregular:
		print("\nUpdated IRREGULAR Current Matrix:")
		for row in matrix:
			print(row)

	print("\nNumber of Rows: " + str(numOfRows))
	print("Number of Columns: " + str(numOfColumns) +"\n")
	print("-----------------\n")

	# Create new matrix
	print("Empty Rotated Matrix:")
	# For more information on 2D Matrices in Python
	# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
	rotatedMatrix = [[None for i in range(numOfRows)] for j in range(numOfColumns)]
	for row in rotatedMatrix: 
   		print(row) 
	print("\nNumber of Rows: " + str(numOfColumns))
	print("Number of Columns: " + str(numOfRows) + "\n")

   	
	# Iterate through the current matrix and update the new rotated matrix
	# The Rotated Matrix's ROW will be the Current Matrix's COLUMN
	# The Rotated Matrix's Column will be the Current Matrix's ROW, but iterated backwards
	print("#########################")

	rowOffset = numOfRows
	for row in range(0, numOfRows): 
		
		print("\nCurrent Row to Add: ")
		print(matrix[row])
		print("Updated Rotated Matrix: ")

		for r in rotatedMatrix:
			print(r)

		rowOffset -= 1

		print("\n")

		for column in range(0, numOfColumns):
			print("Original Row: " + str(row))
			print("Original Column: " + str(column))
			print("Item: " + str(matrix[row][column]))
			print("Rotated Row: " + str(column))
			print("Rotated Column: " + str(rowOffset))

			rotatedMatrix[column][rowOffset] = matrix[row][column]

			print(rotatedMatrix[column])
			print("\n")

		print("-------------------------")

	print("#### Rotated Matrix ####")
	for row in rotatedMatrix: 
   		print(row)

#Test Cases

#square_alphabetical_matrix = [['A','B','C'], ['D','E','F'], ['G','H','I']]
#rotate_matrix(square_alphabetical_matrix)
#rectangular_alphabetical_matrix = [['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L']]
#rectangular_alphabetical_matrix = [['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O']]
#rotate_matrix(rectangular_alphabetical_matrix)

irregular_matrix = [['A','B'], ['C','D','E','F'], ['G','H','I'], ['J','K'], ['L','M','N','O']]
rotate_matrix(irregular_matrix)