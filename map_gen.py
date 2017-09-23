__author__ = 'user'

#A simple test

import dotmap_types
from dotmap_types import Vec3
from dotmap_types import Brush


def main():

    file = open("brush.map", "w")
    str = "// entity 0\r\n"
    str += "{\r\n"
    str += "\"classname\" \"worldspawn\"\r\n"

    str += Brush(Vec3(0, 0, 0), Vec3(10, 10, 10), Vec3(10, 0, 0), Vec3(0, 10, 0), Vec3(0, 0, 10), Vec3(10, 10, 0), Vec3(10, 0, 10), Vec3(0, 10, 10)).str

    str += "}\r\n"

    file.write(str)

    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()