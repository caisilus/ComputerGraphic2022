from src.UI import UI_base
from storage_canvas import StorageCanvas

class UI_2D(UI_base):
    def __init__(self, titel="Painter", width=0, height=0):
        super().__init__(titel, width, height)

    def create_canvas(self):
        self.canv = StorageCanvas(self, width=self.win_width, height=self.win_height, bg="white")
        self.canv.grid(row=1, column=2)
        self.controller.set_canvas(self.canv)