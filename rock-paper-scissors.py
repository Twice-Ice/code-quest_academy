import os
numOfCases = int(input())
output = []
# def ruleCheck(currentWinner, currentTest):
# 	loseRules = {'R':'P', 'S':'R', 'P':'S'}
# 	winRules =  {'R':'S', 'S':'P', 'P':'R'}
# 	convert =   {"R":"ROCK", "S":"SCISSORS", "P":"PAPER"} 
# 	if loseRules[currentWinner] == currentTest:
# 		return [currentTest, convert[currentTest]] 
# 	elif winRules[currentWinner] == currentTest:
# 		return [currentWinner, convert[currentWinner]]
# 	elif currentWinner == currentTest:
# 		return [currentTest, "NO WINNER"]
# for currentCase in range(numOfCases):
# 	case = input().split(" ")
# 	currentWinner = case[0]
# 	for i in range(len(case)):
# 		localWinner = ruleCheck(currentWinner, case[i])
# 		currentWinner = localWinner[0]
# 		if i == len(case) - 1:
# 			output.append(localWinner[1])

for case in range(numOfCases):
	game = input()
	rocks = 0
	papers = 0
	scissors = 0
	try:
		rocks = game.index("R")
	except:
		pass
	try:
		papers = game.index("P")
	except:
		pass
	try:
		scissors = game.index("S")
	except:
		pass

	if rocks == papers == scissors:
		output.append("NO WINNER")

# os.system("cls")
for i in range(len(output)):
	print(i, output[i])

"""
	R v R Done
	R v P Done
	R v S

	P v P Done
	P v S Done
	P v R
	
	S v S Done
	S v R Done
	S v P
"""