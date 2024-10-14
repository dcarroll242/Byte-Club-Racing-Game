from __future__ import annotations
import pygame

class Window:  # singleton class

    window: Window = None

    def __init__(self):
        assert Window.window is None, "Window already created, try using 'Window.getWindow'"

        self.screenWidth = 1600
        self.screenHeight = 800

        self.backgroundColor = "black"

        pygame.init()

        self.display = pygame.display.set_mode((self.screenWidth, self.screenHeight))

    def refresh(self):
        pygame.display.update()
        self.display.fill(self.backgroundColor)

def createWindow():
    if Window.window is None:
        Window.window = Window()

def getWindow():
    createWindow()
    return Window.window

def refreshWindow():
    getWindow().refresh()
