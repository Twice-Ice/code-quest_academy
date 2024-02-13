numOfCases = int(input())
output = [[] for case in range(numOfCases)]
for i in range(numOfCases):
	case = int(input())
	for j in range((2**case)+1):
		output[i].append = bin(j)

for i in range(len(output)):
	for j in range(len(output[i])):
		print(output[i][j])