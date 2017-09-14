import sys
import random
class Moving:

    def decide_place(self , color ,mylist , board):
        validMoves = []
        for x in range(8):
            for y in range(8):
                place = [x , y]
                if Moving.isValidMove(board, color, place) != False:
                    validMoves.append(place)
        return validMoves

    def isOntabel(place):
        return place[0] >= 0 and place[0] <= 7 and place[1] >= 0 and place[1] <= 7

    def isValidMove(self, board , color , place):
        validMoves = []
        if board[place[0]][place[1]].color != '' or not Moving.isOntabel(place):
            return False;
        if color == 'white':
            othercolor = 'black'
        else:
            othercolor = 'white'
        copyOfPlace = place
        for x , y in [ [1 , 0] , [-1 , 0] , [-1 , -1 ] , [0 , -1] , [1 , -1] , [-1 , 1] , [0 , 1] ,[1 , 1] ]:
            xstart , ystart = x , y
            copyOfPlace[0] = copyOfPlace[0] + x
            copyOfPlace[1] = copyOfPlace[1] + y
            #There is a other color here that may be earned
            if Moving.isOntabel(copyOfPlace) and board[copyOfPlace[0] , copyOfPlace[1]].color == othercolor:
                copyOfPlace[0] = copyOfPlace[0] + x
                copyOfPlace[1] = copyOfPlace[1] + y
                if not Moving.isOntabel(copyOfPlace):
                    continue
                while board[copyOfPlace[0] , copyOfPlace[1]].color == othercolor:
                    copyOfPlace[0] = copyOfPlace[0] + x
                    copyOfPlace[1] = copyOfPlace[1] + y
                    if not Moving.isOntabel(place):
                        break
                if not Moving.isOntabel(copyOfPlace):
                    continue
                #There is a other color here that will be earned
                if board[copyOfPlace[0] , copyOfPlace[1]].color == color:
                    while True :
                        copyOfPlace[0] = copyOfPlace[0] - x
                        copyOfPlace[1] = copyOfPlace[1] - y
                        if x == xstart and y == ystart:
                            break
                        validMoves.append(copyOfPlace)
        if len(validMoves) == 0:
            return  False
        return validMoves

    def Best_move(self , decided , board):
        pass
    