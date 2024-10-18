from __future__ import annotations
from general_utils.vec2 import Vec2
import pygame

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

BACKGROUND_COLOR = "black"

display: pygame.Surface = None

def createWindow():
    global display
    if display is None:
        pygame.init()
        display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def refreshWindow():
    pygame.display.update()
    display.fill(BACKGROUND_COLOR)

def getScreenSize():
    return Vec2(SCREEN_WIDTH, SCREEN_HEIGHT)
