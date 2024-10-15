import pygame
from events.event_handler import createPygameEventListener, broadcastPygameEvents
from pygame_rendering import window
from guis.base_guis import RootContainer
from guis.container_guis import AlignmentContainer
from guis.image_guis import GUIImage
from general_utils.vec2 import Vec2

isRunning: bool = True
rootGUI: RootContainer = None

def main():
    start()
    while isRunning:
        mainLoop()
    pygame.quit()

def start():
    window.createWindow()

    createPygameEventListener(pygame.QUIT, stopProgram)

    # create a gui to draw to (just to test)
    # NOTE: in the future, there will be a scene system so that you can easily switch between GUIs and also render the game world
    global rootGUI
    rootGUI = RootContainer()
    alignmentContainer = AlignmentContainer()

    image = GUIImage("sprites/SpriteTest.png", Vec2(100, 100), size=Vec2(160, 160))
    image2 = GUIImage("sprites/SpriteTest.png", Vec2(500, 100), size=Vec2(160, 160), rotation=200)
    image3 = GUIImage("sprites/SpriteTest.png", size=Vec2(320, 640))

    rootGUI.addChild(alignmentContainer)
    alignmentContainer.addChild(image, "TOP_LEFT")
    alignmentContainer.addChild(image2, "TOP_LEFT")
    alignmentContainer.addChild(image3, "BR")


def mainLoop():
    global isRunning

    # will be replaced when scenes are added
    rootGUI.draw()

    broadcastPygameEvents(pygame.event.get())

    window.refreshWindow()

def stopProgram():
    global isRunning
    isRunning = False


if __name__ == '__main__':
    main()
