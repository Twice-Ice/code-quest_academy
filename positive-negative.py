numOfCases = int(input())
output = []
for i in range(numOfCases):
	case = int(input())
	if case > 0: output.append("POSITIVE")
	elif case < 0: output.append("NEGATIVE")
for i in range(len(output)):
	print(output[i])