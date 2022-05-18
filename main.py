import sys
from settings import *
from time import sleep

def main():
    pygame.display.set_caption("Pygame Space Simulator")
            
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    
    BG_IMAGE = pygame.image.load("space.jpg")
    
    clock = pygame.time.Clock()	
    
    while True:
        clock.tick(60) 
        WINDOW.blit(BG_IMAGE, (0,0))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()	
        
        for body in CelestialBodies:
            body.inputs(CelestialBodies)
            body.update_position(CelestialBodies)
            body.custom_draw(WINDOW)
        
        pygame.display.update()
        
def exit():
    pygame.quit()
    sys.exit()

main()