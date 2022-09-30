from math import *
import re
from tkinter import *
from tkinter import ttk
from draw_line import *

def get_point_inline(p, p1, p2, c1, c2, di=None, gradient=False):
    x, y = p
    x1, y1 = p1
    x2, y2 = p2
    dy = abs(y2 - y1)
    dx = abs(x2 - x1)
    grad = dy / (dx + 0.000001)
    dely = 1 if y2 - y1 > 0 else -1
    delx = 1 if x2 - x1 > 0 else -1

    if grad <= 1:
        if di == None:
            di = 2*dy - dx
        if gradient:
            new_c = count_grad_color(c1, c2, x, x1, x2)
        else:
            new_c = (255, 0, 0)
        if di < 0:
            di = di + 2*dy
        else:
            y = y + dely
            di = di + 2*(dy - dx)
        x = x + delx
        if x*delx > x2*delx:
            x = x2
    else:
        if di == None:
            di = 2*dx - dy
        if gradient:
            new_c = count_grad_color(c1, c2, y, y1, y2)
        else:
            new_c = (255, 0, 0)
        if di < 0:
            di = di + 2*dx
        else:
            x = x + delx
            di = di + 2*(dx - dy)
        y = y + dely

        if y*dely > y2*dely:
            y = y
    return (x, y), new_c, di


def draw_triangel(img, p1, p2, p3, c1, c2, c3):
    op, oc, dio = get_point_inline(p1, p1, p2, c1, c2)
    ap, ac, dia = get_point_inline(p1, p1, p3, c1, c3)

    ostart = p1
    oend = p2
    astart = p1
    aend = p3

    ocstart = c1
    ocend = c2
    acstart = c1
    acend = c3

    while ((op != oend) and (ap != aend)):
        line_bresenchem(img, op, ap, oc, ac)

        op, oc, dio = get_point_inline(op, ostart, oend, ocstart, ocend, dio, gradient=True)
        ap, ac, dia = get_point_inline(ap, astart, aend, acstart, acend, dia, gradient=True)

        if (op == p2):
            #ap, ac, dia = get_point_inline(ap, astart, aend, acstart, acend, dia, gradient=True)
            while ((ap != aend)):
                line_bresenchem(img, op, ap, oc, ac)
                ap, ac, dia = get_point_inline(ap, astart, aend, acstart, acend, dia, gradient=True)
            break
        if (ap == p3):
            #op, oc, dio = get_point_inline(op, ostart, oend, ocstart, ocend, dio, gradient=True)
            while ((op != oend)):
                line_bresenchem(img, op, ap, oc, ac)
                op, oc, dio = get_point_inline(op, ostart, oend, ocstart, ocend, dio, gradient=True)
            break

    return

class canvas_control:
    def __init__(self):
        self.root_main = Tk()
        self.root_main.title("Draw Triangle")

        win_width = self.root_main.winfo_screenwidth() // 2
        win_height = self.root_main.winfo_screenheight() // 2

        canv = Canvas(self.root_main, width=win_width, height=win_height, bg="white")
        self.img = PhotoImage(width=win_width, height=win_height)
        canv.create_image((win_width / 2, win_height / 2), image=self.img, state="normal")

        self.root_main.bind("<ButtonRelease-1>", self.set_triangle_point)

        self.p1 = None
        self.p2 = None
        self.p3 = None

        canv.pack()
        self.root_main.mainloop()

    def set_triangle_point(self, event):
        c1=(255, 0, 0)
        c2=(0, 0, 255)
        c3=(0, 255, 0)
        if self.p1 == None:
            self.p1 = (event.x, event.y)
        elif self.p2 == None:
            self.p2 = (event.x, event.y)
        else:
            self.p3 = (event.x, event.y)
            draw_triangel(self.img, self.p1, self.p2, self.p3, c1, c2, c3)
            self.p2 = None
            self.p3 = None
            self.p1 = None



if __name__ == "__main__":
    cc = canvas_control()