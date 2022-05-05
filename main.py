import sys
from settings import *
from time import sleep

def main():
    pygame.display.set_caption("Pygame Space Simulator")
            
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    
    bg_image = pygame.image.load("space.jpg")
    WINDOW.blit(bg_image, (0,0))

    clock = pygame.time.Clock()	
    
    while True:
        clock.tick(60) 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()	
        
        for body in CelestialBodies:
            body.position_update(CelestialBodies)
            body.custom_draw()
            
        pygame.display.update()
        
def exit():
    pygame.quit()
    sys.exit()

main() if __name__ == "__main__" else None # :)