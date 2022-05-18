import math
import pygame
from costants import *
pygame.init()
FONT = pygame.font.SysFont("comicsans", 16)

class CelestialBody:
    DAY = 3600*24
    SCALE = 500 / AU
    def __init__(self, name, x_position, y_position, radius, color, mass):
        self.name = name
        self.x_position = x_position
        self.y_position = y_position
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.distance_to_sun = 0

        self.vel_x = 0
        self.vel_y = 0
        

    def custom_draw(self, win):
        x = self.x_position * self.SCALE + WIDTH / 2
        y = self.y_position * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
        
        
            pygame.draw.lines(win, self.color, False, updated_points, 1)
        if len(self.orbit) > 100:
            self.orbit.pop(0)
        
        pygame.draw.circle(win, self.color, (x, y), self.radius**2 * self.SCALE)
        
        if type(self) != Star:
            name_text = FONT.render(str(self.name), 1, WHITE)
            win.blit(name_text, (x - name_text.get_width()/2, y - name_text.get_height()/2))
            
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 2)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2 + 20))
            
    def inputs(self, CelestialBodies):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.SCALE *= 1.1
        if keys[pygame.K_LCTRL] :
            self.SCALE /= 1.1
        
        if keys[pygame.K_UP]:
            for body in CelestialBodies:
                body.y_position -= 1000000000
        if keys[pygame.K_DOWN]:
            for body in CelestialBodies:
                body.y_position += 1000000000
        if keys[pygame.K_LEFT]:
            for body in CelestialBodies:
                body.x_position -= 1000000000
        if keys[pygame.K_RIGHT]:
            for body in CelestialBodies:
                body.x_position += 1000000000
        
    def calculate_forces(self, body):
        distance_x = body.x_position - self.x_position
        distance_y = body.y_position - self.y_position
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if type(body) == Star:
            self.distance_to_sun = distance

        force = G * self.mass * body.mass / distance**2
        
        force_x = force * distance_x / distance
        force_y = force * distance_y / distance
        
        return force_x, force_y

    def update_position(self, bodies):
        total_force_x = 0
        total_force_y = 0
        
        for body in bodies:
            if self != body:
                force_x, force_y = self.calculate_forces(body)
                total_force_x += force_x
                total_force_y += force_y

        self.vel_x += total_force_x / self.mass * self.DAY
        self.vel_y += total_force_y / self.mass * self.DAY

        self.x_position += self.vel_x * self.DAY
        self.y_position += self.vel_y * self.DAY
        self.orbit.append((self.x_position, self.y_position))
        
class Star(CelestialBody):
    def __init__(self, name, x_position, y_position, mass, radius, temperature):
        super().__init__(name, x_position, y_position, radius, YELLOW, mass)
        self.temperature = temperature
        

class Planet(CelestialBody):
    def __init__(self, name, star, distance_from_star, color, mass, radius):
        self.x_position = distance_from_star
        self.y_position = star.y_position
        super().__init__(name, self.x_position, self.y_position, radius, color, mass)
 