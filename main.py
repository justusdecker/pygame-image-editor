import pygame as pg
from time import perf_counter
from bin.constants import DEFAULT_BACKGROUND_COLOR
class App:
    delta_time = 0
    def __init__(self,
                 window_init_size: list[int,int] = [1280,720]):
        self.WINDOW = pg.display.set_mode(window_init_size)
        self.layers = []
        
    def run(self):
        while self.is_running:
            start_time = perf_counter()
            self.WINDOW.fill(DEFAULT_BACKGROUND_COLOR)
            self.update()
            self.check_events()
            self.delta_time = perf_counter() - start_time
    def update(self):
        pg.display.update()
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.is_running = False
    
APP = App()