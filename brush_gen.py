# -*- coding: utf-8 -*-
import dotmap_types
from dotmap_types import Vec3
from dotmap_types import Brush

def dimensionMin(min_dot, x_size, y_size, z_size):
    #gets the min x min y min z point and 3 dimensions
    p1 = min_dot
    p2 = min_dot + Vec3(x_size, 0, 0)
    p3 = min_dot + Vec3(0, y_size, 0)
    p4 = min_dot + Vec3(0, 0, z_size)
    p5 = min_dot + Vec3(x_size, y_size, 0)
    p6 = min_dot + Vec3(x_size, 0, z_size)
    p7 = min_dot + Vec3(0, y_size, z_size)
    p8 = min_dot + Vec3(x_size, y_size, z_size)

    return Brush(p1, p2, p3, p4, p5, p6, p7, p8)

def dimensionMaxYMinX(dot, x_size, y_size, z_size):
    #gets the min x max y min z point and 3 dimensions
    p1 = dot
    p2 = dot + Vec3(x_size, 0, 0)
    p3 = dot + Vec3(0, 0 - y_size, 0)
    p4 = dot + Vec3(0, 0, z_size)
    p5 = dot + Vec3(x_size, 0 - y_size, 0)
    p6 = dot + Vec3(x_size, 0, z_size)
    p7 = dot + Vec3(0, 0 - y_size, z_size)
    p8 = dot + Vec3(x_size, 0 - y_size, z_size)

    return Brush(p1, p2, p3, p4, p5, p6, p7, p8)

def dimensionMax(min_dot, x_size, y_size, z_size):
    #gets the min x min y min z point and 3 dimensions
    p1 = min_dot
    p2 = min_dot + Vec3(0 - x_size, 0, 0)
    p3 = min_dot + Vec3(0, 0 - y_size, 0)
    p4 = min_dot + Vec3(0, 0, z_size)
    p5 = min_dot + Vec3(0 - x_size, 0 - y_size, 0)
    p6 = min_dot + Vec3(0 - x_size, 0, z_size)
    p7 = min_dot + Vec3(0, 0 - y_size, z_size)
    p8 = min_dot + Vec3(0 - x_size, 0 - y_size, z_size)

    return Brush(p1, p2, p3, p4, p5, p6, p7, p8)

def dimensionMaxXMinY(dot, x_size, y_size, z_size):
    #gets the min x max y min z point and 3 dimensions
    p1 = dot
    p2 = dot + Vec3(0 - x_size, 0, 0)
    p3 = dot + Vec3(0, y_size, 0)
    p4 = dot + Vec3(0, 0, z_size)
    p5 = dot + Vec3(0 - x_size, y_size, 0)
    p6 = dot + Vec3(0 - x_size, 0, z_size)
    p7 = dot + Vec3(0, y_size, z_size)
    p8 = dot + Vec3(0 - x_size, y_size, z_size)

    return Brush(p1, p2, p3, p4, p5, p6, p7, p8)