import math

def distance_from_point_to_line(point, line_p1, line_p2):
    x0, y0 = point
    x1, y1 = line_p1
    x2, y2 = line_p2
    #numenator = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)
    numenator = abs(x0*(y2-y1)+x2*(y1-y0)+x1*(y0-y2))
    denominator = math.sqrt((y2-y1)**2 + (x2-x1)**2)
    return numenator / denominator