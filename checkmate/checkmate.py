output = []

'''if on the board then the position is changed at the board.
Sign defaults to "X"
Args: board to check, y, x, sign to replace at [y][x]'''
def checkSpot(board, y, x, sign = "X"):
    if y >= 0 and y < 8 and x >= 0 and x < 8: 
        board[y][x] = sign
    return board

def generateBoard():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(".")
    return board

'''prints the board into the terminal
chords gives the x and y pos'''
def printBoard(board, chords = False):
    for y in range(8):
        for x in range(8):
            if not chords:
                print(board[y][x], end="")
            elif chords:
                print(f"{x}, {y}, {board[y][x]}")
        print()

'''prints multiple boards next to eachother with their names on top
names is an optional add on, but please keep your names to less than a length of 9.'''
def printBoards(boards, names = None):
    #generates the line of names equally spaced apart.
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

'''returns a board with the king's moves.'''
def king(badBoard, yPos, xPos):
    #checks all spots around the king
    badBoard = checkSpot(badBoard, yPos - 1, xPos - 1)
    badBoard = checkSpot(badBoard, yPos - 1, xPos )
    badBoard = checkSpot(badBoard, yPos - 1, xPos + 1)
    badBoard = checkSpot(badBoard, yPos, xPos - 1)
    badBoard = checkSpot(badBoard, yPos, xPos + 1)
    badBoard = checkSpot(badBoard, yPos + 1, xPos - 1)
    badBoard = checkSpot(badBoard, yPos + 1, xPos)
    badBoard = checkSpot(badBoard, yPos + 1, xPos + 1)

    return badBoard

'''returns a board with the rook's moves'''
def rook(board, badBoard, yPos, xPos):
    goingUp = True
    for y in range(yPos - 1, -1, -1): #range until edge of board
        if goingUp: #if the direction hasn't been interupted
            if board[y][xPos] != ".": goingUp = False #detects if the direction is interupted
            badBoard = checkSpot(badBoard, y, xPos) #changes the spot. 

    goingDown = True
    for y in range(yPos + 1, 8):
        if goingDown:
            if board[y][xPos] != ".": goingDown = False
            badBoard = checkSpot(badBoard, y, xPos)

    goingLeft = True
    for x in range(xPos - 1, -1, -1):
        if goingLeft:
            if board[yPos][x] != ".": goingLeft = False
            badBoard = checkSpot(badBoard, yPos, x)

    goingRight = True
    for x in range(xPos + 1, 8):
        if goingRight:
            if board[yPos][x] != ".": goingRight = False
            badBoard = checkSpot(badBoard, yPos, x)

    return badBoard

'''returns a board with the bishop's moves'''
def bishop(board, badBoard, yPos, xPos):
    #same logic as rook but with slightly differnt math to accound for going to the side 1 as well as up/down 1.
    goingUpLeft = True
    for x in range(xPos - 1, -1, -1):
        if goingUpLeft:
            try:
                if board[yPos - (xPos - x)][x] != ".": goingUpLeft = False
                badBoard = checkSpot(badBoard, yPos - (xPos - x), x)
            except:
                pass

    goingUpRight = True
    for x in range(xPos + 1, 8):
        if goingUpRight:
            try:
                if board[yPos - (x - xPos)][x] != ".": goingUpRight = False
                badBoard = checkSpot(badBoard, yPos - (x - xPos), x)
            except:
                pass

    goingDownLeft = True
    for x in range(xPos - 1, -1, -1):
        if goingDownLeft:
            try:
                if board[yPos + (xPos - x)][x] != ".": goingDownLeft = False 
                badBoard = checkSpot(badBoard, yPos + (xPos - x), x)
            except:
                pass

    goingDownRight = True
    for x in range(xPos + 1, 8):
        if goingDownRight:
            try:
                if board[yPos + (x - xPos)][x] != ".": goingDownRight = False
                badBoard = checkSpot(badBoard, yPos + (x - xPos), x)
            except:
                pass

    return badBoard

'''returns a board with the queen's moves'''
def queen(board, badBoard, yPos, xPos):
    #a queen's moveset is the same as a rook and bishop's combined, so it's literally just that lol.
    badBoard = rook(board, badBoard, yPos, xPos)
    badBoard = bishop(board, badBoard, yPos, xPos)

    return badBoard

'''returns a board with the kight's moves'''
def knight(badBoard, yPos, xPos):
    #similar to the king, all spots are checked where the knight moves.
    badBoard = checkSpot(badBoard, yPos + 1, xPos - 2)
    badBoard = checkSpot(badBoard, yPos - 1, xPos - 2)
    badBoard = checkSpot(badBoard, yPos + 1, xPos + 2)
    badBoard = checkSpot(badBoard, yPos - 1, xPos + 2)
    badBoard = checkSpot(badBoard, yPos - 2, xPos + 1)
    badBoard = checkSpot(badBoard, yPos - 2, xPos - 1)
    badBoard = checkSpot(badBoard, yPos + 2, xPos + 1)
    badBoard = checkSpot(badBoard, yPos + 2, xPos - 1)

    return badBoard

'''returns a board with the pawn's moves
black/white is required due to the pawn's moveset being directional, based on color
bw is black/white, input as "b" or "w"'''
def pawn(badBoard, yPos, xPos, bw):
    #determines the pawn's direction based on bw.
    if bw == "b": dir = 1
    elif bw == "w": dir = -1

    #checks the two attack spots of the pawn.
    badBoard = checkSpot(badBoard, yPos + dir, xPos - 1)
    badBoard = checkSpot(badBoard, yPos + dir, xPos + 1)

    return badBoard

def checkmate(board, badBoard, bw):
    #logic needs to be rewritten to accound for cases where the king is surrounded by attacks and enemies, but can attack those enemies.
    #The current logic doesn't account for those senarios.
    #What it should do is check each spot around the king to see if it can move there or not, and if it can't, 
    #then the attacking enemy's spot should be checked to see if it's in danger or not.
    #if it was in danger, then the king isn't completely fucked.
    #however, this rule only applies to the center of the king, not to it's other moveable/attackable locations.
    #The king can move to any spot it can attack, but if it can't do that, then it can have it's pieces attack the piece that is attacking it's location.

    '''
    psudocode:
    1. check king pos to see if it's under attack and by what it is under attack from. (the position of the attacker, not the type of piece)
    2. if the king pos is fine then return False
    3. else check each spot the king can move to for the following logic:
    4. if the spot is filled check if the spot is defended. If not, the king can move there so return False.
    5. else if it's defended, repeat step 4 for all spaces the king can move to.
    6. if the king can't move to any of the spots, then return True. The king is in checkmate.
    '''
    #define which king you're looking for
    if bw == "b":
        check = "k"
        same = 0
        opposite = 1
    elif bw == "w":
        check = "K"
        same = 1
        opposite = 0
    #gets king location
    kingX = -1
    kingY = -1
    for y in range(8):
        for x in range(8):
            if board[y][x] == check:
                kingX = x
                kingY = y
    
    #checks king's center pos
    for y in range(8):
        for x in range(8):
            boardCheck = pieceLogic(board, y, x)
            if boardCheck[opposite][kingY][kingX] == "X":
                print(f"The king ({check}) has died to the piece at {x}, {y}")

def pieceLogic(board, y, x):
    blackSpots, whiteSpots = generateBoard(), generateBoard()
    if board[y][x] == "k":
        blackSpots = king(blackSpots, y, x)
    elif board[y][x] == "K":
        whiteSpots = king(whiteSpots, y, x)
    elif board[y][x] == "q":
        blackSpots = queen(board, blackSpots, y, x)
    elif board[y][x] == "Q":
        whiteSpots = queen(board, whiteSpots, y, x)
    elif board[y][x] == "r":
        blackSpots = rook(board, blackSpots, y, x)
    elif board[y][x] == "R":
        whiteSpots = rook(board, whiteSpots, y, x)
    elif board[y][x] == "b":
        blackSpots = bishop(board, blackSpots, y, x)
    elif board[y][x] == "B":
        whiteSpots = bishop(board, whiteSpots, y, x)
    elif board[y][x] == "n":
        blackSpots = knight(blackSpots, y, x)
    elif board[y][x] == "N":
        whiteSpots = knight(whiteSpots, y, x)
    elif board[y][x] == "p":
        blackSpots = pawn(blackSpots, y, x, "b")
    elif board[y][x] == "P":
        whiteSpots = pawn(whiteSpots, y, x, "w")

    return blackSpots, whiteSpots

def gameLogic():
    board = []
    for y in range(8): #map gen
        board.append([x for x in input()])
    
    #initialized and sets up white attack board and black attack board.
    whiteSpots = generateBoard()
    blackSpots = generateBoard()

    #loops through the board and checks if a piece is there or not.
    for y in range(8):
        for x in range(8):
            if board[y][x] != ".":
                if board[y][x] == "k":
                    blackSpots = king(blackSpots, y, x)
                elif board[y][x] == "K":
                    whiteSpots = king(whiteSpots, y, x)
                elif board[y][x] == "q":
                    blackSpots = queen(board, blackSpots, y, x)
                elif board[y][x] == "Q":
                    whiteSpots = queen(board, whiteSpots, y, x)
                elif board[y][x] == "r":
                    blackSpots = rook(board, blackSpots, y, x)
                elif board[y][x] == "R":
                    whiteSpots = rook(board, whiteSpots, y, x)
                elif board[y][x] == "b":
                    blackSpots = bishop(board, blackSpots, y, x)
                elif board[y][x] == "B":
                    whiteSpots = bishop(board, whiteSpots, y, x)
                elif board[y][x] == "n":
                    blackSpots = knight(blackSpots, y, x)
                elif board[y][x] == "N":
                    whiteSpots = knight(whiteSpots, y, x)
                elif board[y][x] == "p":
                    blackSpots = pawn(blackSpots, y, x, "b")
                elif board[y][x] == "P":
                    whiteSpots = pawn(whiteSpots, y, x, "w")

    whiteWin = checkmate(board, whiteSpots, "b")
    blackWin = checkmate(board, blackSpots, "w")

    printBoards([whiteSpots, blackSpots, board], ["White", "Black", "Board"])

    return whiteWin, blackWin

'''main loop of code'''
def main():
    for _ in range(int(input())):
        whiteWin, blackWin = gameLogic()

        
        # if whiteWin:
        #     print("CHECKMATE WHITE")
        # elif blackWin:
        #     print("CHECKMATE BLACK")
        # else:
        #     print("NO CHECKMATE")

main()