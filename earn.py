
EMPTY, BLACK, WHITE, OUTER = '.', 'B', 'W', "@"
def squares():
    return [i for i in xrange(11, 89) if 1 <= (i % 10) <= 8]

def NEW_board():
    board = [OUTER] * 100
    for i in squares():
        board[i] = EMPTY
#The middle four squares
    board[44], board[45] = WHITE, BLACK
    board[54], board[55] = BLACK, WHITE
    return board
# def printf_board(board):
#     for row in xrange(0,100 ):
#         # if (row % 10 == 0) :
#         #     print '\n'
#         print ( '%s ' % board[row])
def Board(board):
    rep = ''
    rep += '  %s\n' % ' '.join([OUTER]*8)
    for row in xrange(1, 9):
        begin, end = 10*row + 1, 10*row + 9
        rep += '%s %s %s \n' % (OUTER, ' '.join(board[begin:end] ),OUTER)
        if  (row == 8 ) :
            rep += '  %s\n' % ' '.join([OUTER] * 8)
    return rep
print (Board(NEW_board()))