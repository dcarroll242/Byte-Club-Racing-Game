import pygame
from general_utils.vec2 import Vec2
from general_utils.rect import Rect
from pygame_rendering import window

images: dict[str, pygame.surface.Surface] = dict()

class Image:
    """A diverse image class that allows for rotating, scaling, and the displaying of images to the screen

    designed so that it can be versatile enough to be used in both GUIs and the rendering of the game world (in the future)
    """
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

    def blitAt(self, pos: Vec2, cull: bool = True, cullRect: Rect = None):
        """blit (draw) this image to the screen

        if cull is true then it will cull (not draw) the image if it is entirely outside the cullRect
        if cullRect is left as None, it will become a Rect representing the size of the screen (Rect(Vec2(0.0, 0.0), window.getScreenSize()))

        :param pos: where to draw the image (top left corner)
        :param cull: whether to cull this image or not
        :param cullRect: the rectangle to cull the image in (if cull is True)
        :return: None
        """
        if cull:

            if cullRect is None:
                cullRect = Rect(Vec2(0.0, 0.0), window.getScreenSize())

            if cullRect.isRectColliding(self.getRect(pos)):
                window.display.blit(self.image, self.getRect(pos).toPygameRect())

        else:

            window.display.blit(self.image, self.getRect(pos).toPygameRect())

    def blitAtCropped(self, pos: Vec2, boundingBox: Rect):
        """blit (draw) a cropped version of this image to the screen

        draws the image so that any pixels outside the boundingBox are not displayed and all that are inside the boundingBox are displayed

        :param pos: where to draw the image (top left corner)
        :param boundingBox: the rectangle to crop the image in
        :return: None
        """
        if boundingBox.isRectInside(self.getRect(pos)):
            # if it's completely inside the bounding box just draw it
            window.display.blit(self.image, self.getRect(pos).toPygameRect())

        elif boundingBox.isRectColliding(self.getRect(pos)):

            # get a new rect from the parts of this image and the bounding box that overlap
            rect = Rect.fromCornersValues(max(pos.x, boundingBox.getX()), max(pos.y, boundingBox.getY()),
                                          min(pos.x + self.getSize().x, boundingBox.getX() + boundingBox.getWidth()) - 1.0,
                                          min(pos.y + self.getSize().y, boundingBox.getY() + boundingBox.getHeight()) - 1.0).toPygameRect()

            window.display.blit(self.image.subsurface(rect), rect)
        # if it's not even colliding with the bounding box don't do anything

    def scaleTo(self, size: Vec2):
        self.__size = size
        self.updateImageTransformation()

    def scaleBy(self, scale: Vec2):
        self.__size *= scale
        self.updateImageTransformation()

    def rotateBy(self, rotation: float):
        self.__rotation = (self.__rotation + rotation) % 360
        self.updateImageRotation()

    def rotateTo(self, rotation: float):
        self.__rotation = rotation % 360
        self.updateImageRotation()

    def updateImageRotation(self):
        """updates the image rotation

        note: this usually isn't necessary as any rotation function already calls this method
        """
        self.image = pygame.transform.rotate(self.scaledImage, self.__rotation)

    def updateImageTransformation(self):
        """updates the image scale and rotation

        note: this usually isn't necessary as any scaling function already calls this method
        """
        self.scaledImage = pygame.transform.scale(self.originalImage, self.__size.asTuple())
        self.updateImageRotation()

    def getRect(self, offset: Vec2 = Vec2()):
        """return a Rect that the image fits into"""
        rect = self.image.get_rect()
        rect.center = (offset + self.__size / 2.0).asTuple()
        return Rect.fromPygameRect(rect)

    def getSize(self):
        return self.__size

    def getRotation(self):
        return self.__rotation
