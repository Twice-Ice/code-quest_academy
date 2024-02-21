output = []
for i in range(int(input())):
    case = input().split(" ")
    if case[0] == "true" and case[1] == "true":
        output.append("true")
    else:
        output.append("false")
#\nResults:\n
print(f"{"\n".join(output).strip()}")