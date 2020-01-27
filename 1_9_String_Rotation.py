#!/usr/bin/env python3
# 1/--/2020
# Cracking the Coding Interview Question 1.9 (Strings, Arrays, Hashtables)
# String Rotation: Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only 
# one call to isSubstring (e.g., "Waterbottle" is a rotation of "erbottlewat")

def string_rotation(s1, s2):
	print("\n**======Start=======**")
	print("String 1: " + s1)
	print("String 2: " + s2 + "\n")

	s1List = list(s1)
	alphabeticS1List = sorted(s1List)
	s2List = list(s2)
	alphabeticS2List = sorted(s2List)
	length = len(s1)

	if s1 == s2:
		print("FAIL: Strings match exactly")
	elif len(s1) != len(s2):
		print("FAIL: String lengths do not match.")
	elif alphabeticS1List != alphabeticS2List:
		print("FAIL: Strings do not contain the same characters")
	else:
		index = 1
		foundAt = 0
		# check for substring in s2
		while index < (length-1):	
			substring = s1[0:index]
			foundAt = s2.find(substring)

			if foundAt != -1:
				print("Index: " + str(index))
				print("Substring found at: " + str(foundAt))
				print("Substring: " + substring)
				index += 1		
			elif foundAt == -1:
				index -= 1
				substring = s1[0:index]
				foundAt = s2.find(substring)
				break

		s1Check = substring + s2[:foundAt]
		if s1Check == s1:
			print("\nPASS: '" + s2 + "' is a string rotation of '" + s1 + "'")
		else:
			print("\nFAIL: Does not rotate at one point.")

	print("**=======End========**")

# Test Cases
string_rotation("racecar", "racecar")
string_rotation("Allie", "Ally")
string_rotation("abcdefg", "ijklmno")
string_rotation("waterbottle", "erbottlewat")
string_rotation("abcdefg", "abcgdef")
string_rotation("12345678", "16782345")
string_rotation("catdog", "dogcat")

