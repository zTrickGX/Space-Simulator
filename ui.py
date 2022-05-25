import pygame
from costants import *

class Ui():
    def __init__(self, *funcs):
        self.win = pygame.display.get_surface()
        
        self.funcs = funcs
        self.buttons = []
        
        self.zoom_in  = pygame.Rect(1400, 700, 150, 150)
        self.zoom_out = pygame.Rect(1200, 700, 150, 150)

        self.buttons.append(self.zoom_in)
        self.buttons.append(self.zoom_out)
        

        #pointlist = ((29, 29), (29, 30), (30, 1), (30, 0))
        
    def display(self):
        x, y = pygame.mouse.get_pos()
        for i, rect in enumerate(self.buttons):
            pygame.draw.rect(self.win, UI_BG_COLOR, rect)
            pygame.draw.rect(self.win, UI_BORDER_COLOR, rect, 10)
            if pygame.mouse.get_pressed()[0]:
                if rect.collidepoint(x, y):
                    self.funcs[i]()
        
        
        pointlist = ((30, 29), (30, 30), (29, 1), (29, 0))
        pygame.draw.polygon(self.win, UI_BORDER_COLOR, pointlist)