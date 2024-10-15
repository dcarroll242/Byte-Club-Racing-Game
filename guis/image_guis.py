from guis.base_guis import GUIElement
from pygame_rendering.images import Image
from general_utils.vec2 import Vec2

class GUIImage(GUIElement):

    def __init__(self, filePath: str, relativePos: Vec2 = Vec2(), visible: bool = True, rotation: float = 0.0, size: Vec2 = None):
        self.image = Image(filePath, rotation, size)
        super().__init__(self.image.getSize(), relativePos, visible)

    def draw(self):
        self.image.blitAt(self.getAbsolutePosition())
