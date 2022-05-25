from celestial_bodies import *

Stars = [
        
       #Star(name ,  x_position,  y_position,  mass          ,  radius  ,  temperature  )
        Star('sun',  WIDTH / 2 ,  HEIGHT / 2,  1.989 * 10**30,  69630.40,  'temperature'),
        ]

sun = Stars[0]

Planets = [
       #Planet(name     ,  star,  distance_from_star,  color ,  mass          ,  radius)
        Planet('mercury',  sun ,  0.387 * AU        ,  GREY  ,  3.285 * 10**23,  243.9),
        Planet('venus'  ,  sun ,  0.723 * AU        ,  ORANGE,  4.867 * 10**24,  605.2),
        Planet('earth'  ,  sun ,  1.000 * AU        ,  BLUE  ,  5.972 * 10**24,  637.8),
        Planet('mars'   ,  sun ,  1.524 * AU        ,  RED   ,  6.391 * 10**23,  339.6),
        ]

mercury = Planets[0]
venus = Planets[1]
earth = Planets[2]
mars = Planets[3]

Moons = [
        
        ]

Asteroids = [
        
        ]

mercury.vel_y = 47.400 * 1000
venus.vel_y   = 35.020 * 1000
earth.vel_y   = 29.783 * 1000 
mars.vel_y    = 24.077 * 1000

CelestialBodies = Stars + Planets + Moons + Asteroids

