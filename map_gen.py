__author__ = 'user'

#A simple test

import dotmap_types
from dotmap_types import header
from dotmap_types import Vec3
import Standards
from dotmap_types import Brush
import brush_gen
import simple_struct
import generators
from tkinter import *

def click_me():
    print("a")
    pass

def main():

    #win = Tk()
    #win.title("Map Generator")
    #Label(win, text="number of stories:").grid(column=0, row=0)
    #action = Button(win, text="Next", command=click_me)
    #action.grid(column=1, row = 0)
#
    #win.mainloop()

    file = open("brush.map", "w")
    #You need this for the map file to work
    str = header.entity
    str += header.open
    str += header.classname

    #give the Brush() 8 point, and it shall give you a string
    story = generators.generate_building(Vec3(-100, -100, 0), 300, 300, "high", ["stairRoomStart", "stairRoomMid"])

    floorHole = simple_struct.FloorHole(1000 - Standards.wallsStandards.min_thickness - 20, 1000 - Standards.wallsStandards.min_thickness - 240, 20, 240)
    floor = simple_struct.Floor(Vec3(0,0,0) - dotmap_types.Vec3(0, 0, Standards.floorStandards.def_thickness), 1000, 1000, Standards.floorStandards.def_thickness, [floorHole])

    str += story.str

    #this is also needed
    str += header.close

    #DA
    file.write(str)



if __name__ == '__main__':
    main()