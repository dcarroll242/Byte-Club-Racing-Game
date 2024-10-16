from guis.base_guis import GUIContainer, GUIElement
from general_utils.vec2 import Vec2
from pygame_rendering import window

VALID_ALIGNMENTS = ("TOP_LEFT", "TOP", "TOP_RIGHT", "LEFT", "CENTER", "RIGHT", "BOTTOM_LEFT", "BOTTOM", "BOTTOM_RIGHT")
ALIGNMENT_SHORTHANDS = ("TL", "T", "TR", "L", "C", "R", "BL", "B", "BR")

class AlignmentContainer(GUIContainer):

    def __init__(self, size: Vec2 = window.getScreenSize(), relativePos: Vec2 = Vec2(0, 0), visible: bool = True, children: list[GUIElement] = None, childrenAlignments: list[str] = None):
        super().__init__(size, relativePos, visible, children)
        if childrenAlignments is None:
            childrenAlignments = []

        assert len(self.children) == len(childrenAlignments)

        # sets all shorthand values to their full name or CENTER if not valid
        for i in range(len(childrenAlignments)):
            if childrenAlignments[i] in ALIGNMENT_SHORTHANDS:
                childrenAlignments[i] = VALID_ALIGNMENTS[i]
            elif childrenAlignments[i] not in VALID_ALIGNMENTS:
                childrenAlignments[i] = "CENTER"

        self.childrenAlignments = childrenAlignments

    def addChild(self, child: GUIElement, alignment: str = "CENTER"):
        super().addChild(child)

        if alignment in ALIGNMENT_SHORTHANDS:
            alignment = VALID_ALIGNMENTS[ALIGNMENT_SHORTHANDS.index(alignment)]

        self.childrenAlignments.append(alignment)

    def getAlignmentOfChild(self, child: GUIElement):
        assert child in self.children, "Element not a child of this container"
        return self.childrenAlignments[self.children.index(child)]

    def getChildOffset(self, child: GUIElement):
        alignment = self.getAlignmentOfChild(child)

        if alignment == "TOP_LEFT":
            return super().getChildOffset(child) + Vec2(0, 0)
        elif alignment == "TOP":
            return super().getChildOffset(child) + Vec2((self.size.x - child.size.x) / 2, 0)
        elif alignment == "TOP_RIGHT":
            return super().getChildOffset(child) + Vec2(self.size.x - child.size.x, 0)
        elif alignment == "LEFT":
            return super().getChildOffset(child) + Vec2(0, self.size.y - child.size.y / 2)
        elif alignment == "CENTER":
            return super().getChildOffset(child) + Vec2((self.size.x - child.size.x) / 2, (self.size.y - child.size.y) / 2)
        elif alignment == "RIGHT":
            return super().getChildOffset(child) + Vec2(self.size.x - child.size.x, (self.size.y - child.size.y) / 2)
        elif alignment == "BOTTOM_LEFT":
            return super().getChildOffset(child) + Vec2(0, self.size.y - child.size.y)
        elif alignment == "BOTTOM":
            return super().getChildOffset(child) + Vec2((self.size.x - child.size.x) / 2, self.size.y - child.size.y)
        elif alignment == "BOTTOM_RIGHT":
            return super().getChildOffset(child) + Vec2(self.size.x - child.size.x, self.size.y - child.size.y)
        else:
            raise Exception("Not valid alignment: " + alignment)