import math
from costants import *

def speed_up():
    global TIME
    if TIME < MAX_TIME:
        TIME += 180

def slow_down():
    global TIME
    if TIME > MIN_TIME:
        TIME -= 180

def zoom_in():
    global SCALE, ALT_SCALE
    if SCALE < MAX_SCALE:
        SCALE *= 1.05
        ALT_SCALE /= 1.05

def zoom_out():
    global SCALE, ALT_SCALE
    if SCALE > MIN_SCALE:
        SCALE /= 1.05
        ALT_SCALE *= 1.05

def move_down(CelestialBodies):
    for body in CelestialBodies:
        body.y  -= MOVEMENT * (ALT_SCALE / X)
        body.orbit = [(p[0], p[1] - MOVEMENT * (ALT_SCALE / X)) for p in body.orbit]

def move_up(CelestialBodies):
    for body in CelestialBodies:
        body.y  += MOVEMENT * (ALT_SCALE / X)
        body.orbit = [(p[0], p[1] + MOVEMENT * (ALT_SCALE / X)) for p in body.orbit]

def move_right(CelestialBodies):
    for body in CelestialBodies:
        body.x  -= MOVEMENT * (ALT_SCALE / X)
        body.orbit = [(p[0] - MOVEMENT * (ALT_SCALE / X), p[1]) for p in body.orbit]
        
def move_left(CelestialBodies):
    for body in CelestialBodies:
        body.x += MOVEMENT * (ALT_SCALE / X)
        body.orbit = [(p[0] + MOVEMENT * (ALT_SCALE / X), p[1]) for p in body.orbit]

def show_data(data, y_offset = 0):
    display_surface = pygame.display.get_surface()
    surf = FONT.render(data, True, 'White')
    rect = surf.get_rect(topleft = (80, 80 + y_offset))
    display_surface.blit(surf, rect)

class CelestialBody:
    def __init__(self, name, x, y, radius, color, mass, revolution_period):
        self.name = name
        
        self.x  = x 
        self.y  = y 
        
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.orbit = []

        self.revolution_period = revolution_period
        
        self.vel_x = 0
        self.vel_y = 0

    def custom_draw(self, win):
        x = self.x  * SCALE + WIDTH / 2
        y = self.y  * SCALE + HEIGHT / 2
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * SCALE + WIDTH / 2
                y = y * SCALE + HEIGHT / 2
                updated_points.append((x, y))
    
            pygame.draw.lines(win, self.color, False, updated_points, 1)

        if len(self.orbit) > self.revolution_period * TIME:
            self.orbit.pop(0)
            
        pygame.draw.circle(win, self.color, (x, y), self.radius * SCALE)

        name_text = FONT.render(str(self.name), 1, (255, 255, 255))
        win.blit(name_text, (x - name_text.get_width()/2, y - name_text.get_height()/2))
        
        show_data(f'Zoom: {round(SCALE / X, 3) if SCALE / X < 1 else int(SCALE / X)}')
        show_data(f'Time: {TIME / 3600 * 10}', y_offset = 20)
    
    def calculate_forces(self, body):
        distance_x = body.x - self.x 
        distance_y = body.y - self.y 
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        force = G * self.mass * body.mass / distance**2
        
        force_x = force * distance_x / distance
        force_y = force * distance_y / distance
        
        return force_x, force_y

    def update(self, bodies):
        total_force_x = 0
        total_force_y = 0
        
        for body in bodies:
            if self != body:
                force_x, force_y = self.calculate_forces(body)
                total_force_x += force_x
                total_force_y += force_y

        self.vel_x += total_force_x / self.mass * TIME
        self.vel_y += total_force_y / self.mass * TIME

        self.x += self.vel_x * TIME
        self.y += self.vel_y * TIME
        self.orbit.append((self.x , self.y ))
        
class Star(CelestialBody):
    def __init__(self, name, x , y , mass, radius, color, temperature, revolution_period):
        super().__init__(name, x , y , radius, color, mass, revolution_period)
        self.temperature = temperature
        

class Planet(CelestialBody):
    def __init__(self, name, star, distance_from_star, color, mass, radius, revolution_period):
        self.star = star
        self.x = self.star.x + distance_from_star
        self.y = self.star.y
        super().__init__(name, self.x , self.y , radius, color, mass, revolution_period)

class Moon(CelestialBody):
    def __init__(self, name, planet, distance_from_planet, color, mass, radius):
        self.planet = planet
        self.distance_from_planet = distance_from_planet
        self.x = self.planet.x + self.distance_from_planet
        self.y = self.planet.y
        self.vel_tan = 0
        super().__init__(name, self.x , self.y , radius, color, mass, 0)
    
    def update(self, *args):
        
        self.x += (self.planet.vel_x + self.vel_tan * ((self.y - self.planet.y) / self.distance_from_planet)) * TIME 
        self.y += (self.planet.vel_y + self.vel_tan * ((self.planet.x - self.x) / self.distance_from_planet)) * TIME 
        pygame.draw.line(pygame.display.get_surface(), self.color, (self.x * SCALE + WIDTH / 2, self.y * SCALE + HEIGHT / 2), (self.planet.x * SCALE + WIDTH / 2, self.planet.y * SCALE + HEIGHT / 2), 1)