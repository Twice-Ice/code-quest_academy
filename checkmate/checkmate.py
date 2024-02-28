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
					self.checkSpot(yPos - (x - xPos), x, piece)
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

	def pieceLogic(self, y, x):
		pieces = {"K" : self.king, "Q" : self.queen, "R" : self.rook, "B" : self.bishop, "N" : self.knight, "P" : self.pawn}

		try:
			pieces[self.board[y][x].upper()](y, x)
		except KeyError:
			pass

	def fillBoards(self):
		for y in range(8):
			for x in range(8):
				self.pieceLogic(y, x)

	def checkmate(self):
		ATTACKING, DEFENDING, KING = 0, 1, 2
		Y, X = 0, 1
		cases = []
		for y in range(8):
			for x in range(8):
				if self.board[y][x].upper() == "K":
					if self.board[y][x].isupper(): #white
						cases.append(self.black, #black is attacking white
						self.white, #so is white able to defend?
						[y, x])
					elif self.board[y][x].islower(): #black
						cases.append(self.white,
						self.black,
						[y, x])
		
		for case in range(len(cases)):
			attacking = cases[case][ATTACKING]
			defending = cases[case][DEFENDING]
			kingY = cases[case][KING][Y]
			kingX = cases[case][KING][X]
			attackingPieces = []
			for y in range(8):
				for x in range(8):
					pass

for _ in range(int(input())):
	board = Board("input")
	board.fillBoards()
	board.checkmate()
	board.printBoards()