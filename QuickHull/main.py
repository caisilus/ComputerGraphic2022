import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.UI import UI_base
from Lab4.dot import DotMode
from quick_hull import *
from ui_2d import UI_2D

ui = UI_2D()
ui.add_button("Add point",lambda: ui.controller.switch_mode("AddPoint"))
ui.add_button("Quick hull",lambda: quick_hull_wrapper(ui.canv))
ui.add_button("Clear",lambda: ui.canv.delete_content())
ui.create_canvas()
ui.controller.add_mode("AddPoint", DotMode(ui.canv))
ui.run()