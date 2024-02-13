numOfCases = int(input())
output = []
for case in range(numOfCases):
	output.append(input() [::-1])
for case in range(numOfCases):
	print(output[case])