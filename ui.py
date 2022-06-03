from inspect import signature
from costants import *
from settings import CelestialBodies

class Button():
    def __init__(self, rect, function, image = None):
        self.rect = rect
        self.function = function
        try:
            self.image = pygame.image.load(image).convert_alpha()
        except: 
            self.image = None
            
    def pressed(self):
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(x, y):
                return True

class Ui():
    def __init__(self, *funcs):
        self.win = pygame.display.get_surface()
        
        self.funcs = funcs
        
        self.zoom_in_button = Button(pygame.Rect(1340, 740, 80, 80), self.funcs[0], image = 'Assets/zoom_in.png')
        self.zoom_out_button = Button(pygame.Rect(1440, 740, 80, 80), self.funcs[1], image = 'Assets/zoom_out.png')
        
        self.move_up_button = Button(pygame.Rect(WIDTH / 2, 640, 80, 80), self.funcs[2], image = 'Assets/arrow_up.png')
        self.move_down_button = Button(pygame.Rect(WIDTH / 2, 740, 80, 80), self.funcs[3], image = 'Assets/arrow_down.png')
        self.move_right_button = Button(pygame.Rect(WIDTH / 2 + 100, 740, 80, 80), self.funcs[4], image = 'Assets/arrow_right.png')
        self.move_left_button = Button(pygame.Rect(WIDTH / 2 - 100, 740, 80, 80), self.funcs[5], image = 'Assets/arrow_left.png')
        
        self.speed_up_button = Button(pygame.Rect(180, 740, 80, 80), self.funcs[6])
        self.speed_down_button = Button(pygame.Rect(80, 740, 80, 80), self.funcs[7])
        
        self.buttons = [
                        self.zoom_in_button, 
                        self.zoom_out_button, 
                        self.move_up_button, 
                        self.move_down_button, 
                        self.move_right_button, 
                        self.move_left_button,
                        self.speed_up_button,
                        self.speed_down_button
                        ]
        
    def display(self):
        for button in self.buttons:
            pygame.draw.rect(self.win, UI_BG_COLOR, button.rect)
            if button.image:
                image_rect = button.image.get_rect()
                image_rect.center = button.rect.center
                self.win.blit(button.image, image_rect)
            if button.pressed():
                if str(signature(button.function)) != '()':
                    button.function(CelestialBodies)
                else:
                    button.function()
                    
        pygame.draw.rect(self.win, UI_BG_COLOR, pygame.Rect(0, 0, WIDTH, HEIGHT), 100)
        
        pygame.draw.line(self.win, UI_BORDER_COLOR, (0, 5), (WIDTH, 5),  20)
        pygame.draw.line(self.win, UI_BORDER_COLOR, (5, 0), (5, HEIGHT), 20)
        pygame.draw.line(self.win, UI_BORDER_COLOR, (WIDTH - 5, 0),  (WIDTH - 5, HEIGHT),  20)
        pygame.draw.line(self.win, UI_BORDER_COLOR, (0, HEIGHT - 5), (WIDTH, HEIGHT - 5), 20)
                                
        pygame.draw.line(self.win, UI_BORDER_COLOR, (51, 58), (WIDTH - 51, 58), 15)
        pygame.draw.line(self.win, UI_BORDER_COLOR, (58, 51), ( 58, HEIGHT - 51), 15)
        pygame.draw.line(self.win, UI_BORDER_COLOR, (WIDTH - 58, 51), (WIDTH - 58, HEIGHT - 51), 15)
        pygame.draw.line(self.win, UI_BORDER_COLOR, (51, HEIGHT - 58), (WIDTH - 51, HEIGHT - 58), 15)
        
        display_surface = pygame.display.get_surface()
        debug_surf = FONT.render('Use WASD or Arrow Keys to move, use SHIFT to zoom in and CTRL to zoom out or click zoom buttons.',True,'White')
        debug_rect = debug_surf.get_rect(topleft = (50, 20))
        display_surface.blit(debug_surf,debug_rect)