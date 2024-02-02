NumOfCases = int(input())

output = []

for i in range(NumOfCases):
    stats = input().split(" ")
    bday = 0
    if stats[1] == "true":
        bday += 5
    if int(stats[0]) <= 60 + bday:
        output.append("no ticket")
    elif int(stats[0]) > 60 + bday and int(stats[0]) <= 80 + bday:
        output.append("small ticket")
    elif int(stats[0]) > 80 + bday:
        output.append("big ticket")

for i in range(len(output)):
    print(output[i])