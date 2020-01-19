#!/usr/bin/env python3
# 1/18/2020
# Cracking the Coding Interview Question 1.6 (Strings, Arrays, Hashtables)
# String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3
# If the *compressed* string would not become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a-z).
#Other Examples: aabb = a2b2. aaaa = a4, aabc = a2b1c1, aabbbbaa = a2b4a2

def compress_string(inputString):
	print("----------")
	print("Original Input: " + inputString)
	#If the string length <= 2, then return original string 
	if len(inputString) <= 2:
		return inputString
	#If the string length <= 4 with more than 1 unique character, then return original string.
	if len(inputString) <= 4:
		unique = []
		for char in inputString:
		    if char not in unique:
		        unique.append(char)

		if len(unique) > 1:
			return inputString
		else:
			return (str(unique[0]) + str(len(unique)))
	#Start Comparing
	#A hashtable would be useful, but it will not let us know the repeat count of a duplicate character (aabbbaa = a2b3a2)
	#Create a list from the string
	inputList = list(inputString)
	compressedString = ""
	index = 0
	#Iterate over the list with a forloop.
	for i in range(0, len(inputList)):
		#Check if the first letter matches the next, if so increment index for that character.
		if (i != (len(inputList)-1)) and (inputList[i] == inputList[i+1]):
			index += 1
			print("Index " + str(index))
			print("char " + inputList[i])
		#If the first letter does NOT match the next, start new index count for the new character found.
		else:
			index += 1
			print("Index " + str(index))
			print("char " + inputList[i])
			#Take the first character with its index and concatinate this to a new *Compressed* string variable
			compressedString = compressedString +  (str(inputList[i]) + str(index))
			index = 0
			print(compressedString)
			print("---")
    #Unfortunately, if most or all the characters are unique, then the compressedString will be longer :'(
	if len(compressedString) < len(inputString):
		return compressedString
	else:
		return inputString

print(compress_string("aa"))
print(compress_string("ab"))
print(compress_string("aab"))
print(compress_string("abc"))
print(compress_string("aacb"))
print(compress_string("aaaa"))
print(compress_string("aabbbbbaa"))
print(compress_string("veronica"))
print(compress_string("Verronica"))