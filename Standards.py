# -*- coding: utf-8 -*-
#standards for the BO3 game
#after each class there is a class object which should be called instead of the class


class Stairs:

    def __init__(self):

        self.min_width = 80
        self.def_rise = 8
        self.def_run = 12
        self.narrow_run = 8
        self.wide_run = 16

        pass

    pass

stairsStandards = Stairs()

class Walls:

    def __init__(self):

        self.min_thickness = 8
        self.def_height = 112
        self.high_height = 144
        self.low_height = 96

        pass

    pass

wallsStandards = Walls()

class OutsideWalls:

    def __init__(self):

        self.min_thickness = 8
        self.def_height = 128
        self.high_height = 160
        self.low_height = 128

        pass
    pass

outsideWallsStandards = OutsideWalls()

class Doors:

    def __init__(self):

        self.door_height = 96
        self.single_door_width = 56
        self.double_door_width = 110

        pass
    pass

doorsStandards = Doors()

class DefWindows:

    def __init__(self):

        self.width = 56
        self.height = 64
        self.still_height  = 32

        pass
    pass

defWindowsStandards = DefWindows()

class MinTraveWindows:

    def __init__(self):

        self.width = 40
        self.height = 60
        self.still_height  = 32

        pass
    pass

minTraveWindowsStandards = MinTraveWindows()

class MaxBlockedWindows:

    def __init__(self):

        self.width = 32
        self.height = 32
        self.still_height  = 48

        pass
    pass

maxBlockedWindowsStandards = MaxBlockedWindows()

class Floor:

    def __init__(self):
        self.def_thickness = 16
    pass

floorStandards = Floor()