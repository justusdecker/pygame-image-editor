from bin.constants import DEFAULT_BACKGROUND_COLOR
from pygame import Surface,SRCALPHA,image
from bin.layer import Layer
class File:
    def __init__(self,
                surface_size: list[int,int]=[64,64],
                color_mode: str = "RGBA",
                fromfile: str | None = None):
        self.surface_size = surface_size
        self.color_mode = color_mode
        self.layers = [Layer([1280,720],[0,0])]
        self.default_background_color = DEFAULT_BACKGROUND_COLOR
        self.title = "Untitled"
        
    def render_layers(self):
        match self.color_mode:
            case "RGB":
                self.surface = Surface(self.surface_size)
            case "RGBA":
                self.surface = Surface(self.surface_size,SRCALPHA)
        for layer in self.layers:
            self.surface.blit(*layer.get_surface())
        return self.surface
    
    