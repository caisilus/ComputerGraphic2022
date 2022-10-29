from typing import Tuple, Set
from Lab4.functions import point_from_right, point_from_left
from Lab4.poligon import Polygon
from Lab4.dot import Dot
from Lab4.line import Line
from distance import distance_from_point_to_line

def quick_hull_wrapper(canvas):
    figs = canvas.storage.figs
    points = [dot.points[0] for dot in figs if isinstance(dot, Dot)]
    shell_points = quick_hull(points)
    red = (255, 0, 0)
    for point in shell_points:
        canvas.storage.add_figure(Dot(point, red))
    first_point = shell_points[0]
    for point in shell_points[1:]:
        canvas.storage.add_figure(Line([first_point, point], red))
        first_point = point

def quick_hull(points: Tuple[int, int]):
    rightest_point = find_rightest_point(points)
    leftest_point = find_leftest_point(points)
    #upper_half, lower_half = points_halfs_sets(points, rightest_point, leftest_point)
    upper_half = points_from_right(points, rightest_point, leftest_point)
    lower_half = points_from_right(points, leftest_point, rightest_point)
    shell_points = []
    shell_points = process_points(upper_half, rightest_point, leftest_point)
    shell_points.extend(process_points(lower_half, leftest_point, rightest_point))
    return shell_points

def points_from_right(points, p1, p2):
    res = set()
    for point in points:
        if point_from_right(point, p1, p2):
            res.add(point)
    return res

def process_points(points: Set[Tuple[int, int]], p1, p2):
    #new_points = points_from_right(points, p1, p2)
    new_points = points
    most_distant_p = most_distant_point(new_points, p1, p2)
    triangle = Polygon([p1, most_distant_p, p2])
    new_points = filter_point_not_in_triangle(new_points, triangle)
    if len(new_points) == 0:
        return [p1, most_distant_p, p2]
    res = []
    right_line_points = points_from_right(new_points, p1, most_distant_p)
    res.extend(process_points(right_line_points, p1, most_distant_p))
    left_line_points = points_from_right(new_points, most_distant_p, p2)
    res.extend(process_points(left_line_points, most_distant_p, p2))
    return res

def filter_point_not_in_triangle(points, triangle: Polygon):
    new_points = set()
    for point in points:
        if not triangle.check_convex(point):
            new_points.add(point)
    return new_points

def find_rightest_point(points):
    rightest_x, rightest_y = points[0]
    for point in points:
        x, y = point[0], point[1]
        if x > rightest_x:
            rightest_x = x
            rightest_y = y
    return rightest_x, rightest_y

def find_leftest_point(points):
    leftest_x, leftest_y = points[0]
    for point in points:
        x, y = point[0], point[1]
        if x < leftest_x:
            leftest_x = x
            leftest_y = y
    return leftest_x, leftest_y

def most_distant_point(points, line_p1, line_p2):
    most_distant_point = None
    max_distance = -1
    for point in points:
        distance = distance_from_point_to_line(point, line_p1, line_p2)
        if distance > max_distance:
            most_distant_point = point
            max_distance = distance
    return most_distant_point