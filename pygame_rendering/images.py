import pygame
from general_utils.vec2 import Vec2
from pygame_rendering.window import getWindow

images: dict[str, pygame.surface.Surface] = dict()

class Image:

    def __init__(self, filePath: str, rotation: float = 0.0, size: Vec2 = None):
        if filePath not in images.keys():
            images[filePath] = pygame.image.load(filePath)
        self.image = images[filePath]#.copy()

        self.__size = size

        if size is not None:
            self.image = pygame.transform.scale(self.image, size.asTuple())
        else:
            rect = self.image.get_rect()
            self.__size = Vec2(rect.width, rect.height)

        if rotation != 0.0:
            self.image = pygame.transform.rotate(self.image, rotation)

    def blitAt(self, pos: Vec2):
        getWindow().display.blit(self.image, self.getRect(pos))

    def scaleTo(self, size: Vec2):
        self.__size = size
        self.image = pygame.transform.scale(self.image, size.asTuple())

    def scaleBy(self, scale: Vec2):
        self.__size *= scale
        self.image = pygame.transform.scale_by(self.image, scale.asTuple())

    def rotateBy(self, rotation: float):
        self.image = pygame.transform.rotate(self.image, rotation)

    def getRect(self, offset: Vec2 = Vec2()):
        rect = self.image.get_rect()
        rect.topleft = offset.asTuple()
        return rect

    def getSize(self):
        return self.__size
