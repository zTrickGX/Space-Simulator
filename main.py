import sys
from settings import *
from time import sleep

debug = True

def main():
    pygame.display.set_caption("Pygame Space Simulator")
            
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    BG_IMAGE = pygame.image.load("space.jpg")
    
    clock = pygame.time.Clock()	
    
    WINDOW.blit(BG_IMAGE, (0,0))
    while True:
        clock.tick(60) 
        WINDOW.fill((0, 0, 0))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()	
        
        for body in CelestialBodies:
            body.custom_draw()
            body.position_update(CelestialBodies)
            if debug and body.name != 'sun':
                print(body.name)
                print(body.x_position, body.y_position)
                print(body.vel_x, body.vel_y)
                print('\n')
        
        pygame.display.update()
        
def exit():
    pygame.quit()
    sys.exit()

main() if __name__ == "__main__" else None