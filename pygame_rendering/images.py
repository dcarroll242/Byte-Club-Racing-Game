import pygame
from general_utils.vec2 import Vec2
from general_utils.rect import Rect
from pygame_rendering.window import getWindow

images: dict[str, pygame.surface.Surface] = dict()

class Image:

    def __init__(self, filePath: str, rotation: float = 0.0, size: Vec2 = None):
        if filePath not in images.keys():
            images[filePath] = pygame.image.load(filePath)

        self.originalImage = images[filePath]
        self.scaledImage = images[filePath]
        self.image = images[filePath]

        self.__size = size
        self.__rotation = rotation

        if size is not None:
            self.image = pygame.transform.scale(self.image, size.asTuple())
        else:
            rect = self.image.get_rect()
            self.__size = Vec2(rect.width, rect.height)

        if rotation != 0.0:
            self.image = pygame.transform.rotate(self.image, rotation)

    def blitAt(self, pos: Vec2):
        getWindow().display.blit(self.image, self.getRect(pos))

    def blitAtCropped(self, pos: Vec2, boundingBox: Rect):
        if (pos.x + self.__size.x <= boundingBox.getX() + boundingBox.size.x and pos.x >= boundingBox.getX() and
                pos.y + self.__size.y <= boundingBox.getY() + boundingBox.size.y and pos.y >= boundingBox.getY()):
            self.blitAt(pos)
        elif not (pos.x + self.__size.x < boundingBox.getX() or pos.x > boundingBox.getX() + boundingBox.size.x or
                pos.y + self.__size.y < boundingBox.getY() or pos.y > boundingBox.getY() + boundingBox.size.y):
            pass
            # MAKE IT CROPPED AAAA
            # rect = Rect(Vec2(max(pos.x, boundingBox.getX()), max(pos.y, boundingBox.getY())), Vec2)
        else:
            pass

    def scaleTo(self, size: Vec2):
        self.__size = size
        self.updateImageTransformation()

    def scaleBy(self, scale: Vec2):
        self.__size *= scale
        self.updateImageTransformation()

    def rotateBy(self, rotation: float):
        self.__rotation += rotation
        self.updateImageRotation()

    def rotateTo(self, rotation: float):
        self.__rotation = rotation
        self.updateImageRotation()

    def updateImageRotation(self):
        self.image = pygame.transform.rotate(self.scaledImage, self.__rotation)

    def updateImageTransformation(self):
        self.scaledImage = pygame.transform.scale(self.originalImage, self.__size.asTuple())
        self.updateImageRotation()

    def getRect(self, offset: Vec2 = Vec2()):
        rect = self.image.get_rect()
        rect.center = (offset + self.__size / 2.0).asTuple()
        return rect

    def getSize(self):
        return self.__size
