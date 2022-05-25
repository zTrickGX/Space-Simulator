import sys
from settings import *
from time import sleep
from ui import Ui 

def zoom_in():
    global SCALE
    SCALE *= 1.1

def zoom_out():
    global SCALE
    SCALE /= 1.1

def move_up():
    for body in CelestialBodies:
        body.y_position -= 2000000000
        body.orbit = [(p[0], p[1] - 2000000000) for p in body.orbit]

def move_down():
    for body in CelestialBodies:
        body.y_position += 2000000000
        body.orbit = [(p[0], p[1] + 2000000000) for p in body.orbit]

def move_left():
    for body in CelestialBodies:
        body.x_position -= 2000000000
        body.orbit = [(p[0] - 2000000000, p[1]) for p in body.orbit]

def move_right():
    for body in CelestialBodies:
        body.x_position += 2000000000
        body.orbit = [(p[0] + 2000000000, p[1]) for p in body.orbit]

def inputs():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        zoom_in()
    if keys[pygame.K_LCTRL] :
        zoom_out()
    
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        move_up()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        move_down()
        
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move_left()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move_right()


def main():
    pygame.display.set_caption("Pygame Space Simulator")
            
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    
    BG_IMAGE = pygame.image.load("space.jpg")
    
    clock = pygame.time.Clock()	
    ui = Ui(zoom_in, zoom_out)
    
    while True:
        clock.tick(FPS) 
        WINDOW.blit(BG_IMAGE, (0,0))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()	
        
        for body in CelestialBodies:
            body.update_position(CelestialBodies)
            body.custom_draw(WINDOW, SCALE)
        
        inputs()
        Ui.display(ui)
        
        pygame.display.update()
        
def exit():
    pygame.quit()
    sys.exit()

main()