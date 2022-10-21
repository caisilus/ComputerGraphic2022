from math import radians, sin, cos

from src.point import Point
import numpy as np

def translation_matrix(dx, dy, dz):
    return [[1,  0,  0,  0],
            [0,  1,  0,  0],
            [0,  0,  1,  0],
            [dx, dy, dz, 1]]

def scale_matrix(kx, ky, kz):
    return [[kx, 0,  0,  0],
            [0,  ky, 0,  0],
            [0,  0,  kz, 0],
            [0,  0,  0,  1]]

def rotation_matrix(a, dir, angle):
    x, y, z = a
    l, m, n = dir
    rad_angle = radians(angle)
    cos_angle = cos(rad_angle)
    sin_angle = sin(rad_angle)
    l2 = l*l
    m2 = m*m
    n2 = n*n
    return [[l2 + cos_angle*(1 - l2), l*(1-cos_angle)*m + n*sin_angle, l*(1-cos_angle)*n + m*sin_angle, 0],
            [l*(1-cos_angle)*m - n*sin_angle, m2 + cos_angle*(1-m2),   m*(1-cos_angle)*n + l*sin_angle, 0],
            [l*(1-cos_angle)*n + m*sin_angle, m*(1-cos_angle)*n + l*sin_angle, n2 + cos_angle*(1-n2),   0], 
            [0, 0, 0, 1]]


def apply_matrix_to_point(point, matrix):
    px, py, pz = point.x, point.y, point.z
    point_vector = [px, py, pz, 1]
    new_point_arr = np.dot(point_vector, matrix)
    new_point = Point(new_point_arr[0], new_point_arr[1], new_point_arr[2])
    return new_point

def apply_matrix_to_points(points, matrix):
    new_points = []
    for point in points:
        new_point = apply_matrix_to_point(point, matrix)
        new_points.append(new_point)
    return new_points

def translate(points, dx, dy, dz):
    matrix = translation_matrix(dx, dy, dz)
    return apply_matrix_to_points(points, matrix)

def rotate(points, a, dir, angle):
    matrix = rotation_matrix(a, dir, angle)
    return apply_matrix_to_points(points, matrix)

def scale(points, kx, ky, kz, scaling_center=None):
    if scaling_center is None:
        scaling_center = centroid(points)
    dx, dy, dz = -scaling_center[0], -scaling_center[1], -scaling_center[2]
    translated_points = translate(points, dx, dy, dz)
    scaled_points = just_scale(translated_points, kx, ky, kz)
    result = translate(scaled_points, -dx, -dy, -dz)
    return result

def just_scale(points, kx, ky, kz):
    matrix = scale_matrix(kx, ky, kz)
    return apply_matrix_to_points(points, matrix)

def centroid(points):
    xs = [point.x for point in points]
    ys = [point.y for point in points]
    zs = [point.z for point in points]
    l = len(points)
    x = sum(xs) / l
    y = sum(ys) / l
    z = sum(zs) / l
    return (x, y, z)