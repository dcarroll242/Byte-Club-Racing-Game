import pygame
from pygame_rendering import window

isRunning: bool = True

def main():
    start()
    while isRunning:
        mainLoop()
    pygame.quit()

def start():
    window.createWindow()

def mainLoop():
    global isRunning

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    window.refreshWindow()

if __name__ == '__main__':
    main()
