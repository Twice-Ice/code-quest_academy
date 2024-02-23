carPos = (0, 0)
X = 0
Y = 1

def generateMap():
    mapProperties = [int(value) for value in input().split(" ")]
    WIDTH = mapProperties[0]
    LENGTH = mapProperties[1]
    CAR_POS = mapProperties[2]
    map = []
    for l in range(LENGTH + 4):
        line = []
        for w in range(WIDTH + 2):
            if l == 0 or l == LENGTH + 4 - 1:
                line.append("=")
            elif l == 2:
                line.append("-")
            else:
                if w == 0 or w == WIDTH + 2 - 1:
                    line.append("|")
                else:
                    line.append(" ")
        map.append(line)
    map[1][CAR_POS] = "v"
    return map

def placeObstacles(map):
    cases = input()
    for case in range(int(cases)):
        DIST = 0
        XPOS = 1
        rules = [int(value) for value in input().split(" ")]

        for i in range((len(map) -4) // rules[DIST]):
            map[i * rules[DIST] + 3 + rules[DIST] - 1][rules[XPOS]] = "o"
    return map

def moveCar(map):
    carX = map[1].index("v")
    instructions = input().strip()

    map[3][carX] = "v"
    for l in range(1, len(map) - 4):
        if instructions[l - 1] == "L" and map[l + 3][carX - 1] != "|":
            carX -= 1
        elif instructions[l - 1] == "R" and map[l + 3][carX + 1] != "|":
            carX += 1
        if map[l + 3][carX] == "o":
            map[l + 3][carX] = "X"
        else:
            map[l + 3][carX] = "v" # this line of code is the problem child. IDFK WHYY AHHHHHHHHHHHHHHH

    return map

def printMap(map):
    crashed = False
    for l in range(len(map)):
        for w in range(len(map[l])):
            if crashed == False:
                print(map[l][w], end="")
        try: 
            map[l].index("X")
            print("\nYou Crashed - GAME OVER")
            crashed = True
        except:
            pass
        if crashed == False:
            print()
        if l == len(map) - 1 and crashed == False:
            print("Course Complete!")
    

for i in range(int(input())):
    map = generateMap()
    map = placeObstacles(map)
    map = moveCar(map)
    printMap(map)