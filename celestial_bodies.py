import math
import pygame
from costants import *
pygame.init()

FONT = pygame.font.Font(None, 40)

class CelestialBody():
    def __init__(self, name, x_position, y_position, color, mass, radius):
        super().__init__()
        self.name = name
        
        self.x_position = x_position
        self.y_position = y_position
        
        self.mass = mass
        
        self.radius = math.sqrt(radius) / SCALE
        
        self.color = color
        
        self.vel_x = 0
        self.vel_y = 0
        
    def custom_draw(self):
        WINDOW = pygame.display.get_surface()
        celestial_body = pygame.draw.circle(WINDOW, self.color, (self.x_position, self.y_position), self.radius)
        
        name_surf = FONT.render(str(self.name),True,'Black')
        name_rect = name_surf.get_rect(topleft = (celestial_body.center[0] - (name_surf.get_width() / 2), (celestial_body.center[1] + (self.radius))))

        WINDOW.blit(name_surf,name_rect)
        
    def calculate_forces(self, body):
        distance_x = body.x_position - self.x_position
        distance_y = body.y_position - self.y_position
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        
        force = GRAVITY * self.mass * body.mass / distance ** 2
        
        force_x = force * distance_x / distance
        force_y = force * distance_y / distance

        return force_x, force_y
    
    def position_update(self, CelestialBodies):
        if self.name != 'sun':
            total_force_x = 0
            total_force_y = 0

            for body in CelestialBodies:
                if self != body:
                    force_x, force_y = self.calculate_forces(body)

                    total_force_x += force_x
                    total_force_y += force_y

            self.vel_x += total_force_x / self.mass * TIME
            self.vel_y += total_force_y / self.mass * TIME
            
            self.x_position += self.vel_x * TIME if 0 == 1 else 1
            self.y_position += self.vel_y * TIME if 0 == 1 else 1
        
            
class Star(CelestialBody):
    def __init__(self, name, x_position, y_position, mass, radius, temperature):
        super().__init__(name, x_position, y_position, YELLOW, mass, radius)
        self.temperature = temperature
        

class Planet(CelestialBody):
    def __init__(self, name, star, distance_from_star, color, mass, radius):
        self.x_position = star.x_position + math.sqrt(distance_from_star) / SCALE
        self.y_position = star.y_position
        super().__init__(name, self.x_position, self.y_position, color, mass, radius)
        self.star = star
 