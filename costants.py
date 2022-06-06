import pygame
pygame.init()
pygame.mixer.init()

FONT = pygame.font.SysFont('Arial', 20)

WIDTH = 1600
REAL_WIDTH = 1900
HEIGHT = 900

FPS = 600

UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'

AU = 149597870707
G = 6.67428e-11

SCALE = 500 / AU
ALT_SCALE = 500 / AU

MIN_SCALE = 1e-3 * 3.342245989304813e-09
MAX_SCALE = 1e+3 * 3.342245989304813e-09

X = 3.342245989304813e-09

MOVEMENT = 1e10

TIME = 1800 * 5

MAX_TIME = 1800 * 5
MIN_TIME = 1800 * 0.25