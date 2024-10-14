from __future__ import annotations
import math

class Vec2:
    """Multi purpose vector class"""

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x: float = float(x)
        self.y: float = float(y)

    def __repr__(self):
        return f"Vec2({self.x}, {self.y})"

    def __add__(self, other: Vec2 | float | int):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            return Vec2(self.x + other, self.y + other)

    def __sub__(self, other: Vec2 | float | int):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            return Vec2(self.x - other, self.y - other)

    def __mul__(self, other: Vec2 | float | int):
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        else:
            return Vec2(self.x * other, self.y * other)

    def __truediv__(self, other: Vec2 | float | int):
        if isinstance(other, Vec2):
            return Vec2(self.x / other.x, self.y / other.y)
        else:
            return Vec2(self.x / other, self.y / other)

    def __eq__(self, other: Vec2):
        return self.x == other.x and self.y == other.y

    def rotateRadians(self, angle: float):
        return Vec2(self.x * math.cos(angle) - self.y * math.sin(angle),
                    self.x * math.sin(angle) + self.y * math.cos(angle))

    def rotate(self, angle: float):
        return self.rotateRadians(math.radians(angle))

    def rotateAroundRadians(self, point: Vec2, angle: float):
        return (self - point).rotateRadians(angle) + point

    def rotateAround(self, point: Vec2, angle: float):
        return (self - point).rotate(angle) + point

    def asTuple(self):
        return self.x, self.y

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def lengthSquared(self):
        return self.x ** 2 + self.y ** 2

    def normalized(self):
        length = self.length()
        return Vec2(self.x / length, self.y / length)