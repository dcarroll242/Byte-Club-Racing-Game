from general_utils.vec2 import Vec2

class Rect:

    def __init__(self, topLeft: Vec2, size: Vec2):
        self.topLeft = topLeft
        self.size = size

    @staticmethod
    def fromValues(x, y, width, height):
        return Rect(Vec2(x, y), Vec2(width, height))

    def getX(self):
        return self.topLeft.x

    def getY(self):
        return self.topLeft.y

    def getWidth(self):
        return self.size.x

    def getHeight(self):
        return self.size.y
