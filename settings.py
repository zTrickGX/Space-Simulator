from celestial_bodies import *

Stars = [
        Star('sun', WIDTH / 2, HEIGHT / 4, 1.989 * 10**30, 6963.40, 'temp'),
        ]

sun = Stars[0]

Planets = [
        Planet('mercury', sun ,  579000 , GREY   , 3.285 * 10 , 243.9),#**23
        Planet('venus'  , sun , 1082000 , ORANGE , 4.867 * 10 , 605.2),#**24
        Planet('earth'  , sun , 1496000 , BLUE   , 5.972 * 10, 637.8),#**24
        Planet('mars'   , sun , 2279000 , RED    , 6.391  * 10 , 339.6),#**23
        ]

mercury = Planets[0]
venus = Planets[1]
earth = Planets[2]
mars = Planets[3]

Moons = [
        
        ]

Asteroids = [
        
        ]

CelestialBodies = Stars + Planets + Moons + Asteroids