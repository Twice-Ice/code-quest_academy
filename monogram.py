output = []
for i in range(int(input())):
	for j in range(int(input())):
		name = input().split(" ")
		output.append([name[0][0], name[2][0], name[1][0]])
print("\n".join(["".join(i) for i in output]).upper().strip())