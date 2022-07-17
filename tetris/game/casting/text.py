from constants import const
import pygame
from pygame.locals import *
from game.services.key_board_services import KeyboadServices


class Text:
    """A text message."""

    def __init__(self):
        """Constructs a new Text."""
        pass
    
    def makeTextObjs(self, text, font, color):
        surf = font.render(text, True, color)
        return surf, surf.get_rect()

    def showTextScreen(self, text):
        """
        This function displays large text in the
        center of the screen until a key is pressed.
        Draw the text drop shadow
        """
        titleSurf, titleRect = self.makeTextObjs(text, const.BIGFONT, const.TEXTSHADOWCOLOR)
        titleRect.center = (int(const.WINDOWWIDTH / 2), int(const.WINDOWHEIGHT / 2))
        const.DISPLAYSURF.blit(titleSurf, titleRect)
        
        # Draw the text
        titleSurf, titleRect = self.makeTextObjs(text, const.BIGFONT, const.TEXTCOLOR)
        titleRect.center = (int(const.WINDOWWIDTH / 2) - 3, int(const.WINDOWHEIGHT / 2) - 3)
        const.DISPLAYSURF.blit(titleSurf, titleRect)
        
        # Draw the additional "Press a key to play." text.
        pressKeySurf, pressKeyRect = self.makeTextObjs('Press a key to play.', const.BASICFONT, const.TEXTCOLOR)
        pressKeyRect.center = (int(const.WINDOWWIDTH / 2), int(const.WINDOWHEIGHT / 2) + 100)
        const.DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
        
        while KeyboadServices.checkForKeyPress() == None:
            pygame.display.update()
            const.FPSCLOCK.tick()
    
    