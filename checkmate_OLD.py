output = []

'''if on the board then the position is changed at the board.
Sign defaults to "X"
Args: board to check, y, x, sign to replace at [y][x]'''
def checkSpot(board, y, x, sign = "X"):
    if y >= 0 and y < 8 and x >= 0 and x < 8: 
        board[y][x] = sign
    return board

'''generates a blank board filled with "."'''
def generateBoard(pieces = []):
    X = 0
    Y = 1
    NAME = 2
    board = [["." for i in range(8)] for i in range(8)]
    for i in range(len(pieces)):
        board[pieces[i][Y]][pieces[i][X]] = pieces[i][NAME]
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

def pieceLogic(board, y, x, blackSpots = generateBoard(), whiteSpots = generateBoard()):
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

def pieceDefended(board, pieceY, pieceX, opposite):
    attackingPieces = []
    for y in range(8):
        for x in range(8):
            boardCheck = pieceLogic(board, y, x, generateBoard(), generateBoard())
            if boardCheck[opposite][pieceY][pieceX] == "X":
                attackingPieces.append([x, y])
    return attackingPieces

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

    
    pseudocode #2:
    how to check the king's surroundings:
    1. calculate all incoming attacks for all pieces.
    2. if any of the king's surroundings aren't under attack, then the king can move there and you return False.

    how to check the king's position:
    X 1. get a list of all pieces attacking the king's position
    X 2. if there are 2 or more pieces attacking the king's position, the king is in checkmate. Return True.
    X 3. if there is only one piece attacking the king's position do the following:
    X 4. check the location of the piece attacking the king, and see if that piece is under attack.
    X 5. if that piece is under attack, return False because that piece can be killed and get the king out of checkmate.
    _ 6. else: if the piece is a bishop, rook, or queen, loop through each attack position of the piece;
    _ 7. if another piece can move into the way of any of the attack positions, create a board where that is the case.
        (for each attack position, check each opposing piece to see if a piece can move there.)
    _ 8. then check the king's position to see if it's still under attack.
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
    
    X = 0
    Y = 1

    #checks king's center pos
    attacking = pieceDefended(board, kingY, kingX, opposite)
    kingExists = (kingX != -1 and kingY != -1)
    print(f"The king's position is : {kingX, kingY}." if kingExists  else "")
    if len(attacking) >= 2 and kingExists:
        print(len(attacking))
        print(f"The king ({check}) is in checkmate") #it's not actually in checkmate, you would then have to check it's surroundings.
    elif kingExists:
        defending = pieceDefended(board, attacking[0][Y], attacking[0][X], same)
        if len(defending) > 0:
            print(f"The king isn't in checkmate, and the piece at {attacking[0][X], attacking[0][Y]} has died to the piece at {defending[0][X], defending[0][Y]}")
        elif board[attacking[0][Y]][attacking[0][X]].upper() in "BRQ": #CHECKS IF COORDS ON BOARD IS ANY PIECE OTHER THAN PAWN, KING, OR KNIGHT
            currentPiece = board[attacking[0][Y]][attacking[0][X]]
            attackingBoard = board
            boards = None
            def generateFilledBoard():
                blackSpots, whiteSpots = generateBoard(), generateBoard()
                for y in range(8):
                    for x in range(8):
                        boards = pieceLogic(board, y, x, blackSpots, whiteSpots)
            for y in range(8):
                for x in range(8):
                    if boards[0][y][x] == "X" and boards[1][y][x] == "X":
                        newBoard = generateBoard([[kingX, kingY, check], [attacking[0][X], attacking[0][Y], currentPiece]])
                        # if generateFilledBoard()

            printBoards([boards[0], boards[1]], ["White", "Black"])
            # currentPiece = board[attacking[0][Y]][attacking[0][X]].upper()
            # funkyNewBoard = generateBoard()
            # if currentPiece == "R" or currentPiece == "Q":
            #     if attacking[0][X] == kingX:
            #         pieceDistance = abs(attacking[0][Y] - kingY)
            #         for i in range(pieceDistance):
            #             i = i if kingY > attacking[0][Y] else -i
            #             funkyNewBoard[attacking[0][Y] + i][kingX] = "X"
            #             print()
            #             printBoard(funkyNewBoard)

            #     if attacking[0][Y] == kingY:
            #         pieceDistance = abs(attacking[0][X] - kingX)
            #         for i in range(pieceDistance):
            #             i = i if kingX > attacking[0][X] else -i
            #             funkyNewBoard[kingY][attacking[0][X] + i] = "X"
            #             print()
            #             printBoard(funkyNewBoard)

            # elif currentPiece == "B" or currentPiece == "Q":
            #     pieceDistance = abs(attacking[0][Y] - kingY)
            #     for i in range(pieceDistance):
            #         y = i if kingY > attacking[0][Y] else -i
            #         x = i if kingX > attacking[0][X] else -i
            #         funkyNewBoard[attacking[0][Y] + y][attacking[0][X] + x] = "X"
            #     printBoard(funkyNewBoard)

            print(f"The king ({check}) has died to the piece at {attacking[0][0], attacking[0][1]}.")

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