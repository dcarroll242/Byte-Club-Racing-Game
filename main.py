import pygame
from events.event_handler import createPygameEventListener, broadcastPygameEvents
from pygame_rendering import window

isRunning: bool = True

def main():
    start()
    while isRunning:
        mainLoop()
    pygame.quit()

def start():
    window.createWindow()

    createPygameEventListener(pygame.QUIT, stopProgram)

def mainLoop():
    global isRunning

    broadcastPygameEvents(pygame.event.get())

    window.refreshWindow()

def stopProgram():
    global isRunning
    isRunning = False


if __name__ == '__main__':
    main()
