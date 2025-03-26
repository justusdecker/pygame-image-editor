from pygame import Rect

class Viewport:
    def __init__(self, vport: Rect = Rect(0,0,1,1)):
        self.vport = vport
    def get_absolute_position(self,offset: list[int, int],scale:float):
        return Rect((self.vport.x - offset[0]) * scale, (self.vport.y - offset[1]) * scale,(self.vport.w - offset[0]) * scale, (self.vport.h - offset[1]) * scale)