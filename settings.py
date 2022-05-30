from celestial_bodies import *

Stars = [
        Star('Sun',  WIDTH / 2 ,  HEIGHT / 2,  	1.988500 * 10**30, 69570.0, (252, 150,   1) ,'temperature', 25),
        ]

sun = Stars[0]

Planets = [
        Planet('Mercury', sun , 0.387  * AU, (177, 173, 173), 3.3010  * 10**23,  2440.5,    87),
        Planet('Venus'  , sun , 0.723  * AU, (247, 187, 118), 4.8673  * 10**24,  6051.8,   224),
        Planet('Earth'  , sun , 1.000  * AU, ( 53 ,105, 191), 5.9722  * 10**24,  6378.1,   365),
        Planet('Mars'   , sun , 1.524  * AU, (255,  77,  47), 6.4169  * 10**23,  3396.2,   687),
        Planet('Jupiter', sun , 5.203  * AU, (167, 156, 134), 1.89813 * 10**27, 71492.0,  4332),
        Planet('Saturn' , sun , 9.539  * AU, (234, 214, 184), 5.6832  * 10**26, 60268.0, 10759),
        Planet('Uranus' , sun , 19.191 * AU, (213, 251, 252), 8.6811  * 10**25, 25559.0, 30685),
        Planet('Neptune', sun , 30.061 * AU, ( 63,  84, 186), 1.02409 * 10**26, 24764.0, 60189),
        Planet('Pluto'  , sun , 39.482 * AU, (221, 196, 175), 1.303   * 10**22,  1188.0, 90560),
        ]

mercury = Planets[0]; mercury.vel_y = 47.36 * 1000; mercury.vel_x = 0
venus   = Planets[1]; venus.vel_y   = 35.02 * 1000; venus.vel_x   = 0
earth   = Planets[2]; earth.vel_y   = 29.78 * 1000; earth.vel_x   = 0
mars    = Planets[3]; mars.vel_y    = 24.07 * 1000; mars.vel_x    = 0
jupiter = Planets[4]; jupiter.vel_y = 13.06 * 1000; jupiter.vel_x = 0
saturn  = Planets[5]; saturn.vel_y  =  9.68 * 1000; saturn.vel_x  = 0
uranus  = Planets[6]; uranus.vel_y  =  6.80 * 1000; uranus.vel_x  = 0
neptune = Planets[7]; neptune.vel_y =  5.43 * 1000; neptune.vel_x = 0
pluto   = Planets[8]; pluto.vel_y   =  4.67 * 1000; pluto.vel_x   = 0

Moons = [
        Moon('Moon', earth, 0.00257 * AU, (177, 173, 173), 7.3477 * 10**22, 1737.1, 27),
        ]

moon = Moons[0]
moon.vel_y = 1.022 * 1000 + earth.vel_y
moon.vel_x = 0 + earth.vel_x

Asteroids = [
        
        ]

CelestialBodies = Stars + Planets + Moons + Asteroids