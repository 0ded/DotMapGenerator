import simple_struct
import complex_struct
import dotmap_types
import Standards
import brush_gen

def generate_story(dot, width, length, height, storyMode = ""):

    h = simple_struct.wallHeightManager(False, height)
    stairsYDot =  length - (Standards.wallsStandards.min_thickness) - (Standards.stairsStandards.def_run*(int((h + Standards.floorStandards.def_thickness) / Standards.stairsStandards.def_rise) + 4))
    extraBrushes = []

    if storyMode == "stairRoomStart":
        wall1_holes = generate_holes("SingleDoor", "", width)
        wall2_holes = generate_holes("", "", width)
        wall3_holes = generate_holes("", "", length)
        wall4_holes = generate_holes("", "", length)
        walls = generate_4_walls(dot, width, length, height, wall1_holes, wall2_holes, wall3_holes, wall4_holes)
        stairsXDot = width - Standards.wallsStandards.min_thickness
        stairsYDot = length - (Standards.wallsStandards.min_thickness) - (Standards.stairsStandards.def_run*(int((h/2 + Standards.floorStandards.def_thickness) / Standards.stairsStandards.def_rise) + 4))

        stairsDot = dot + dotmap_types.Vec3(stairsXDot, stairsYDot, 0)

        stairs = [simple_struct.Stairs(stairsDot, walls[0].height/2 , Standards.stairsStandards.min_width, "def", 3)]

        stairsYDot = (Standards.wallsStandards.min_thickness) + (Standards.stairsStandards.def_run*(int((h/2 + Standards.floorStandards.def_thickness) / Standards.stairsStandards.def_rise) + 4))
        stairsDot = dotmap_types.Vec3(dot.x + Standards.wallsStandards.min_thickness, dot.y + stairsYDot, dot.z + h/2 + Standards.floorStandards.def_thickness)

        stairs.append(simple_struct.Stairs(stairsDot, walls[0].height/2 - Standards.floorStandards.def_thickness, Standards.stairsStandards.min_width, "def", 1))

        floor = simple_struct.Floor(dot - dotmap_types.Vec3(0, 0, Standards.floorStandards.def_thickness), width, length, Standards.floorStandards.def_thickness)

        story = complex_struct.Story(floor, walls, stairs)

    if storyMode == "stairRoomMid":

        wall1_holes = generate_holes("SingleDoor", "", width)
        wall2_holes = generate_holes("", "", width)
        wall3_holes = generate_holes("", "", length)
        wall4_holes = generate_holes("", "", length)
        walls = generate_4_walls(dot, width, length, height, wall1_holes, wall2_holes, wall3_holes, wall4_holes)
        stairsXDot = width - Standards.wallsStandards.min_thickness
        stairsYDot = length - (Standards.wallsStandards.min_thickness) - (Standards.stairsStandards.def_run*(int((h/2 + Standards.floorStandards.def_thickness) / Standards.stairsStandards.def_rise) + 4))

        stairsDot = dot + dotmap_types.Vec3(stairsXDot, stairsYDot, Standards.floorStandards.def_thickness)

        stairs = [simple_struct.Stairs(stairsDot, walls[0].height/2 , Standards.stairsStandards.min_width, "def", 3)]

        stairsYDot = (Standards.wallsStandards.min_thickness) + (Standards.stairsStandards.def_run*(int((h/2 + Standards.floorStandards.def_thickness) / Standards.stairsStandards.def_rise) + 4))
        stairsDot = dotmap_types.Vec3(dot.x + Standards.wallsStandards.min_thickness, dot.y + stairsYDot, dot.z + h/2 + Standards.floorStandards.def_thickness)

        stairs.append(simple_struct.Stairs(stairsDot, walls[0].height/2 - Standards.floorStandards.def_thickness, Standards.stairsStandards.min_width, "def", 1))

        startHoleY = stairs[1].dot.y - stairs[1].length - dot.y
        floorHole = [simple_struct.FloorHole(Standards.wallsStandards.min_thickness, startHoleY, width - Standards.wallsStandards.min_thickness* 2, length - startHoleY - Standards.wallsStandards.min_thickness)]

        floor = simple_struct.Floor(dot - dotmap_types.Vec3(0, 0, Standards.floorStandards.def_thickness), width, length, Standards.floorStandards.def_thickness, floorHole)

        print(floor)

        eBX = stairs[0].dot.x - dot.x - stairs[0].width
        eBY = stairs[1].dot.y - stairs[1].length - dot.y
        eBY2 = stairs[0].dot.y - dot.y - eBY
        eBD = dot + dotmap_types.Vec3(eBX, eBY, -Standards.floorStandards.def_thickness)

        extraBrushes.append(brush_gen.dimensionMin(eBD, stairs[0].width, eBY2, Standards.floorStandards.def_thickness))

        eBX = Standards.wallsStandards.min_thickness + dot.x
        eBY = stairs[0].dot.y + stairs[0].length + dot.y
        eBZ = dot.z + stairs[0].height
        eBY2 = length - Standards.wallsStandards.min_thickness - eBY

        extraBrushes.append(brush_gen.dimensionMin(dot + dotmap_types.Vec3(eBX, eBY, eBZ), width - Standards.wallsStandards.min_thickness* 2, eBY2, Standards.floorStandards.def_thickness))

        story = complex_struct.Story(floor, walls, stairs, extraBrushes)

    if storyMode == "simple_entance_up":
        wall1_holes = generate_holes("Main", "", width)
        wall2_holes = generate_holes("", "Rooms", width)
        wall3_holes = generate_holes("", "Rooms", length)
        wall4_holes = generate_holes("", "Rooms", length)
        walls = generate_4_walls(dot, width, length, height, wall1_holes, wall2_holes, wall3_holes, wall4_holes)
        floor = simple_struct.Floor(dot - dotmap_types.Vec3(0, 0, Standards.floorStandards.def_thickness), width, length, Standards.floorStandards.def_thickness)

        stairsDot = dot + dotmap_types.Vec3(width - Standards.wallsStandards.min_thickness, stairsYDot, 0)

        stairs = [simple_struct.Stairs(stairsDot, walls[0].height + Standards.floorStandards.def_thickness, Standards.stairsStandards.min_width, "def", 3)]

        story = complex_struct.Story(floor, walls, stairs)
    if storyMode == "floor_only":
        floor = simple_struct.Floor(dot - dotmap_types.Vec3(0, 0, Standards.floorStandards.def_thickness), width, length, Standards.floorStandards.def_thickness)
        story = complex_struct.Story(floor)

    if storyMode == "only_windows_mid":
        wall1_holes = generate_holes("", "Rooms", width)
        wall2_holes = generate_holes("", "Rooms", width)
        wall3_holes = generate_holes("", "Rooms", length)
        wall4_holes = generate_holes("", "Rooms", length)
        walls = generate_4_walls(dot, width, length, height, wall1_holes, wall2_holes, wall3_holes, wall4_holes)

        stairsDot = dot + dotmap_types.Vec3(width - Standards.wallsStandards.min_thickness, stairsYDot, 0)

        stairs = [simple_struct.Stairs(stairsDot, walls[0].height + Standards.floorStandards.def_thickness, Standards.stairsStandards.min_width, "def", 3)]


        floorHole = simple_struct.FloorHole(width - Standards.wallsStandards.min_thickness - stairs[0].width, stairsYDot, stairs[0].width, stairs[0].length)
        floor = simple_struct.Floor(dot - dotmap_types.Vec3(0, 0, Standards.floorStandards.def_thickness), width, length, Standards.floorStandards.def_thickness, [floorHole])

        story = complex_struct.Story(floor, walls, stairs)
    if storyMode == "buncker_mid":
        wall1_holes = generate_holes("", "wide", width)
        wall2_holes = generate_holes("", "wide", width)
        wall3_holes = generate_holes("", "wide", length)
        wall4_holes = generate_holes("", "wide", length)
        walls = generate_4_walls(dot, width, length, height, wall1_holes, wall2_holes, wall3_holes, wall4_holes)

        stairsDot = dot + dotmap_types.Vec3(width - Standards.wallsStandards.min_thickness, stairsYDot, 0)

        stairs = [simple_struct.Stairs(stairsDot, walls[0].height + Standards.floorStandards.def_thickness, Standards.stairsStandards.min_width, "def", 3)]



        floorHole = simple_struct.FloorHole(width - Standards.wallsStandards.min_thickness - stairs[0].width, stairsYDot, stairs[0].width, stairs[0].length)
        floor = simple_struct.Floor(dot - dotmap_types.Vec3(0, 0, Standards.floorStandards.def_thickness), width, length, Standards.floorStandards.def_thickness, [floorHole])

        story = complex_struct.Story(floor, walls, stairs)
    if storyMode == "buncker_first":
        wall1_holes = generate_holes("Main", "", width)
        wall2_holes = generate_holes("", "wide", width)
        wall3_holes = generate_holes("", "wide", length)
        wall4_holes = generate_holes("", "wide", length)
        walls = generate_4_walls(dot, width, length, height, wall1_holes, wall2_holes, wall3_holes, wall4_holes)
        floor = simple_struct.Floor(dot - dotmap_types.Vec3(0, 0, Standards.floorStandards.def_thickness), width, length, Standards.floorStandards.def_thickness)

        stairsDot = dot + dotmap_types.Vec3(width - Standards.wallsStandards.min_thickness, stairsYDot, 0)

        stairs = [simple_struct.Stairs(stairsDot, walls[0].height + Standards.floorStandards.def_thickness, Standards.stairsStandards.min_width, "def", 3)]

        story = complex_struct.Story(floor, walls, stairs)
    return story


def generate_4_walls(dot, width, length, height, wall1_holes, wall2_holes, wall3_holes, wall4_holes):

    walls = []
    walls.append(simple_struct.Wall(dot, False, Standards.wallsStandards.min_thickness, width, height, "south", wall1_holes))
    walls.append(simple_struct.Wall(dot + dotmap_types.Vec3(width, length, 0), False, Standards.wallsStandards.min_thickness, width, height, "north", wall2_holes))
    walls.append(simple_struct.Wall(dot + dotmap_types.Vec3(width, 0, 0), False, Standards.wallsStandards.min_thickness, length, height, "east", wall3_holes))
    walls.append(simple_struct.Wall(dot + dotmap_types.Vec3(0, length, 0), False, Standards.wallsStandards.min_thickness, length, height, "west", wall4_holes))

    return walls

def generate_holes(entranceMode, windowMode, width):

    holes = []

    if entranceMode == "Main":
        w = width /2 - Standards.doorsStandards.double_door_width/2
        holes.append(simple_struct.Door(w, True))

    if entranceMode == "SingleDoor":
        w = width /2 - Standards.doorsStandards.single_door_width/2
        holes.append(simple_struct.Door(w, False))

    if windowMode == "Rooms":
        windowNum = int(width / (Standards.defWindowsStandards.width*2)) # make sure got enough space between the windows
        for i in range(windowNum):
            #holes.append(simple_struct.Winodow(Standards.wallsStandards.min_thickness + (Standards.defWindowsStandards.width*i) + Standards.defWindowsStandards.width * 0.2))
            holes.append(simple_struct.Winodow(Standards.defWindowsStandards.width))

    elif windowMode == "wide":
        holes.append(simple_struct.Winodow(Standards.wallsStandards.min_thickness, False, Standards.maxBlockedWindowsStandards.height, width - Standards.wallsStandards.min_thickness*3, Standards.maxBlockedWindowsStandards.still_height))

    return holes


    pass

def generate_building(dot, width, length, height, storyModes):
    stories = []
    i = 0
    for storyMode in storyModes:
        if i > 0:
            stories.append(generate_story(dot + dotmap_types.Vec3(0, 0, i*(stories[-1].walls[0].height + Standards.floorStandards.def_thickness)), width, length, height, storyMode))
        if i == 0:
            stories.append(generate_story(dot , width, length, height, storyMode))
        i += 1
    return complex_struct.Building(stories)

    pass

def generate_stairCase(dot, floorNum, storyHeight):

    pass