import simple_struct
import Standards
import brush_gen




class Story:

    def __init__(self, floor = "", walls = [], stairs = [], extraBrushes = []):

        self.str = ""
        if floor != "":
            self.str += floor.str
        self.walls = walls
        for wall in walls:
            self.str += wall.str
        if stairs != []:
            for case in stairs:
                self.str += case.str
        if extraBrushes != None:
            for arg in extraBrushes:
                if arg.str is not None:
                    self.str += arg.str

        pass
    def __str__(self):
        return self.str

    pass


class Building:

    def __init__(self, stories, *args):

        self.stories = stories
        self.str = ""
        for story in stories:
            self.str += story.str


        pass

    def __str__(self):
        return self.str

    pass