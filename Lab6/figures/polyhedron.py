from turtle import color
from src.figure import Figure
from src.point import face_midpoint

class Polyhedron(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.faces = []

    def draw(self, renderer):
        super().draw(renderer)
        """ for point in self.points:
            renderer.draw_point(point, color = (255, 0, 0)) """
        for face in self.faces:
            face.draw(renderer)

    def select(self):
        super().select()
        for face in self.faces:
            face.select()

    def deselect(self):
        super().deselect()
        for face in self.faces:
            face.deselect()

class Face3D(Figure):
    def __init__(self, edges, color):
        super().__init__(color)
        self.edges = edges
        num_point = len(edges)
        p0 = edges[0].points[0]
        p1 = edges[0].points[1]
        for i in range(num_point):
            self.points.append(p0)
            for edge in edges:
                if edge.points[0] == p1:
                    p0 = p1
                    p1 = edge.points[1]
                    break
                if (edge.points[1] == p1 and edge.points[0] != p0):
                    p0 = p1
                    p1 = edge.points[0]
                    break
            
        # for edge in edges:
        #     self.points.append(edge.points[0])
        #     self.points.append(edge.points[1])
        self.points = list(dict.fromkeys(self.points))

    def draw(self, renderer):
        super().draw(renderer)
        for edge in self.edges:
            edge.brush_color = self.brush_color
            edge.draw(renderer)

    def select(self):
        super().select()
        for edge in self.edges:
            edge.select()

    def deselect(self):
        super().deselect()
        for edge in self.edges:
            edge.deselect()

    def get_center(self):
        return face_midpoint(self.points)