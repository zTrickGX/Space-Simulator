import sys
from settings import *
from ui import Ui
from time import sleep
from threading import Thread

def inputs():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        zoom_in()
    if keys[pygame.K_LCTRL]:
        zoom_out()

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        move_up(CelestialBodies)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        move_down(CelestialBodies)

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move_left(CelestialBodies)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move_right(CelestialBodies)

    if keys[pygame.K_e]:
        speed_up()

    if keys[pygame.K_q]:
        slow_down()

    if keys[pygame.K_ESCAPE]:
        exit()

def main():
    pygame.display.set_caption('Pygame Space Simulator')
            
    WINDOW = pygame.display.set_mode((REAL_WIDTH, HEIGHT))

    pygame.mixer.init()
    pygame.mixer.music.load('Assets/boundless-space.ogg')
    pygame.mixer.music.play(loops = -1)
    
    BG_IMAGE = pygame.image.load('Assets/space.jpg').convert_alpha()
    image_rect = pygame.Rect(65, 65, 1475, 775)
    
    clock = pygame.time.Clock()	
    
    ui = Ui(zoom_in, zoom_out, move_up, move_down, move_right, move_left, speed_up, slow_down)
    
    while True:
        arg = None
        clock.tick(FPS) 
        WINDOW.blit(BG_IMAGE, (0,0))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if image_rect.collidepoint(event.pos):
                    if event.button == 4: zoom_in()
                    if event.button == 5: zoom_out()
                else:
                    arg = event
                
        for body in CelestialBodies:
            body.update(CelestialBodies)
            body.custom_draw(WINDOW)
        
        inputs()
        Ui.display(ui, arg)
        
        pygame.display.update()
        
def exit():
    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    main()