#!/usr/bin/env python3
# 1/--/2020
# Cracking the Coding Interview Question 1.8 (Strings, Arrays, Hashtables)
# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.

from copy import copy, deepcopy

def zero_matrix(matrix):
	squareMatrix = True
	columnsToUpdate = []
	rowsToUpdate = []
	updated_matrix = []
	numOfRows = len(matrix)
	numOfColumns = 0
	for row in matrix:
		#find the longest list to find the max column length in case the matrix is an irregular shape
		columnLength = len(row)
		if columnLength > numOfColumns:
			numOfColumns = columnLength
		if columnLength < numOfColumns:
			squareMatrix = False

	print("\n**======Start=======**")
	print("\nCurrent Matrix:")
	for row in matrix:
		print(row)

	rowIndex = 0
	# iterate through matrix, and see which rows and columns have zeros
	for row in matrix:
		print("\n-- row " + str(rowIndex) + " --")
		columnIndex = 0
		# If all columns are found to be added to the list, break and populate list with 0s
		if (len(columnsToUpdate) == numOfColumns) and squareMatrix:
			print("Break. All Columns Detected")
			updated_matrix = [[0 for i in range(numOfColumns)] for j in range(numOfRows)]
			break
		else:	
			for item in row:	
				if item == 0:
					if columnIndex not in columnsToUpdate:
						columnsToUpdate.append(columnIndex)
					if rowIndex not in rowsToUpdate:
						rowsToUpdate.append(rowIndex)
					print(str(item) + " at column " + str(columnIndex))
				columnIndex += 1
		rowIndex += 1

	# go through matrix and create updated matrix with zeros
	updated_row = []
	for row in range(0, numOfRows):
		updated_row.clear()
		for column in range(0, len(matrix[row])):
			# find if the row or column matches, and add the correct item (1 or 0) accordingly 
			if row in rowsToUpdate or column in columnsToUpdate:
				updated_row.append(0)
			else:
				updated_row.append(1)
		updated_matrix.append(deepcopy(updated_row))
		rowIndex += 1

	print("\nUpdated Matrix:")		
	for row in updated_matrix:
		print(row)

	print("\n**=======End========**")


# Test Cases
# matrix1 = [[0 , 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0]]
# zero_matrix(matrix1)
# matrix1 = [[0 , 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0]]
# zero_matrix(matrix1)
# matrix2 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
# zero_matrix(matrix2)
matrix3 = [[1, 1, 1, 1, 1], [1, 0, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
zero_matrix(matrix3)
# matrix4 = [[0, 0, 0, 0, 0], [1, 0, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
# zero_matrix(matrix4)
# matrix5 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
# zero_matrix(matrix5)
# irregular_matrix = [[1], [1, 0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1], [1, 1, 1, 1, 1]]
# zero_matrix(irregular_matrix)
# irregular_matrix = [[1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 1], [1, 1, 1, 1, 1]]
# zero_matrix(irregular_matrix)
