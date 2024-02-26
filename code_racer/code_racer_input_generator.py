import random
import os

class InGen:
	def __init__(self, cases):
		self.output = ""
		# auto = False

		# if auto:
		self.auto(cases)
		# else:
			# self.manual()

		with open("code_racer/input.txt", "w") as file:
			file.write(self.output)

	def auto(self, cases):
		self.output += f"{cases}"
		for i in range(cases):
			width = random.randint(25, 30)
			length = 100#random.randint(10, 1000)
			playerPos = random.randint(1, width)
			self.output += f"\n{width} {length} {playerPos}"
			obstacleCasesNum = random.randint(width//2, width)
			self.output += f"\n{obstacleCasesNum}"
			for j in range(obstacleCasesNum):
				self.output += f"\n{random.randint(2, width)} {random.randint(1, width)}"
			player = " "
			for j in range(length):
				value = random.randint(1, 100)
				if value % 2 == 0:
					player += "L"
				else:
					player += "R"
			self.output += f"\n{player}"
		

# print(self.output)