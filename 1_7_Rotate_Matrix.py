#!/usr/bin/env python3
# 1/--/2020
# Cracking the Coding Interview Question 1.7 (Strings, Arrays, Hashtables)
# Rotate Matrix: Given an image represented by an NxN matrix,
# where each pixel in the image is 4 bytes, write a method to 
# rotate the image by 90 degrees. Can you do this in place?2

def rotate_matrix(matrix):
	print("\nCurrent Matrix:")
	for row in matrix:
		print(row)

	#get the dimensions of the current matrix
	numOfRows = len(matrix)
	numOfColumns = len(matrix[0])
	print("\nNumber of Rows: " + str(numOfRows))
	print("Number of Columns: " + str(numOfColumns) +"\n")
	print("-----------------\n")

	#create new matrix
	print("Empty Rotated Matrix:")
	#For more information on 2D Matrices in Python
	#https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
	rotatedMatrix = [[0 for i in range(numOfRows)] for j in range(numOfColumns)]
	for row in rotatedMatrix: 
   		print(row) 
	print("\nNumber of Rows: " + str(numOfColumns))
	print("Number of Columns: " + str(numOfRows) + "\n")

   	
	#iterate through the current matrix and update the new rotated matrix
	#The Rotated Matrix's ROW will be the Current Matrix's COLUMN
	#The Rotated Matrix's Column will be the Current Matrix's ROW, but iterated backwards
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
			print("Item: " + matrix[row][column])
			print("Rotated Row: " + str(column))
			print("Rotated Column: " + str(rowOffset))

			rotatedMatrix[column][rowOffset] = matrix[row][column]

			print(rotatedMatrix[column])
			print("\n")

			subtractOne = True

		print("-------------------------")

	print("#### Rotated Matrix ####")
	for row in rotatedMatrix: 
   		print(row)

#Square and Rectanglular Matrices
#alphabetical_matrix = [['A','B','C'], ['D','E','F'], ['G','H','I']]
#alphabetical_matrix = [['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L']]
alphabetical_matrix = [['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O']]
rotate_matrix(alphabetical_matrix)