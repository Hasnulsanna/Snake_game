import pygame
import json
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.font.init()


WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWHEIGHT % CELLSIZE == 0, "Window Height must be a multiple of Cell Size"
assert WINDOWWIDTH % CELLSIZE == 0, "Window Width must be a multiple of Cell Size"
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#Colour Codes
#			 R    G    B
WHITE    = (255, 255, 255)
BLACK    = (0,     0,   0)
RED      = (255,   0,   0)
GREEN    = (0,   255,   0)
DARKGREEN= (0,   155,   0)
DARKGRAY = (40,   40,  40)
YELLOW   = (255, 255,   0)
BLUE     = (0,    0,  255)

BGCOLOR = WHITE

#Control Keys
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 

#Game Sounds
APPLEEATSOUND = pygame.mixer.Sound(r"sounds/appleEatSound.wav")
BGMUSIC = pygame.mixer.music.load(r"sounds/bgmusic.mid")

level = ""

def loadHighScores():
    try:
        with open("high_scores.json", "r") as file:
            high_scores = json.load(file)
    except FileNotFoundError:
        high_scores = {"EASY": 0, "MEDIUM": 0, "HARD": 0}
    return high_scores

def saveHighScores(high_scores):
    with open("high_scores.json", "w") as file:
        json.dump(high_scores, file)
        
