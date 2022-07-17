# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
from turtle import down


GAME_NAME = "Tetris"

# DIALOG
PRESS_START = "PRESS ANY KEY TO START"
LEFT_RIGHT = "Press LEFT or RIGHT ARROW to move"
DOWN_CONTROL = "Press DOWN ARROW to hurry the falling piece"
UP_CONTROL = "Press UP ARROW to change the direction of the piece"
SPACE_CONTROL = "Press SPACE to let the piece immediately fall"
PAUSED_GAME = "Press P to pause game"
GAME_PAUSED = "PAUSED"
PRESS_CONTINUE = "Press A to continue"
GAME_OVER = "GAME OVER"

FPS = 25 # FRAME RATE

# SCREEN
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 720
BOX_SIZE = 20
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLANK = '.'

# FRAME RATE MOVEMENT - HOLDING DOWN KEYS
MOVE_SIDE_WAYS_FREQ = 0.15
MOVE_DOWN_FREQ = 0.1

# PADDING LEFT, RIGHT, and TOP
MARGIN_WIDTH = int((WINDOW_WIDTH - BOARD_WIDTH * BOX_SIZE) / 2)
TOP_MARGIN = WINDOW_HEIGHT - (BOARD_HEIGHT * BOX_SIZE) - 5

# COLORS        R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
LIGHTPINK   = (255, 98, 255)
PINK        = (255, 172, 255)
LIGHTPURPLE = (107, 29, 230)
PURPLE      = (169, 91, 248)
BLUE        = (25, 98, 255)
LIGHTBLUE   = (25, 176, 255)
AQUA      = (52, 217, 164)
LIGHTAQUA = (57, 201, 164)

# BOARD GAME COLORS
BORDER_COLOR = (238, 177, 164)
BACK_GROUND_COLOR = BLACK
TEXT_COLOR = WHITE
TEXT_SHADOW_COLOR = GRAY
COLORS      = (     BLUE,      PURPLE,      PINK,      AQUA)
LIGHTCOLORS = (LIGHTBLUE, LIGHTPURPLE, LIGHTPINK, LIGHTAQUA)
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color


# FONT
FONT_FILE = "tetris/assets/fonts/BigJano.ttf"
FONT_SMALL = 18
FONT_LARGE = 100

# ********* TEXT *********
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# ********* KEYS *********
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# ********* SCENES *********
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER_SCENE = 4

# ********* LEVELS *********
BASE_LEVELS = 5


# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# ********* PHASES *********
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6


# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# ********* STATS *********
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# ********* HUD *********
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# TETRIS SIZE
TEMPLATE_WIDTH = 5
TEMPLATE_HEIGHT = 5

# TETRIS - GEOMETRIC SHAPES (composed of four squares, connected orthogonally.)
S_SHAPE_TETRIS = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]


Z_SHAPE_TETRIS = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]


I_SHAPE_TETRIS = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]


O_SHAPE_TETRIS = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]


J_SHAPE_TETRIS = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]


L_SHAPE_TETRIS = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]


T_SHAPE_TETRIS = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]


SHAPES = {'S': S_SHAPE_TETRIS, 
          'Z': Z_SHAPE_TETRIS,
          'J': J_SHAPE_TETRIS,
          'L': L_SHAPE_TETRIS,
          'I': I_SHAPE_TETRIS,
          'O': O_SHAPE_TETRIS,
          'T': T_SHAPE_TETRIS}
