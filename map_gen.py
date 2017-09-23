__author__ = 'user'

#A simple test

import dotmap_types
from dotmap_types import Vec3
from dotmap_types import Brush


def main():

    file = open("brush.map", "w")

    #You need this for the map file to work
    str = "// entity 0\r\n"
    str += "{\r\n"
    str += "\"classname\" \"worldspawn\"\r\n"

    #give the Brush() 8 point, and it shall give you a string
    str += Brush(Vec3(0, 0, 0), Vec3(10, 10, 10), Vec3(10, 0, 0), Vec3(0, 10, 0), Vec3(0, 0, 10), Vec3(10, 10, 0), Vec3(10, 0, 10), Vec3(0, 10, 10)).str

    #this is also needed
    str += "}\r\n"

    #DA
    file.write(str)



if __name__ == '__main__':
    main()