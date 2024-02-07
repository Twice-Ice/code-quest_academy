NumOfCases = int(input())
output = [[0, 0] for i in range(NumOfCases)]

def calculateValues(hand, n, player):
	global output
	playerDealer = 0
	if not player: playerDealer = 1

	for i in range(len(hand)):
		hand[i] = hand[i].split("_OF_")[0]
		try:
			output[n][playerDealer] += int(hand[i])
		except:
			if hand[i] == "JACK" or hand[i] == "QUEEN" or hand[i] == "KING":
				output[n][playerDealer] += 10
			elif hand[i] == "ACE":
				continue

	for i in range(len(hand)):
		if hand[i] == "ACE":
			if output[n][playerDealer] + 11 > 21:
				output[n][playerDealer] += 1
			else:
				output[n][playerDealer] += 11  


for n in range(NumOfCases):
	calculateValues(input().split(" "), n, True)  #Player
	
	calculateValues(input().split(" "), n, False) #Dealer

for n in range(len(output)):
	def distTo21(num):
		return 21 - num

	wl = ""			  # win/loss
	ps = distTo21(output[n][0]) # player distance to 21
	ds = distTo21(output[n][1]) # dealer distance to 21
	
	# if ps == ds or (ps < 0 and ds < 0):
	# 	wl = "Tie"
	# elif (ps < ds and ps >= 0 and ds >= 0) or (ps > 0 and ds < 0):
	# 	wl = "Player Wins"
	# elif (ps > ds and ps >= 0 and ds >= 0) or (ps < 0 and ds > 0):
	# 	wl = "Dealer Wins"

	if ps == 0 and ds != 0: #player has blackjack and dealer doesn't
		wl = "Player Wins"
	elif ps == 0 and ds == 0: #player and dealer have blackjack
		wl = "Tie"
	elif ds < 0 and ps >= 0: #dealer busts and player doesn't
		wl = "Player Wins"
	elif ps < 0 and ds >= 0: #player busts and dealer doesn't
		wl = "Dealer Wins"
	elif ps >= 0 and ds >= 0: #if neither bust thennnn
		if ps < ds: #if the player is closer to 21
			wl = "Player Wins"
		elif ds < ps: #if the dealer is closer to 21
			wl = "Dealer Wins"
	elif ps == ds: #dealer and player have same score
		wl = "Tie"
	elif ps < 0 and ds < 0: #if both bust
		wl = "Dealer Wins"

	if wl == "":
		print("AHHHHH")

	print(f"Player Score: {output[n][0]} Dealer Score: {output[n][1]} {wl}!")
	# print(f"Player dist : {ps} Dealer Dist : {ds}")