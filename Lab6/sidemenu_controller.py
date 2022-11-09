from Lab6.projections import *
from Lab7.rotation_figure import RotationFigure
from src.point import Point
from Lab6.point3D import Point3D
from Lab6.figures.line3D import Line3D
from Lab6.figures.cube import Cube
from Lab6.figures.tetrahedron import Tetrahedron
from Lab6.figures.octahedron import Octahedron
from Lab6.figures.icosahedron import Icosahedron
from Lab6.figures.dodecahedron import Dodecahedron


class SideMenu_Controller():
    def __init__(self, renderer, scene, loader):
        self.mode_name = "2D"
        self.instrument_name = "Point"
        self.loader = loader
        self.mode_projection = {
            "2D": simple2D_projection(),
            "3D perspective": perspective_projection(),
            "3D aksonometric": akso_projection(),
        }
        self.figures_names = ["Point", "Line", "Cube", "Tetrahedron", "Octahedron", "Icosahedron", "Dodecahedron",
                              "Load Figure"]
        self.renderer = renderer
        self.scene = scene
        self.forming_point = None
        self.axes = ['OX', 'OY', 'OZ']
        self.axis = None
        self.rotation_axis = None
        self.partition = None

    def mode_update(self, event):
        mode_name = event.widget.get()
        self.mode_name = mode_name
        self.renderer.set_projection(self.mode_projection[mode_name])
        self.renderer.render_scene(self.scene)

    def figure_update(self, event):
        figure_name = event.widget.get()
        self.figure_name = figure_name

    def draw_figure(self):
        if self.figure_name == "Point":
            self.scene.add_figure(Point3D(Point(0, 50, 0), (255, 0, 0)))
        elif self.figure_name == "Line":
            self.scene.add_figure(Line3D(Point(100, 0, 0), Point(0, 0, 0)))
        elif self.figure_name == "Cube":
            self.scene.add_figure(Cube(Point(50, 50, 50), 100))
        elif self.figure_name == "Tetrahedron":
            self.scene.add_figure(Tetrahedron(Point(50, 50, 50), 100))
        elif self.figure_name == "Octahedron":
            self.scene.add_figure(Octahedron(Point(50, 50, 50), 100))
        elif self.figure_name == "Icosahedron":
            self.scene.add_figure(Icosahedron(Point(50, 50, 50), 100))
        elif self.figure_name == "Dodecahedron":
            self.scene.add_figure(Dodecahedron(Point(50, 50, 50), 100))
        elif self.figure_name == "Load Figure":
            res = self.loader.open_file()
            self.scene.add_figure(res)
        self.renderer.render_scene(self.scene)

    def axis_update(self, event):
        axis = event.widget.get()
        self.axis = axis
    def add_forming_point(self):  # не очень красивый код, но я не придумала лучше
        flag = False
        i = []
        for x in self.scene.storage:
            if isinstance(x, RotationFigure):
                flag = True
                i.append(x)
        if flag:
            for x in i:
                if x.selected:
                    x.update_rotation_figure(self.forming_point, self.partition, self.axis)
        else:
            self.scene.add_figure(RotationFigure(Point(50, 50, 50), self.axis, self.partition))
            self.scene.storage[-1].update_rotation_figure(self.forming_point, self.partition, self.axis)
        self.renderer.render_scene(self.scene)
