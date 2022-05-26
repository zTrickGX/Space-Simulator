from celestial_bodies import *

Stars = [
        
       #Star(name ,  x_position,  y_position,  mass          ,  radius  ,  temperature  )
        Star('Sun',  WIDTH / 2 ,  HEIGHT / 2,  	1.988500 * 10**30, 69570.0,  'temperature'),
        ]

sun = Stars[0]

Planets = [
        Planet('Mercury', sun , 0.387  * AU, GREY  , 3.3010  * 10**23,  2440.5),
        Planet('Venus'  , sun , 0.723  * AU, ORANGE, 4.8673  * 10**24,  6051.8),
        Planet('Earth'  , sun , 1.000  * AU, BLUE  , 5.9722  * 10**24,  6378.1),
        Planet('Mars'   , sun , 1.524  * AU, RED   , 6.4169  * 10**23,  3396.2),
        Planet('Jupiter', sun , 5.203  * AU, ORANGE, 1.89813 * 10**27, 71492.0),
        Planet('Saturn' , sun , 9.539  * AU, YELLOW, 5.6832  * 10**26, 60268.0),
        Planet('Uranus' , sun , 19.191 * AU, BLUE  , 8.6811  * 10**25, 25559.0),
        Planet('Neptune', sun , 30.061 * AU, GREY  , 1.02409 * 10**26, 24764.0),
        Planet('Pluto'  , sun , 39.482 * AU, GREY  , 1.303   * 10**22,  1188.0),
        ]

mercury = Planets[0]
venus   = Planets[1]
earth   = Planets[2]
mars    = Planets[3]
jupiter = Planets[4]
saturn  = Planets[5]
uranus  = Planets[6]
neptune = Planets[7]
pluto   = Planets[8]

Moons = [
        
        ]

Asteroids = [
        
        ]

mercury.vel_y = 47.36 * 1000
venus.vel_y   = 35.02 * 1000
earth.vel_y   = 29.78 * 1000
mars.vel_y    = 24.07 * 1000
jupiter.vel_y = 13.06 * 1000
saturn.vel_y  =  9.68 * 1000
uranus.vel_y  =  6.80 * 1000
neptune.vel_y =  5.43 * 1000
pluto.vel_y   =  4.67 * 1000

CelestialBodies = Stars + Planets + Moons + Asteroids