from constants import *
from pygame.locals import *
import random, time, pygame, sys

from game.directing.scene_manager import SceneManager
from game.casting.draw import Draw


class Director:
    """A person who directs the game."""

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
        self._draw = Draw()
        
    def start_game(self):
        """Starts the game. Runs the main game loop."""
        self._scene_manager.show_text_screen(GAME_NAME)
        while True: # game loop
            self._execute_actions()
            self._scene_manager.show_text_screen(GAME_OVER)

    def _execute_actions(self):
        """
        setup variables for the start of the game
        """
        board = self._draw.get_blank_board()
        last_move_down_time = time.time()
        last_move_sideways_time = time.time()
        last_fall_time = time.time()
        moving_down = False # note: there is no movingUp variable
        moving_left = False
        moving_right = False
        score = 0
        level, fall_freq = self._draw.calculate_level_and_fall_freq(score)
        
        falling_piece = self._draw.get_new_piece()
        next_piece = self._draw.get_new_piece()
        
        while True: # main game loop
            if falling_piece == None:
                # No falling piece in play, so start a new piece at the top
                falling_piece = next_piece
                next_piece = self._draw.get_new_piece()
                last_fall_time = time.time() # reset last_fall_time
                
                if not self._draw.is_valid_position(board, falling_piece):
                    return # can't fit a new piece on the board, so game over
            
            self._scene_manager._is_game_over()
            for event in pygame.event.get(): # event handling loop
                if event.type == KEYUP:
                    if (event.key == K_p):
                        # Pausing the game
                        DISPLAY_SURF.fill(BACK_GROUND_COLOR)
                        self._scene_manager.show_text_screen(GAME_PAUSED) # pause until a key press
                        last_fall_time = time.time()
                        last_move_down_time = time.time()
                        last_move_sideways_time = time.time()
                    elif (event.key == K_LEFT or event.key == K_a):
                        moving_left = False
                    elif (event.key == K_RIGHT or event.key == K_d):
                        moving_right = False
                    elif (event.key == K_DOWN or event.key == K_s):
                        moving_down = False
                elif event.type == KEYDOWN:
                    # moving the block sideways
                    if (event.key == K_LEFT or event.key == K_a) and self._draw.is_valid_position(board, falling_piece, adjX=-1):
                        falling_piece['x'] -= 1
                        moving_left = True
                        moving_right = False
                        last_move_sideways_time = time.time()
                    elif (event.key == K_RIGHT or event.key == K_d) and self._draw.is_valid_position(board, falling_piece, adjX=1):
                        falling_piece['x'] += 1
                        moving_right = True
                        moving_left = False
                        last_move_sideways_time = time.time()
                    
                    # rotating the block (if there is room to rotate)
                    elif (event.key == K_UP or event.key == K_w):
                        falling_piece['rotation'] = (falling_piece['rotation'] + 1) % len(SHAPES[falling_piece['shape']])
                        if not self._draw.is_valid_position(board, falling_piece):
                            falling_piece['rotation'] = (falling_piece['rotation'] - 1) % len(SHAPES[falling_piece['shape']])
                    elif (event.key == K_q): # rotate the other direction
                        falling_piece['rotation'] = (falling_piece['rotation'] - 1) % len(SHAPES[falling_piece['shape']])
                        if not self._draw.is_valid_position(board, falling_piece):
                            falling_piece['rotation'] = (falling_piece['rotation'] + 1) % len(SHAPES[falling_piece['shape']])
                    
                    # making the block fall faster with the down key
                    elif (event.key == K_DOWN or event.key == K_s):
                        moving_down = True
                        
                        if self._draw.is_valid_position(board, falling_piece, adjY=1):
                            falling_piece['y'] += 1
                        last_move_down_time = time.time()
                    
                    # move the current block all the way down
                    elif event.key == K_SPACE:
                        moving_down = False
                        moving_left = False
                        moving_right = False
                        for i in range(1, BOARD_HEIGHT):
                            if not self._draw.is_valid_position(board, falling_piece, adjY=i):
                                break
                        falling_piece['y'] += i - 1
            
            # handle moving the block because of user input
            if (moving_left or moving_right) and time.time() - last_move_sideways_time > MOVE_SIDE_WAYS_FREQ:
                if moving_left and self._draw.is_valid_position(board, falling_piece, adjX=-1):
                    falling_piece['x'] -= 1
                elif moving_right and self._draw.is_valid_position(board, falling_piece, adjX=1):
                    falling_piece['x'] += 1
                last_move_sideways_time = time.time()
            
            if moving_down and time.time() - last_move_down_time > MOVE_DOWN_FREQ and self._draw.is_valid_position(board, falling_piece, adjY=1):
                falling_piece['y'] += 1
                last_move_down_time = time.time()
            
            # let the piece fall if it is time to fall
            if time.time() - last_fall_time > fall_freq:
                # see if the piece has landed
                if not self._draw.is_valid_position(board, falling_piece, adjY=1):
                    # falling piece has landed, set it on the board
                    self._draw.add_to_board(board, falling_piece)
                    score += self._draw.remove_completed_lines(board)
                    level, fall_freq = self._draw.calculate_level_and_fall_freq(score)
                    falling_piece = None
                else:
                    # piece did not land, just move the block down
                    falling_piece['y'] += 1
                    last_fall_time = time.time()
            
            # drawing everything on the screen
            DISPLAY_SURF.fill(BACK_GROUND_COLOR)
            self._draw.draw_tetris_game_board(board)
            self._draw.draw_game_board_stats(score, level)
            self._draw.draw_next_tetris_piece(next_piece)
            
            if falling_piece != None:
                self._draw.draw_tetris_piece(falling_piece)
            
            pygame.display.update()
            FPS_CLOCK.tick(FPS)  
