# -*- coding: utf-8 -*-
#import heapq

#NOTE: Only works with 6 planes brushes


class Header:
    #headers, should be changed based on the game

    def __init__(self):
        self.entity = "// entity 0\r\n"
        self.open = "{\r\n"
        self.close = "}\r\n"
        self.classname = "\"classname\" \"worldspawn\"\r\n"

        pass

    pass

header = Header()

class Vec3:
    #class for 3d points

    def __init__(self, x, y, z):

        #init a new 3d point
        #X, Y, Z are .map world location varaibles
        #str is a string representing a point which can be inserted to a .map file without errors
        # (as long as done the right way, see knowlege)

        self.x = x
        self.y = y
        self.z = z
        self.str = '( {} {} {} )'.format(x, y, z)

        pass

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z

        return Vec3(x, y, z)

    pass

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Vec3(x, y, z)

    def __str__(self):
        return self.str


class Brush:
    #class for planes

    def __init__(self, p1, p2, p3, p4, p5,  p6, p7, p8):
        #init a new box brush
        #gets the 8 points of the box
        #than sort which points belong to each plane
        #up, dwn, lft, rit, fwd, bwd are planes

        points = [p1, p2, p3, p4, p5,  p6, p7, p8]
        self.points = points

        order = Points_Order(points)

        self.up = next(order)  # up = max z axis
        self.dwn = next(order)  # dwn = min z axis
        self.lft = next(order)  # lft = min x axis
        self.rit = next(order)  # rit = max x axis
        self.fwd = next(order)  # fwd = max y axis
        self.bwd = next(order)  # bwd = min y axis

        self.str = "{\r\n"
        self.str += "{} {} {} NULL 0 0 0 0.5 0.5 0 0 0\r\n".format(self.up[0].str, self.up[1].str, self.up[2].str)
        self.str += "{} {} {} NULL 0 0 0 0.5 0.5 0 0 0\r\n".format(self.dwn[0].str, self.dwn[1].str, self.dwn[2].str)
        self.str += "{} {} {} NULL 0 0 0 0.5 0.5 0 0 0\r\n".format(self.lft[0].str, self.lft[1].str, self.lft[2].str)
        self.str += "{} {} {} NULL 0 0 0 0.5 0.5 0 0 0\r\n".format(self.rit[0].str, self.rit[1].str, self.rit[2].str)
        self.str += "{} {} {} NULL 0 0 0 0.5 0.5 0 0 0\r\n".format(self.fwd[0].str, self.fwd[1].str, self.fwd[2].str)
        self.str += "{} {} {} NULL 0 0 0 0.5 0.5 0 0 0\r\n".format(self.bwd[0].str, self.bwd[1].str, self.bwd[2].str)
        self.str += "}\r\n"

        pass
    def __str__(self):
        return self.str

    pass


def Points_Order(points):
    #in: 8 points of the cube
    #out: 4 points of each plane

    #xAxis = []
    #yAxis = []
    #zAxis = []
#
    #for point in points:
    #    xAxis.append(point.x)
    #for point in points:
    #    yAxis.append(point.y)
    #for point in points:
    #    zAxis.append(point.z)

    points.sort(key = lambda x: x.z)
    yield(Up_Order( points[4:]))
    yield(Dwn_Order( points[:4]))

    points.sort(key = lambda x: x.x)
    yield(Lft_Order( points[:4]))
    yield(Rit_Order( points[4:]))

    points.sort(key = lambda x: x.y)
    yield(Fwd_Order( points[4:]))
    yield(Bwd_Order( points[:4]))

    pass


#----------------------------------------------------/
#------ this clusterfuck orgenize the points clocwise/
#----------------------------------------------------/
def Up_Order(points):
    #in: list of 4 points
    #out: list of 3 points clockwise order

    new_order = []

    choosen_point = None

    for point in points:
        if choosen_point is not None:
            if point.x <= choosen_point.x:
                if point.y >= choosen_point.y:
                    choosen_point = point
        else:
            choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.x >= choosen_point.x:
            if point.y >= choosen_point.y:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.x >= choosen_point.x:
            if point.y <= choosen_point.y:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    return new_order



def Dwn_Order(points):
    #in: list of 4 points
    #out: list of 3 points clockwise order

    new_order = []

    choosen_point = points[0]

    for point in points:
        if point.x >= choosen_point.x:
            if point.y >= choosen_point.y:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.x <= choosen_point.x:
            if point.y >= choosen_point.y:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if choosen_point is not None:
            if point.x <= choosen_point.x:
                if point.y <= choosen_point.y:
                    choosen_point = point
        else:
            choosen_point = point

        pass
    new_order.append(choosen_point)

    return new_order



def Lft_Order(points):
    #in: list of 4 points
    #out: list of 3 points clockwise order

    new_order = []

    choosen_point = None

    for point in points:
        if choosen_point is not None:
            if point.y >= choosen_point.y:
                if point.z >= choosen_point.z:
                    choosen_point = point
        else:
            choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.y <= choosen_point.y:
            if point.z >= choosen_point.z:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.y <= choosen_point.y:
            if point.z <= choosen_point.z:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    return new_order



def Rit_Order(points):
    #in: list of 4 points
    #out: list of 3 points clockwise order

    new_order = []

    choosen_point = None

    for point in points:
        if choosen_point is not None:
            if point.z >= choosen_point.z:
                if point.y <= choosen_point.y:
                    choosen_point = point
        else:
            choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.z >= choosen_point.z:
            if point.y >= choosen_point.y:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.z <= choosen_point.z:
            if point.y >= choosen_point.y:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    return new_order



def Fwd_Order(points):
    #in: list of 4 points
    #out: list of 3 points clockwise order

    new_order = []

    choosen_point = None

    for point in points:
        if choosen_point is not None:
            if point.z >= choosen_point.z:
                if point.x >= choosen_point.x:
                    choosen_point = point
        else:
            choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.z >= choosen_point.z:
            if point.x <= choosen_point.x:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.z <= choosen_point.z:
            if point.x <= choosen_point.x:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    return new_order



def Bwd_Order(points):
    #in: list of 4 points
    #out: list of 3 points clockwise order

    new_order = []

    choosen_point = None

    for point in points:
        if choosen_point is not None:
            if point.z >= choosen_point.z:
                if point.x <= choosen_point.x:
                    choosen_point = point
        else:
            choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.z >= choosen_point.z:
            if point.x >= choosen_point.x:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    for point in points:
        if point.z <= choosen_point.z:
            if point.x >= choosen_point.x:
                choosen_point = point

        pass
    new_order.append(choosen_point)

    return new_order




