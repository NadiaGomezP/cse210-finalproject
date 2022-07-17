from constants import *
import random, time, pygame, sys
from pygame.locals import *

from game.directing.scene_manager import SceneManager

class Draw:

    def __init__(self):
        """
        Constructs a new Director using the pygame API.
        """
        global FPS_CLOCK, DISPLAY_SURF, BASIC_FONT, BIG_FONT
        pygame.init()
        FPS_CLOCK = pygame.time.Clock()
        DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        BASIC_FONT = pygame.font.Font(FONT_FILE, FONT_SMALL)
        BIG_FONT = pygame.font.Font(FONT_FILE, FONT_LARGE)
        pygame.display.set_caption(GAME_NAME)
        self._scene_manager = SceneManager()
    
    def calculate_level_and_fall_freq(self, score):
        """
        Based on the score, return the level the player is on and
        how many seconds pass until a falling piece falls one space.
        """
        
        level = int(score / 10) + 1
        fall_freq = 0.27 - (level * 0.02)
        return level, fall_freq


    def get_new_piece(self):
        """
        return a random new piece in a random rotation and color
        """
        shape = random.choice(list(SHAPES.keys()))
        newPiece = {'shape': shape, 
                    'rotation': random.randint(0, len(SHAPES[shape]) - 1),
                    'x': int(BOARD_WIDTH / 2) - int(TEMPLATE_WIDTH / 2),
                    'y': -2, # start it above the board (i.e. less than 0)
                    'color': random.randint(0, len(COLORS)-1)}
        return newPiece


    def add_to_board(self, board, piece):
        """
        fill in the board based on piece's location, shape, and rotation
        """
        for x in range(TEMPLATE_WIDTH):
            for y in range(TEMPLATE_HEIGHT):
                if SHAPES[piece['shape']][piece['rotation']][y][x] != BLANK:
                    board[x + piece['x']][y + piece['y']] = piece['color']


    def get_blank_board(self):
        """
        create and return a new blank board data structure
        """
        board = []
        for i in range(BOARD_WIDTH):
            board.append([BLANK] * BOARD_HEIGHT)
        return board


    def is_valid_position(self, board, piece, adjX=0, adjY=0):
        """
        Return True if the piece is within the board and not colliding
        """
        for x in range(TEMPLATE_WIDTH):
            for y in range(TEMPLATE_HEIGHT):
                is_above_board = y + piece['y'] + adjY < 0
                if is_above_board or SHAPES[piece['shape']][piece['rotation']][y][x] == BLANK:
                    continue
                if not self.is_on_board(x + piece['x'] + adjX, y + piece['y'] + adjY):
                    return False
                if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                    return False
        return True


    def is_on_board(self, x, y):
        return x >= 0 and x < BOARD_WIDTH and y < BOARD_HEIGHT
    

    def remove_completed_lines(self, board):
        """
        Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
        """
        num_lines_removed = 0
        y = BOARD_HEIGHT - 1 # start y at the bottom of the board
        
        while y >= 0:
            if self.is_line_completed(board, y):
                # Remove the line and pull boxes down by one line.
                for pull_boxes_down_by_one_line in range(y, 0, -1):
                    for x in range(BOARD_WIDTH):
                        board[x][pull_boxes_down_by_one_line] = board[x][pull_boxes_down_by_one_line - 1]
                # Set very top line to blank.
                for x in range(BOARD_WIDTH):
                    board[x][0] = BLANK
                num_lines_removed += 1
                
                # Note on the next iteration of the loop, y is the same. This is so that
                # if the line that was pulled down is also complete, it will be removed.
            else:
                y -= 1 # move on to check next row up
        return num_lines_removed


    def is_line_completed(self, board, y):
        """
        Return True if the line filled with boxes with no gaps.
        """
        for x in range(BOARD_WIDTH):
            if board[x][y] == BLANK:
                return False
        return True


    def draw_single_box(self, boxx, boxy, color, pixelx=None, pixely=None):
        """
        draw a single box (each tetris piece has four boxes) at xy coordinates on the board. Or, if pixelx & pixely
        are specified, draw to the pixel coordinates stored in pixelx & pixely (this is used for the "Next" piece).
        """
        if color == BLANK:
            return
        if pixelx == None and pixely == None:
            pixelx, pixely = self.convert_to_pixel_coordinates(boxx, boxy)
        pygame.draw.rect(DISPLAY_SURF, COLORS[color], (pixelx + 1, pixely + 1, BOX_SIZE - 1, BOX_SIZE - 1))
        pygame.draw.rect(DISPLAY_SURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOX_SIZE - 4, BOX_SIZE - 4))


    def convert_to_pixel_coordinates(self, boxx, boxy):
        """
        Convert the given xy coordinates of the board to xy coordinates of the location on the screen.
        """
        return (MARGIN_WIDTH + (boxx * BOX_SIZE)), (TOP_MARGIN + (boxy * BOX_SIZE))


    def draw_tetris_game_board(self, board):
        """
        draw the border around the board
        """
        pygame.draw.rect(DISPLAY_SURF, BORDER_COLOR, (MARGIN_WIDTH - 3, TOP_MARGIN - 7, (BOARD_WIDTH * BOX_SIZE) + 8, (BOARD_HEIGHT * BOX_SIZE) + 8), 5)
        
        # fill the background of the board
        pygame.draw.rect(DISPLAY_SURF, BACK_GROUND_COLOR, (MARGIN_WIDTH, TOP_MARGIN, BOX_SIZE * BOARD_WIDTH, BOX_SIZE * BOARD_HEIGHT))

        # draw the individual boxes on the board
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                self.draw_single_box(x, y, board[x][y])


    def draw_game_board_stats(self, score, level):
        """
        draw the score text
        """
        score_format = BASIC_FONT.render('Score: %s' % score, True, TEXT_COLOR)
        score_rect = score_format.get_rect()
        score_rect.topleft = (WINDOW_WIDTH - 325, 300)
        DISPLAY_SURF.blit(score_format, score_rect)

        # draw the paused game text
        paused_game_format = BASIC_FONT.render(PAUSED_GAME, True, TEXT_COLOR)
        paused_game_rect = paused_game_format.get_rect()
        paused_game_rect.topleft = (WINDOW_WIDTH - 550, 250)
        DISPLAY_SURF.blit(paused_game_format, paused_game_rect)
        
        # draw the level text
        level_format = BASIC_FONT.render('Level: %s' % level, True, TEXT_COLOR)
        level_rect = level_format.get_rect()
        level_rect.topleft = (WINDOW_WIDTH - 325, 350)
        DISPLAY_SURF.blit(level_format, level_rect)

        move_controls_game_format = BASIC_FONT.render(LEFT_RIGHT, True, TEXT_COLOR)
        move_controls_game_rect = move_controls_game_format.get_rect()
        move_controls_game_rect.topleft = (WINDOW_WIDTH - 880, 20)
        DISPLAY_SURF.blit(move_controls_game_format, move_controls_game_rect)

        change_controls_game_format = BASIC_FONT.render(UP_CONTROL, True, TEXT_COLOR)
        change_controls_game_rect = change_controls_game_format.get_rect()
        change_controls_game_rect.topleft = (WINDOW_WIDTH - 880, 40)
        DISPLAY_SURF.blit(change_controls_game_format, change_controls_game_rect)

        down_controls_game_format = BASIC_FONT.render(DOWN_CONTROL, True, TEXT_COLOR)
        down_controls_game_rect = down_controls_game_format.get_rect()
        down_controls_game_rect.topleft = (WINDOW_WIDTH - 880, 60)
        DISPLAY_SURF.blit(down_controls_game_format, down_controls_game_rect)

        space_controls_game_format = BASIC_FONT.render(SPACE_CONTROL, True, TEXT_COLOR)
        space_controls_game_rect = space_controls_game_format.get_rect()
        space_controls_game_rect.topleft = (WINDOW_WIDTH - 880, 80)
        DISPLAY_SURF.blit(space_controls_game_format, space_controls_game_rect)


    def draw_next_tetris_piece(self, piece):
        """
        draw the "next" text
        """
        next_tetris_color = BASIC_FONT.render('Next Shape:', True, TEXT_COLOR)
        next_tetris_shape = next_tetris_color.get_rect()
        next_tetris_shape.topleft = (WINDOW_WIDTH - 325, 400)
        DISPLAY_SURF.blit(next_tetris_color, next_tetris_shape)
        # draw the "next" piece
        self.draw_tetris_piece(piece, pixelx=WINDOW_WIDTH - 230, pixely=380)
    

    def draw_tetris_piece(self, piece, pixelx=None, pixely=None):
        tetris_shape_to_draw = SHAPES[piece['shape']][piece['rotation']]
        
        if pixelx == None and pixely == None:
            # if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
            pixelx, pixely = self.convert_to_pixel_coordinates(piece['x'], piece['y'])
            
        # draw each of the blocks that make up the piece
        for x in range(TEMPLATE_WIDTH):
            for y in range(TEMPLATE_HEIGHT):
                if tetris_shape_to_draw[y][x] != BLANK:
                    self.draw_single_box(None, None, piece['color'], pixelx + (x * BOX_SIZE), pixely + (y * BOX_SIZE))