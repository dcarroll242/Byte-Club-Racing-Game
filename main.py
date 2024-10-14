import pygame

isRunning: bool = True

SCREEN_WIDTH: int = 1600
SCREEN_HEIGHT: int = 800

def main():
    start()
    while isRunning:
        mainLoop()
    pygame.quit()

def start():
    pygame.init()
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def mainLoop():
    global isRunning

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            isRunning = False

if __name__ == '__main__':
    main()