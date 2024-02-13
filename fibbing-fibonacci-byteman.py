import random
numOfCases = int(input())
output = []
for i in range(numOfCases):
	case = int(input())
	# case = random.randint(0, 100)
	# print(f"case = {case}")
	fibNumOld = 0
	fibNum = 1
	if case == 0:
		output.append("TRUE")
		continue
	while case > fibNum:
		storedFibNumOld = fibNum
		fibNum = fibNumOld + fibNum
		fibNumOld = storedFibNumOld
	else:
		if fibNum == case:
			output.append("TRUE")
		else:
			output.append("FALSE")

# print("\n\n")
outputText = "\n".join(output)

print(outputText.strip())

# old = 0
# cur = 1
# while 100 > cur:
# 	storedOld = cur
# 	cur = old + cur
# 	old = storedOld
# 	print(f"num: {cur}")