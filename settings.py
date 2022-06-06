from celestial_bodies import *

Stars = [
        Star('Sun',  WIDTH / 2 ,  HEIGHT / 2,  	1.988500 * 10**30, 69570.0, (252, 150,   1) , 5778, 25),
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

mercury = Planets  [0]; mercury.vel_y = 47.36 * 1000
venus   = Planets  [1]; venus.vel_y   = 35.02 * 1000
earth   = Planets  [2]; earth.vel_y   = 29.78 * 1000
mars    = Planets  [3]; mars.vel_y    = 24.07 * 1000
jupiter = Planets  [4]; jupiter.vel_y = 13.06 * 1000
saturn  = Planets  [5]; saturn.vel_y  =  9.68 * 1000
uranus  = Planets  [6]; uranus.vel_y  =  6.80 * 1000
neptune = Planets  [7]; neptune.vel_y =  5.43 * 1000
pluto   = Planets  [8]; pluto.vel_y   =  4.67 * 1000

Moons = [
        Moon('Moon'     , earth  , 0.002570 * AU, (177, 173, 173), 7.3477 * 10**22, 1737.1),
            
        Moon('Phobos'   , mars   , 0.000620 * AU, (177, 173, 173), 1.0659 * 10**16,  111.0),
        Moon('Deimos'   , mars   , 0.001560 * AU, (177, 173, 173), 1.4760 * 10**15,   62.0),
         
        Moon('Io'       , jupiter, 0.002857 * AU, (177, 173, 173), 8.9319 * 10**22, 1821.3),
        Moon('Europa'   , jupiter, 0.004500 * AU, (177, 173, 173), 4.7998 * 10**22, 1560.8),
        Moon('Ganymede' , jupiter, 0.009000 * AU, (177, 173, 173), 1.4819 * 10**22, 2634.2),
        Moon('Callisto' , jupiter, 0.019000 * AU, (177, 173, 173), 1.0241 * 10**22, 2410.3),
        Moon('Amalthea' , jupiter, 0.001212 * AU, (177, 173, 173), 2.0800 * 10**18,   83.5),
          
        Moon('Mimas'    , saturn , 0.001240 * AU, (177, 173, 173), 3.7493 * 10**19,  198.2),
        Moon('Encedalus', saturn , 0.001590 * AU, (177, 173, 173), 1.0802 * 10**20,  252.1),
        Moon('Tethys'   , saturn , 0.001969 * AU, (177, 173, 173), 6.1755 * 10**20,  533.0),
        Moon('Dione'    , saturn , 0.002522 * AU, (177, 173, 173), 1.0957 * 10**21,  561.7),
        Moon('Rhea'     , saturn , 0.003523 * AU, (177, 173, 173), 1.5243 * 10**21,  764.3),
        Moon('Titan'    , saturn , 0.008167 * AU, (177, 173, 173), 1.3455 * 10**23, 2574.7),
        Moon('Iapetus'  , saturn , 0.023802 * AU, (177, 173, 173), 1.8059 * 10**21,  735.6),
        
        Moon('Miranda'  , uranus , 0.000868 * AU, (177, 173, 173), 6.5941 * 10**19,  235.8),
        Moon('Ariel'    , uranus , 0.001276 * AU, (177, 173, 173), 1.2948 * 10**21,  578.9),
        Moon('Umbriel'  , uranus , 0.001778 * AU, (177, 173, 173), 1.2214 * 10**21,  584.7),
        Moon('Titania'  , uranus , 0.002916 * AU, (177, 173, 173), 3.4199 * 10**21,  788.9),
        Moon('Oberon'   , uranus , 0.003900 * AU, (177, 173, 173), 2.8834 * 10**21,  761.4),
        
        Moon('Larissa'  , neptune, 0.000491 * AU, (177, 173, 173), 4.9456 * 10**18,   97.0),
        Moon('Proteus'  , neptune, 0.000786 * AU, (177, 173, 173), 5.0355 * 10**19,  210.0),
        Moon('Triton'   , neptune, 0.002371 * AU, (177, 173, 173), 2.1390 * 10**22, 1353.4),
        Moon('Nereid'   , neptune, 0.036858 * AU, (177, 173, 173), 3.0872 * 10**19,  178.5),
        
        Moon('Charon'   , pluto  , 0.000192 * AU, (177, 173, 173), 1.5466 * 10**21,  603.6),
        ]

moon      = Moons [0];  moon.vel_tan      =  1.022 * 1000
 
phobos    = Moons [1];  phobos.vel_tan    =  2.138 * 1000
deimos    = Moons [2];  deimos.vel_tan    =  1.351 * 1000
 
io        = Moons [3];  io.vel_tan        = 17.334 * 1000
europa    = Moons [4];  europa.vel_tan    = 13.743 * 1000
ganymede  = Moons [5];  ganymede.vel_tan  = 10.880 * 1000
callisto  = Moons [6];  callisto.vel_tan  =  8.204 * 1000
amalthea  = Moons [7];  amalthea.vel_tan  =  26.57 * 1000

mimas     = Moons [8];  mimas.vel_tan     = 14.280 * 1000
enceladus = Moons [9];  enceladus.vel_tan = 12.635 * 1000
tethys    = Moons[10];  tethys.vel_tan    = 11.350 * 1000
dione     = Moons[11];  dione.vel_tan     = 10.027 * 1000
rhea      = Moons[12];  rhea.vel_tan      =  8.483 * 1000
titan     = Moons[13];  titan.vel_tan     =  5.569 * 1000 
iapetus   = Moons[14];  iapetus.vel_tan   =  3.263 * 1000

miranda   = Moons[15];  miranda.vel_tan   =  6.685 * 1000
ariel     = Moons[16];  ariel.vel_tan     =  5.508 * 1000
umbriel   = Moons[17];  umbriel.vel_tan   =  4.667 * 1000
titania   = Moons[18];  titania.vel_tan   =  3.644 * 1000
oberon    = Moons[19];  oberon.vel_tan    =  3.152 * 1000

larissa   = Moons[20];  larissa.vel_tan   =  9.637 * 1000
proteus   = Moons[21];  proteus.vel_tan   =  7.625 * 1000
triton    = Moons[22];  triton.vel_tan    =  4.390 * 1000
nereid    = Moons[23];  nereid.vel_tan    =  0.934 * 1000

charon    = Moons[24];  charon.vel_tan    =  0.199 * 1000

CelestialBodies = Stars + Planets + Moons
