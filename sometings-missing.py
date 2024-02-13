numOfCases = int(input())
output = []

EXPECTED_OUTPUT = "uppy\nkittn\nfsh\ndo"

for i in range(numOfCases):
	case = input().split(" ")
	word = [*case[0]]
	letter = int(case[1])
	word.remove(word[letter])
	output.append("".join(word).strip())

finalOutput = "\n".join(output)

print(finalOutput.strip())

# for i in range(len(output)):
# 	print(output[i].strip())