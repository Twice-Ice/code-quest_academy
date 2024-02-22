from string import ascii_uppercase as ALPHABET
#ascii_uppercase is the alphabet

output : "list[str]" = []
#declares output as a list of strings specifically

for i in range(int(input())):
	encrypted = input()
	decrypted = ""
	values = [int(value) for value in input().split(" ")]
	#For every value in input, convert to int

	goingRight = [value == "1" for value in input().split(" ")]
	#For every value in input, if it equals one, append true, else false
	
	indexOffset = 0

	for pos in range(len(encrypted)):
		offsetNum = (pos-indexOffset)%len(values)
		#The number that you're offsetting. indexOffset is so that it doesn't increase when we're handling special characters. Modding it by len(values) makes sure theres no indexOutOfBounds error

		dirNum = (pos-indexOffset)%len(goingRight)
		#Same as line 20, but with goingRight instead of values

		try:
			currentPos = ALPHABET.index(encrypted[pos])
			#try to get the index of the currentcharacter
		except ValueError: #If character is not a standrard alphabetic character
			decrypted += encrypted[pos]
			#just add the special character to decrypted
			indexOffset += 1
			#Make sure that we don't keep cycling through offsets when we're doing special characters
			continue
		offset = -values[offsetNum] if goingRight[dirNum] else values[offsetNum]
		#subtract offset to undo the right shift if we are going right, if not going right, ADD offset to undo leftwards shift

		offsetCharacter = ALPHABET[(currentPos + offset)%26]
		#Alphabet at position, mod to make sure theres no indexOutOfBounds exception

		decrypted += offsetCharacter


	output.append(decrypted)
print("\n".join(output).lower().strip())
#Convert to lowercase, format to be seperated by newlines, strip of any trailing or leading whitespace