from __future__ import annotations
from general_utils.vec2 import Vec2
import pygame

class Rect:

    def __init__(self, topLeft: Vec2, size: Vec2):
        self.topLeft = topLeft
        self.size = size

    def __repr__(self):
        return f"Rect({self.topLeft}, {self.size})"

    @staticmethod
    def fromValues(x, y, width, height):
        return Rect(Vec2(x, y), Vec2(width, height))

    @staticmethod
    def fromCorners(topLeft: Vec2, topRight: Vec2):
        return Rect(topLeft, topRight - topLeft + Vec2(1.0, 1.0))

    @staticmethod
    def fromCornersValues(x1, y1, x2, y2):
        return Rect.fromCorners(Vec2(x1, y1), Vec2(x2, y2))

    @staticmethod
    def fromPygameRect(rect: pygame.Rect):
        return Rect.fromValues(rect.x, rect.y, rect.width, rect.height)

    def toPygameRect(self):
        return pygame.Rect(self.topLeft.asTuple(), self.size.asTuple())

    def isPointInside(self, point: Vec2):
        return self.topLeft.x <= point.x < self.topLeft.x + self.size.x and self.topLeft.y <= point.y < self.topLeft.y + self.size.y

    def isRectInside(self, rect: Rect):
        return self.isPointInside(rect.topLeft) and self.isPointInside(rect.topLeft + rect.size - Vec2(1.0, 1.0))

    def isRectColliding(self, rect: Rect):
        return (self.topLeft.x < rect.topLeft.x + rect.size.x - 1.0 and
                self.topLeft.x + self.size.x - 1.0 > rect.topLeft.x and
                self.topLeft.y < rect.topLeft.y + rect.size.y - 1.0 and
                self.topLeft.y + self.size.y - 1.0 > rect.topLeft.y)

    def getX(self):
        return self.topLeft.x

    def getY(self):
        return self.topLeft.y

    def getWidth(self):
        return self.size.x

    def getHeight(self):
        return self.size.y

    def toTuple(self):
        return self.topLeft.x, self.topLeft.x, self.size.x, self.size.y
