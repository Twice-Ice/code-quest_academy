ouput = []

'''prints multiple boards next to eachother with their names on top
names is an optional add on, but please keep your names to less than a length of 9.'''

class Board:
	def __init__(self, boardType = "default", pieceList = None):
		'''generates main board with pieces on it, or blank depending on the input of boardType'''
		if boardType == "default":
			self.board = [["." for i in range(8)] for i in range(8)]
		elif boardType == "input":
			self.board = []
			for i in range(8):
				self.board.append(input())
		elif type(boardType) == list:
			self.board = boardType
		elif boardType == "pieceList":
			self.board = [["." for i in range(8)] for i in range(8)]
			Y, X, PIECE = 0, 1, 2
			for piece in range(len(pieceList)):
				self.board[pieceList[piece][Y]][pieceList[piece][X]] = pieceList[piece][PIECE]
		self.white = [["." for i in range(8)] for i in range(8)]
		self.black = [["." for i in range(8)] for i in range(8)]

	def printBoards(self,):
		#generates the line of names equally spaced apart.
		boards = [self.board, self.white, self.black]
		names = ["Board", "White", "Black"]
		if names != None:
			namesLine = ""
			for name in range(len(names)):
				namesLine += names[name]
				for i in range(8 + 2 - len(names[name])): #the + 2 is to accound for the extra distance added by separating the boards.
					namesLine += " "
			print(namesLine)
		for y in range(8):
			line = ""
			for board in range(len(boards)):
				for x in range(8):
					line += boards[board][y][x]
				line += "  "
			print(line)

	def checkSpot(self, y, x, piece = None):
		if piece == None: piece = self.board[y][x]
		if y >= 0 and y < 8 and x >= 0 and x < 8:
			if piece.isupper():
				self.white[y][x] = "X"
			elif piece.islower():
				self.black[y][x] = "X"
		return

	def king(self, y, x):
		#checks all spots around the king
		piece = self.board[y][x]
		self.checkSpot(y - 1, x - 1, piece)
		self.checkSpot(y - 1, x , piece)
		self.checkSpot(y - 1, x + 1, piece)
		self.checkSpot(y, x - 1, piece)
		self.checkSpot(y, x + 1, piece)
		self.checkSpot(y + 1, x - 1, piece)
		self.checkSpot(y + 1, x, piece)
		self.checkSpot(y + 1, x + 1, piece)

	def rook(self, yPos, xPos):
		piece = self.board[yPos][xPos]
		goingUp = True
		for y in range(yPos - 1, -1, -1): #range until edge of board
			if goingUp: #if the direction hasn't been interupted
				if self.board[y][xPos] != ".": goingUp = False #detects if the direction is interupted
				self.checkSpot(y, xPos, piece) #changes the spot. 

		goingDown = True
		for y in range(yPos + 1, 8):
			if goingDown:
				if self.board[y][xPos] != ".": goingDown = False
				self.checkSpot(y, xPos, piece)

		goingLeft = True
		for x in range(xPos - 1, -1, -1):
			if goingLeft:
				if self.board[yPos][x] != ".": goingLeft = False
				self.checkSpot(yPos, x, piece)

		goingRight = True
		for x in range(xPos + 1, 8):
			if goingRight:
				if self.board[yPos][x] != ".": goingRight = False
				self.checkSpot(yPos, x, piece)

	def bishop(self, yPos, xPos):
		#same logic as rook but with slightly differnt math to accound for going to the side 1 as well as up/down 1.
		piece = self.board[yPos][xPos]
		goingUpLeft = True
		for x in range(xPos - 1, -1, -1):
			if goingUpLeft:
				try:
					if self.board[yPos - (xPos - x)][x] != ".": goingUpLeft = False
					self.checkSpot(yPos - (xPos - x), x, piece)
				except:
					pass

		goingUpRight = True
		for x in range(xPos + 1, 8):
			if goingUpRight:
				try:
					if self.board[yPos - (x - xPos)][x] != ".": goingUpRight = False
					self.checkSpot(yPos - (x - xPos), x, piece)
				except:
					pass

		goingDownLeft = True
		for x in range(xPos - 1, -1, -1):
			if goingDownLeft:
				try:
					if self.board[yPos + (xPos - x)][x] != ".": goingDownLeft = False 
					self.checkSpot(yPos + (xPos - x), x, piece)
				except:
					pass

		goingDownRight = True
		for x in range(xPos + 1, 8):
			if goingDownRight:
				try:
					if self.board[yPos + (x - xPos)][x] != ".": goingDownRight = False
					self.checkSpot(yPos + (x - xPos), x, piece)
				except:
					pass

	def queen(self, y, x):
		self.rook(y, x)
		self.bishop(y, x)

	def knight(self, y, x):
		self.checkSpot(y + 1, x - 2)
		self.checkSpot(y - 1, x - 2)
		self.checkSpot(y + 1, x + 2)
		self.checkSpot(y - 1, x + 2)
		self.checkSpot(y - 2, x + 1)
		self.checkSpot(y - 2, x - 1)
		self.checkSpot(y + 2, x + 1)
		self.checkSpot(y + 2, x - 1)

	def pawn(self, y, x):
		if self.board[y][x].isupper():
			dir = -1
		else:
			dir = 1

		self.checkSpot(y + dir, x - 1)
		self.checkSpot(y + dir, x + 1)

	def pieceLogic(self, y, x, noKing = False):
		pieces = {"K" : self.king, "Q" : self.queen, "R" : self.rook, "B" : self.bishop, "N" : self.knight, "P" : self.pawn}

		try:
			if noKing and self.board[y][x].upper() == "K":
				pass
			else:
				pieces[self.board[y][x].upper()](y, x)
		except KeyError:
			pass

	def fillBoards(self, noKing = False):
		for y in range(8):
			for x in range(8):
				self.pieceLogic(y, x, noKing)

	def checkmate(self):
		ATTACKING, DEFENDING, KING = 0, 1, 2
		Y, X = 0, 1
		cases = []
		for y1 in range(8):
			for x1 in range(8):
				if self.board[y1][x1].upper() == "K": #finds the king
					if self.board[y1][x1].isupper(): #white king
						kingY = x1
						kingX = y1
						attackingPieces = []
						for y2 in range(8):
							for x2 in range(8): #loops through the board and finds all attacking pieces
								simulatedBoard = Board(self.board) #initalizes board with the king and the current piece at y2, x2
								attacking = simulatedBoard.black
								defending = simulatedBoard.white
								simulatedBoard.fillBoards()
								if attacking[kingY][kingX] == "X":
									attackingPieces.append([y2, x2, self.board[y2][x2]])
						if len(attackingPieces) >= 2:
							print(f"The king is being attacked by {len(attackingPieces)} pieces.")
							#next, check the suroundings to see if the king is in checkmate.
						elif len(attackingPieces) == 1:
							print(f"The king is being attacked by {len(attackingPieces)} piece.")
							simulatedBoard1 = Board("pieceList", [[kingY, kingX, self.board[kingY][kingX]], [attackingPieces[0][0], attackingPieces[0][1], attackingPieces[0][2]]])
							simulatedBoard1.fillBoards(True)
							attacking1 = simulatedBoard1.black
							defending1 = simulatedBoard1.white
							for y3 in range(8):
								for x3 in range(8):
									if attacking1[y3][x3] == "X" and defending1[y3][x3] == "X":
										simulatedBoard2 = Board("pieceList", [[kingY, kingX, self.board[kingY][kingX]], [y3, x3, "P"], [attackingPieces[0][0], attackingPieces[0][1], attackingPieces[0][2]]])
										attacking2 = simulatedBoard2.black
										defending2 = simulatedBoard2.white
										simulatedBoard2.pieceLogic(attackingPieces[0][0], attackingPieces[0][1])
										if attacking2[kingY][kingX] != "X":
											print("The king can be defended!")
							#next, check if the attacks can be blocked.
						else:
							print(f"The king is safe.")
							#return false. The king is not in checkmate.
					elif self.board[y1][x1].islower(): #black king
						pass
						# cases.append([white, black, [y, x]])

for _ in range(int(input())):
	board = Board("input")
	board.fillBoards()
	board.checkmate()
	board.printBoards()