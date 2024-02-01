# table = [[] for i in range(NumOfCases)]
# for i in range(NumOfCases):
#     table[i].append([int(val) for val in input().split(",")])

# for i in range(NumOfCases):
#     for j in range(len(table[i])):
#         print(table[i][j])

NumOfCases = int(input())

temp = []
for i in range(NumOfCases):
    table = []
    for j in range(3):
        table.append((input().split(",")))
    temp.append(table)


output = []

for i in range(len(temp)):
    width = int(temp[i][0][0])
    height = int(temp[i][0][1])

    r1 = int(temp[i][1][0])
    c1 = int(temp[i][1][1])

    r2 = int(temp[i][2][0])
    c2 = int(temp[i][2][1])

    # print(f"{i}, distance r: {r2 - r1}\n{i}, distance c: {c2 - c1}")

    if r2 > 0 and r2 <= width and c2 > 0 and c2 <= height and width <= 1000 and height <= 1000:
        odd1 = False
        odd2 = False

        if (r2 - r1) % 2 == 1:
            odd1 = True #is odd
        if (c2 - c1) % 2 == 1:
            odd2 = True #is odd

        # print(f"{odd1}, {r2 - r1}; {odd2}, {c2 - c1}")

        if (odd1 == True and odd2 == True) or (odd1 == False and odd2 == False):
            output.append("Yes")
        else:
            output.append("No")

for i in range(len(output)):
    print(output[i])


# for i in range(10):
#     for j in range(10):
#         print("["+str(i)+","+str(j)+"]", end = " ")
#     print()