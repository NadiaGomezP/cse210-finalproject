import pygame
from pygame.locals import *


class KeyboadServices:
    """
    This class is for the mechanics of the keyboard and the game
    """
    def __init__(self):
        pass

    def checkForKeyPress():
        """
        Go through event queue looking for a KEYUP event.
        Grab KEYDOWN events to remove them from the event queue.
        """
        #checkForQuit()
        for event in pygame.event.get([KEYDOWN, KEYUP]):
            if event.type == KEYDOWN:
                continue
            return event.key
        return None