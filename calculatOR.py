import math
numOfCases = int(input())
output = []
def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.5002 if val >= 0 else -0.5002))
    return result / 10**n_digits

def round(input):
	return better_round(input, 1)

for i in range(numOfCases):
	case = input().split(" ")
	case[0], case[2] = float(case[0]), float(case[2])
	if case[1] == "+":
		output.append(f"{round(case[0] + case[2])} {round(case[2] + case[0])}")
	elif case[1] == "-":
		output.append(f"{round(case[0] - case[2])} {round(case[2] - case[0])}")
	elif case[1] == "/":
		output.append(f"{round(case[0] / case[2])} {round(case[2] / case[0])}")
	elif case[1] == "*":
		output.append(f"{round(case[0] * case[2])} {round(case[2] * case[0])}")

print("\n".join(output).strip())