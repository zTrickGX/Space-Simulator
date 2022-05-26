import sys
from settings import *
from time import sleep
from ui import Ui 

def inputs():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        zoom_in()
    if keys[pygame.K_LCTRL] :
        zoom_out()
    
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        move_up(CelestialBodies)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        move_down(CelestialBodies)
        
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move_left(CelestialBodies)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move_right(CelestialBodies)


def main():
    pygame.display.set_caption('Pygame Space Simulator')
            
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.mixer.init()
    pygame.mixer.music.load('Assets/boundless-space.ogg')
    pygame.mixer.music.play()
    
    BG_IMAGE = pygame.image.load('Assets/space.jpg').convert_alpha()
    
    clock = pygame.time.Clock()	
    ui = Ui(zoom_in, zoom_out, move_up, move_down, move_right, move_left)
    
    while True:
        clock.tick(FPS) 
        WINDOW.blit(BG_IMAGE, (0,0))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                exit()	
        
        for body in CelestialBodies:
            body.update_position(CelestialBodies)
            body.custom_draw(WINDOW)
        
        inputs()
        Ui.display(ui)
        
        pygame.display.update()
        
def exit():
    pygame.quit()
    sys.exit()
    
if __name__ == '__main__':
    main()