from pygame import Surface
class Layer:
    def __init__(self,
                 size: list[int,int],
                 pos: list[int,int]):
        self.size = size
        self.pos = pos
        self.rotation = .0
        self.pivot = [xy+(s//2) for xy,s in zip(pos,size)]
        
        self.blending_mode = None
        
        self.opacity = 1.
        self.locked = False
        self.alpha_inherit = False
        self.alpha_locked = False
        self.visible = True
        
        self.styles = {
            "outline": None,
            "outerShadow": None,
            "innerShadow": None,
            "innerGlow": None,
            "outerGlow": None,
            "gradientOverlay": None,
            "textureOverlay": None
        }
        self.surface = Surface(self.size)
        self.surface.fill((75,75,75))
    def get_surface(self):
        return self.surface,self.pos
        