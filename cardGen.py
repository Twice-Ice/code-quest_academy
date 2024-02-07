import random
cases = 5
print(cases)
cards = ["ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING"]
for i in range(cases):
	for z in range(2):
		out = ""
		for j in range(random.randint(2, 4)):
			out += str(cards[random.randint(0, 12)])
			out += "_OF_ "
		print(out)