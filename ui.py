import pygame
from costants import *

class Button():
    def __init__(self, rect, function, image):
        self.rect = rect
        self.function = function
        if image:
            self.image = pygame.image.load(image).convert_alpha()
        
    def pressed(self):
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(x, y):
                return True

class Ui():
    def __init__(self, *funcs):
        self.win = pygame.display.get_surface()
        
        self.funcs = funcs
        self.buttons = []
        
        self.zoom_in_button = Button(pygame.Rect(1310, 725, 100, 100), funcs[0], 'Assets/zoom_in.png')
        self.zoom_out_button = Button(pygame.Rect(1425, 725, 100, 100), funcs[1], 'Assets/zoom_out.png')
        
        self.buttons.append(self.zoom_in_button)
        self.buttons.append(self.zoom_out_button)
        
    def display(self):
        for button in self.buttons:
            pygame.draw.rect(self.win, UI_BG_COLOR, button.rect)
            pygame.draw.rect(self.win, UI_BORDER_COLOR, button.rect, 10)
            image_rect = button.image.get_rect()
            image_rect.center = button.rect.center
            self.win.blit(button.image, image_rect)
            if button.pressed():
                button.function()
        
        pygame.draw.rect(self.win, UI_BG_COLOR, pygame.Rect(0, 0, WIDTH, HEIGHT), 50)
        pygame.draw.rect(self.win, UI_BORDER_COLOR, pygame.Rect(0, 0, WIDTH, HEIGHT), 10)
        pygame.draw.rect(self.win, UI_BORDER_COLOR, pygame.Rect(50, 50, WIDTH - 100, HEIGHT - 100), 10)
        
        display_surface = pygame.display.get_surface()
        debug_surf = FONT.render('Use WASD or Arrow Keys to move, use SHIFT to zoom in and CTRL to zoom out or click zoom buttons.',True,'White')
        debug_rect = debug_surf.get_rect(topleft = (50, 20))
        display_surface.blit(debug_surf,debug_rect)