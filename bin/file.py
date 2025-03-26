from bin.constants import DEFAULT_BACKGROUND_COLOR
from pygame import Surface,SRCALPHA,image
class File:
    def __init__(self,
                surface_size: list[int,int]=[64,64],
                color_mode: str = "RGBA",
                fromfile: str | None = None):
        self.surface_size = surface_size
        self.color_mode = color_mode
        self.layer = [] #! Add layers in the next updates!
        self.default_background_color = DEFAULT_BACKGROUND_COLOR
        self.title = "Untitled"
        match self.color_mode:
            case "RGB":
                self.surface = Surface(self.surface_size)
            case "RGBA":
                self.surface = Surface(self.surface_size,SRCALPHA)
    def render_layers(self):
        pass
    