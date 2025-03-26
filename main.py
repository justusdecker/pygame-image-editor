import pygame as pg
from time import perf_counter
from bin.constants import DEFAULT_BACKGROUND_COLOR
from bin.file import File
class App:
    delta_time = 0
    def __init__(self,
                 window_init_size: list[int,int] = [1280,720]):
        self.WINDOW = pg.display.set_mode(window_init_size)
        self.file = File()
        self.is_running = True
        self.scale = 1
        self.viewport_xy = [0,0]
        self.viewport_change = []
    def run(self):
        while self.is_running:
            start_time = perf_counter()
            self.WINDOW.fill(DEFAULT_BACKGROUND_COLOR)
            self.update()
            self.check_events()
            self.delta_time = perf_counter() - start_time
    def update(self):
        self.WINDOW.blit(self.file.render_layers(),self.viewport_xy)
        pg.display.update()
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.is_running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.viewport_change.append("x-")
                if event.key == pg.K_RIGHT:
                    self.viewport_change.append("x+")
                if event.key == pg.K_UP:
                    self.viewport_change.append("y-")
                if event.key == pg.K_DOWN:
                    self.viewport_change.append("y+")
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    if "x-" in self.viewport_change: self.viewport_change.remove("x-")
                if event.key == pg.K_RIGHT:
                    if "x+" in self.viewport_change: self.viewport_change.remove("x+")
                if event.key == pg.K_UP:
                    if "y-" in self.viewport_change: self.viewport_change.remove("y-")
                if event.key == pg.K_DOWN:
                    if "y+" in self.viewport_change: self.viewport_change.remove("y+")
        if "x-" in self.viewport_change: self.viewport_xy[0] -= 1
        if "x+" in self.viewport_change: self.viewport_xy[0] += 1
        if "y-" in self.viewport_change: self.viewport_xy[1] -= 1
        if "y+" in self.viewport_change: self.viewport_xy[1] += 1
                    
    
APP = App()
APP.run()