from __future__ import annotations
from general_utils.vec2 import Vec2
from abc import abstractmethod, ABC
from pygame_rendering import window

class GUIElement(ABC):

    def __init__(self, size: Vec2 = Vec2(), relativePos: Vec2 = Vec2(0, 0), visible: bool = True):
        self.relativePos = relativePos
        self.__size = size
        self.visible = visible
        self.parent: GUIContainer | type(None) = None

    @abstractmethod
    def draw(self):
        pass

    def addToContainer(self, container: GUIContainer):
        container.addChild(self)

    def toggleVisible(self):
        self.visible = not self.visible

    def setVisible(self, visible: bool = True):
        self.visible = visible

    def getVisible(self) -> bool:
        return self.visible

    def setSize(self, size: Vec2):
        self.__size = size

    def getSize(self):
        return self.__size

    # TODO: create an absolutePosition field that gets updated with relative
    #  positions so that this doesn't need to called every frame for every image
    def getAbsolutePosition(self):
        if self.parent is None:
            return Vec2()
        else:
            return self.relativePos + self.parent.getChildOffset(self) + self.parent.getAbsolutePosition()


class GUIContainer(GUIElement):

    def __init__(self, size: Vec2 = window.getScreenSize(), relativePos: Vec2 = Vec2(0, 0),
                 visible: bool = True, children: list[GUIElement] = None):
        super().__init__(size, relativePos, visible)
        if children is None:
            children = []
        self.children = list(children)

    def draw(self):
        super().draw()
        for child in self.children:
            if child.getVisible():
                child.draw()

    def addChild(self, child: GUIElement):
        assert child.parent is None, "Element already added to a container"

        child.parent = self
        self.children.append(child)

        return self

    @abstractmethod
    def getChildOffset(self, child: GUIElement):
        assert child in self.children, "Element not a child of this container"
        return Vec2()

    def getChildren(self):
        return self.children

class RootContainer(GUIContainer):  # not sure if this needs its own class or not, but I thought why not

    def getChildOffset(self, child: GUIElement):
        return super().getChildOffset(child)

