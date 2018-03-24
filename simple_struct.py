# -*- coding: utf-8 -*-
from Standards import stairsStandards as s
import Standards
import brush_gen
import dotmap_types

class Stairs:
    # generate stairs
    def __init__(self, min_point, height, width, run, rotation, floating = True):
        # min point is the minimum point of the stair case (min x, y, z)
        # height is the height of the whole staircase
        # rotation:
        # 0 = x goes up, you go up
        # 1 = Y goes down you go up
        # 2 = X goes down you go up
        # 3 = Y goes up you go up
        # 4 is nothing, you foil
        self.height = height
        self.width = width
        self.dot = min_point
        stairsNum = int(height / s.def_rise)

        self.stairsNum = stairsNum

        if width < s.min_width:
            raise Exception("error: staris width must be above {}".format(s.min_width))
        if height < s.def_rise :
            raise Exception( "error: height should be at least {}".format(s.def_rise))
        if run == "wide":
            run_h = s.wide_run
        elif run == "narrow":
            run_h = s.narrow_run
        elif run == "def":
            run_h = s.def_run
        else:
            raise Exception ("error: run value can be \'wide\', \'narrow\' or \'def\'")

        self.length = run_h * stairsNum

        if rotation == 0:
            self.stairs = upX(min_point, height, width, run_h, floating)
        elif rotation == 1:
            self.stairs = downY(min_point, height, width, run_h, floating)
        elif rotation == 2:
            self.stairs = downX(min_point, height, width, run_h, floating)
        elif rotation == 3:
            self.stairs = upY(min_point, height, width, run_h, floating)
        else:
            raise Exception ("error: invalid rotation value (can be 0-3)")
        self.str = ""
        for stair in self.stairs:
            self.str += stair.str
    pass

# utility functions for Stairs class

def upX(min_point, height, width, run, floating):

    stairsNum = int(height / s.def_rise)
    stairs = []
    if floating:
        for stair in range(stairsNum):
            stairs.append(brush_gen.dimensionMin(min_point, run, width, s.def_rise))
            min_point = min_point + brush_gen.Vec3(run, 0, s.def_rise)

    if not floating:
        i = 0
        for stair in range(stairsNum):
            i += 1
            length = run * (stairsNum - stair)
            stairs.append(brush_gen.dimensionMin(min_point, length, width, s.def_rise))
            min_point = min_point + brush_gen.Vec3(run, 0, s.def_rise)


    return stairs
    pass

def downY(dot, height, width, run, floating):

    stairsNum = int(height / s.def_rise)
    stairs = []

    if floating:
        for stair in range(stairsNum):
            stairs.append(brush_gen.dimensionMaxYMinX(dot, width, run, s.def_rise))
            dot = dot + brush_gen.Vec3(0, 0, s.def_rise)
            dot = dot - brush_gen.Vec3(0, run, 0)

    if not floating:
        i = 0
        for stair in range(stairsNum):
            i += 1
            length = run * (stairsNum - stair)
            stairs.append(brush_gen.dimensionMaxYMinX(dot, width, length, s.def_rise))
            dot = dot + brush_gen.Vec3(0, 0, s.def_rise)
            dot = dot - brush_gen.Vec3(0, run, 0)


    return stairs
    pass

def downX(dot, height, width, run, floating):

    stairsNum = int(height / s.def_rise)
    stairs = []

    if floating:
        for stair in range(stairsNum):
            stairs.append(brush_gen.dimensionMax(dot, run, width, s.def_rise))
            dot = dot + brush_gen.Vec3(0 - run, 0, s.def_rise)

    if not floating:
        i = 0
        for stair in range(stairsNum):
            i += 1
            length = run * (stairsNum - stair)
            stairs.append(brush_gen.dimensionMax(dot, length, width, s.def_rise))
            dot = dot + brush_gen.Vec3(0 - run, 0, s.def_rise)

    return stairs
    pass

def upY(dot, height, width, run, floating):

    stairsNum = int(height / s.def_rise)
    stairs = []

    if floating:
        for stair in range(stairsNum):
            stairs.append(brush_gen.dimensionMaxXMinY(dot, width, run, s.def_rise))
            dot = dot + brush_gen.Vec3(0, run, s.def_rise)
    if not floating:
        i = 0
        for stair in range(stairsNum):
            i += 1
            length = run * (stairsNum - stair)
            stairs.append(brush_gen.dimensionMaxXMinY(dot, width, length, s.def_rise))
            dot = dot + brush_gen.Vec3(0, run, s.def_rise)


    return stairs
    pass


class Winodow:

    #Gets hole dimensions as well as placement on the brush grid
    #window generator.
    #leftdist is the distance  from left side of the wall (looking from the outside
    #traversable is bool

    def __init__(self, leftdist, traversable = None, height = None, width = None, still_height = None):
        #defaulr window
        self.isDoor = False
        self.leftdist = leftdist
        if traversable is None and height is None and width is None and still_height is None:
            self.height = Standards.defWindowsStandards.height
            self.width = Standards.defWindowsStandards.width
            self.still_height = Standards.defWindowsStandards.still_height
        elif height is None and width is None and still_height is None:
            if traversable:
                self.height = Standards.minTraveWindowsStandards.height
                self.width = Standards.minTraveWindowsStandards.width
                self.still_height = Standards.minTraveWindowsStandards.still_height
            if not traversable:
                self.height = Standards.maxBlockedWindowsStandards.height
                self.width = Standards.maxBlockedWindowsStandards.width
                self.still_height = Standards.maxBlockedWindowsStandards.still_height
        else:
            self.leftdist = leftdist
            self.height = height
            self.width = width
            self.still_height = still_height



    pass


class Door:

    #Gets hole dimensions as well as placement on the brush grid
    #generate doors (default traversable wall hole)
    def __init__(self, leftdist, doubleDoor = False):
        self.isDoor = True
        self.leftdist = leftdist
        self.height = Standards.doorsStandards.door_height
        if doubleDoor:
            self.width = Standards.doorsStandards.double_door_width
        else:
            self.width = Standards.doorsStandards.single_door_width

        pass
    pass


class Wall:
    #generates walls

    def __init__(self, dot, outside, thickness, width, height, rotation, holes = []):

        wallValidCheck(holes, thickness, width)

        self.width = width


        holes.sort(key = lambda x: x.leftdist)

        finalHeight = wallHeightManager(outside, height)
        self.height = finalHeight
        if rotation == "north":
            self.wallParts = createNorthWall(dot, thickness, width, finalHeight, holes)
        elif rotation == "south":
            self.wallParts = createSouthWall(dot, thickness, width, finalHeight, holes)
        elif rotation == "east":
            self.wallParts = createEastWall(dot, thickness, width, finalHeight, holes)
        elif rotation == "west":
            self.wallParts = createWestWall(dot, thickness, width, finalHeight, holes)
        else:
            raise Exception("unsupported wall rotation type")

        self.str = ""
        for wallPart in self.wallParts:
            self.str += wallPart.str


    pass


class FloorHole:

    #Gets hole dimensions as well as placement on the brush grid
    def __init__(self, leftdist, downdist, width, length):
        self.leftdist = leftdist
        self.downdist = downdist
        self.width = width
        self.length = length

        pass

    pass


class Floor:

    def __init__(self, dot, length, width, thickness = Standards.floorStandards.def_thickness, openings = []):
        self.dot = dot
        self.length = length
        self.width = width
        self.str = ""
        if openings == []:
            self.floor = brush_gen.dimensionMin(dot, length, width, thickness)
            self.str += self.floor.str
        else:
            brushes = []
            openings.sort(key = lambda x: x.leftdist)
            for opening in openings:
                brushes.append(brush_gen.dimensionMin(dot, opening.leftdist, length, thickness))
                dot = dot + dotmap_types.Vec3(opening.leftdist, 0, 0)
                brushes.append(brush_gen.dimensionMin(dot, opening.width, opening.downdist, thickness))
                brushes.append(brush_gen.dimensionMin(dot + dotmap_types.Vec3(0, opening.downdist + opening.length, 0), opening.width, length - opening.downdist - opening.length, thickness))
                dot = dot + dotmap_types.Vec3(opening.width, 0, 0)
            brushes.append(brush_gen.dimensionMin(dot, width - openings[-1].width - openings[-1].leftdist, length, thickness))
            for brush in brushes:
                self.str += brush.str


    def __str__(self):
        return self.dot.str + " " + str(self.width) + " " + str(self.length)


    pass


# utility functions for the wall class

def wallValidCheck(holes, thickness, width):
    if thickness < Standards.wallsStandards.min_thickness:
            raise Exception("You're not thick enough (that's what she said)")

    #thats bad pythoning. i know. fuck it, not gonna pretend im any good.
    i = 0
    for hole in holes:
        i += 1
        if hole.leftdist < thickness:
            raise Exception("wall hole too close to the left")
        if hole.leftdist + hole.width >= width - thickness:
            raise Exception("wall hole too close to the right")
        for x in range(i, len(holes)):
            if hole.leftdist > holes[x].leftdist and hole.leftdist < holes[x].leftdist + holes[x].width:
                raise Exception("wall holes overlapping")

def wallHeightManager(outside, height):
    if height != "high" and height != "low" and height != "def":
        raise Exception("wall height need to be low def or high")
    if outside and height == "high":
        return Standards.outsideWallsStandards.high_height
    elif outside and height == "def":
        return Standards.outsideWallsStandards.def_height
    elif outside and height == "low":
        return Standards.outsideWallsStandards.low_height
    if not outside and height == "high":
        return Standards.wallsStandards.high_height
    elif not outside and height == "def":
        return Standards.wallsStandards.def_height
    elif not outside and height == "low":
        return Standards.wallsStandards.low_height
    else:
        raise Exception("Error while creating wall")


def createNorthWall(dot, thickness, width, height, holes):
    #north wall is the max Y wall
    brushes = []
    totalLeftdist = 0

    for hole in holes:
        brushes.append(brush_gen.dimensionMax(dot, hole.leftdist, thickness, height))
        totalLeftdist += hole.leftdist + hole.width
        dot = dot - dotmap_types.Vec3(hole.leftdist, 0, 0)
        if hole.isDoor:
            brushes.append(brush_gen.dimensionMax(dot + dotmap_types.Vec3(0, 0, hole.height), hole.width, thickness, height - hole.height))
        elif not hole.isDoor:
            brushes.append(brush_gen.dimensionMax(dot + dotmap_types.Vec3(0, 0, hole.height + hole.still_height), hole.width, thickness, height - hole.height - hole.still_height))
            brushes.append(brush_gen.dimensionMax(dot, hole.width, thickness, hole.still_height))
        dot = dot - dotmap_types.Vec3(hole.width, 0, 0)
    if holes != []:

        brushes.append(brush_gen.dimensionMax(dot, width - totalLeftdist, thickness, height))
    else:
        brushes.append(brush_gen.dimensionMax(dot, width, thickness, height))
    return brushes

    pass


def createSouthWall(dot, thickness, width, height, holes):
    #north wall is the max Y wall
    brushes = []
    totalLeftdist = 0

    for hole in holes:
        brushes.append(brush_gen.dimensionMin(dot, hole.leftdist, thickness, height))
        totalLeftdist += hole.leftdist + hole.width
        dot = dot + dotmap_types.Vec3(hole.leftdist, 0, 0)
        if hole.isDoor:
            brushes.append(brush_gen.dimensionMin(dot + dotmap_types.Vec3(0, 0, hole.height), hole.width, thickness, height - hole.height))
        elif not hole.isDoor:
            brushes.append(brush_gen.dimensionMin(dot + dotmap_types.Vec3(0, 0, hole.height + hole.still_height), hole.width, thickness, height - hole.height - hole.still_height))
            brushes.append(brush_gen.dimensionMin(dot, hole.width, thickness, hole.still_height))
        dot = dot + dotmap_types.Vec3(hole.width, 0, 0)
    if holes != []:
        brushes.append(brush_gen.dimensionMin(dot, width - totalLeftdist, thickness, height))
    else:
        brushes.append(brush_gen.dimensionMin(dot, width, thickness, height))
    return brushes

    pass


def createEastWall(dot, thickness, width, height, holes):
    #north wall is the max Y wall
    brushes = []
    totalLeftdist = 0

    for hole in holes:
        brushes.append(brush_gen.dimensionMaxXMinY(dot, thickness, hole.leftdist, height))
        totalLeftdist += hole.leftdist + hole.width
        dot = dot + dotmap_types.Vec3(0, hole.leftdist, 0)
        if hole.isDoor:
            brushes.append(brush_gen.dimensionMaxXMinY(dot + dotmap_types.Vec3(0, 0, hole.height), thickness, hole.width, height - hole.height))
        elif not hole.isDoor:
            brushes.append(brush_gen.dimensionMaxXMinY(dot + dotmap_types.Vec3(0, 0, hole.height + hole.still_height), thickness, hole.width, height - hole.height - hole.still_height))
            brushes.append(brush_gen.dimensionMaxXMinY(dot, thickness, hole.width, hole.still_height))
        dot = dot + dotmap_types.Vec3(0, hole.width, 0)
    if holes != []:
        brushes.append(brush_gen.dimensionMaxXMinY(dot, thickness,width - totalLeftdist, height))
    else:
        brushes.append(brush_gen.dimensionMaxXMinY(dot, thickness, width, height))
    return brushes

    pass


def createWestWall(dot, thickness, width, height, holes):
    #north wall is the max Y wall
    brushes = []
    totalLeftdist = 0

    for hole in holes:
        brushes.append(brush_gen.dimensionMaxYMinX(dot, thickness, hole.leftdist, height))
        totalLeftdist += hole.leftdist + hole.width
        dot = dot - dotmap_types.Vec3(0, hole.leftdist, 0)
        if hole.isDoor:
            brushes.append(brush_gen.dimensionMaxYMinX(dot + dotmap_types.Vec3(0, 0, hole.height), thickness, hole.width, height - hole.height))
        elif not hole.isDoor:
            brushes.append(brush_gen.dimensionMaxYMinX(dot + dotmap_types.Vec3(0, 0, hole.height + hole.still_height), thickness, hole.width, height - hole.height - hole.still_height))
            brushes.append(brush_gen.dimensionMaxYMinX(dot, thickness, hole.width, hole.still_height))
        dot = dot - dotmap_types.Vec3(0, hole.width, 0)
    if holes != []:
        brushes.append(brush_gen.dimensionMaxYMinX(dot, thickness, width - totalLeftdist, height))
    else:
        brushes.append(brush_gen.dimensionMaxYMinX(dot, thickness, width, height))
    return brushes

    pass