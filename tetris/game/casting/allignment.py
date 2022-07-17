from constants import *
from game.casting.complete_lines import CompleteLines

class Allignment(CompleteLines):
    """
    This class is for checking complete lines in the game and eliminating the blocks that are full
    """
    
    def __init__(self):
        """
        Instantiating and taking from the parent class 
        """
        super().__init__()

    def isCompleteLine(self, board, y):
        """
        Return True if the line filled with boxes with no gaps.
        """
        for x in range(BOARD_WIDTH):
            if board[x][y] == BLANK:
                return False
        return True


    def removeCompleteLines(self, board):
        """
        Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
        """  
        numLinesRemoved = 0
        y = BOARD_HEIGHT - 1 # start y at the bottom of the board
        
        while y >= 0:
            if self.isCompleteLine(board, y):
                # Remove the line and pull boxes down by one line.
                for pullDownY in range(y, 0, -1):
                    for x in range(BOARD_WIDTH):
                        board[x][pullDownY] = board[x][pullDownY-1]
                # Set very top line to blank.
                for x in range(BOARD_WIDTH):
                    board[x][0] = BLANK
                numLinesRemoved += 1
                            
                # Note on the next iteration of the loop, y is the same.
                # This is so that if the line that was pulled down is also
                # complete, it will be removed.
            else:
                y -= 1 # move on to check next row up
        return numLinesRemoved


    def convertToPixelCoords(boxx, boxy):
        """
        Convert the given xy coordinates of the board to xy
        coordinates of the location on the screen.
        """
        return ((boxx * BOX_SIZE)), ((boxy * BOX_SIZE))

    def isValidPosition(self, board, piece, adjX=0, adjY=0):
        """
        Return True if the piece is within the board and not colliding
        """
        for x in range(TEMPLATE_WIDTH):
            for y in range(TEMPLATE_HEIGHT):
                isAboveBoard = y + piece['y'] + adjY < 0
                if isAboveBoard or SHAPES[piece['shape']][piece['rotation']][y][x] == BLANK:
                    continue
                if not self.isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                    return False
                if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                    return False
        return True
    
    def isOnBoard(self, x, y):
        return x >= 0 and x < BOARD_WIDTH and y < BOARD_HEIGHT
