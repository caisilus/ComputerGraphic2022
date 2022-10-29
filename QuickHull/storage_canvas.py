from src.fig_storage import Storage
from src.canvas import MyCanvas

class StorageCanvas(MyCanvas):
    def __init__(self, tk, width, height, bg="white"):
        super().__init__(tk, width, height, bg)
        self.storage = Storage([], self)