import pygame, sys
from constants import *
from pygame.locals import *


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    def __init__(self):
        """
        Constructs a new SceneManager using the pygame API.
        """
        self._is_game_paused = False
        global FPS_CLOCK, DISPLAY_SURF, BASIC_FONT, BIG_FONT
        pygame.init()
        FPS_CLOCK = pygame.time.Clock()
        DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        BASIC_FONT = pygame.font.Font(FONT_FILE, FONT_SMALL)
        BIG_FONT = pygame.font.Font(FONT_FILE, FONT_LARGE)
        pygame.display.set_caption("TETRIS - NADIA PERALTA DIAZ")


    def show_text_screen(self, text):
        """
        This function displays large text in the center of the screen until a key is pressed.
        """
        # Draw the text drop shadow
        title_surf, title_rect = self._render_text_objs(text, BIG_FONT, TEXT_SHADOW_COLOR)
        title_rect.center = (int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2))
        DISPLAY_SURF.blit(title_surf, title_rect)
        
        # Draw the text
        title_surf, title_rect = self._render_text_objs(text, BIG_FONT, TEXT_COLOR)
        title_rect.center = (int(WINDOW_WIDTH / 2) - 3, int(WINDOW_HEIGHT / 2) - 3)
        DISPLAY_SURF.blit(title_surf, title_rect)
        
        if(text != GAME_PAUSED):
            display_text = PRESS_START
        else:
            display_text = PRESS_CONTINUE
        
        # Draw the additional "PRESS A KEY TO START" text or "PRESS A KEY TO CONTINUE" text.
        press_key_surf, press_key_rect = self._render_text_objs(display_text, BASIC_FONT, TEXT_COLOR)
        press_key_rect.center = (int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2) + 100)
        DISPLAY_SURF.blit(press_key_surf, press_key_rect)
        
        while self._handle_key_press() == None:
            pygame.display.update()
            FPS_CLOCK.tick()
    
    def _render_text_objs(self, text, font, color):
        surf = font.render(text, True, color)
        return surf, surf.get_rect()

    def _handle_key_press(self):
        # Go through event queue looking for a KEYUP event.
        # Grab KEYDOWN events to remove them from the event queue.
        self._is_game_over()
        for event in pygame.event.get([KEYDOWN, KEYUP]):
            if event.type == KEYDOWN:
                continue
            return event.key
        return None
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    def _is_game_over(self):
        for event in pygame.event.get(QUIT): # get all the QUIT events
            self._terminate() # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                self._terminate() # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event) # put the other KEYUP event objects back

    def _terminate(self):
        pygame.quit()
        sys.exit()
