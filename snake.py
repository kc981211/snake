from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.bodies = []
        self.create_snake()
        self.head = self.bodies[0]
        # self.heading = self.head.heading()
        # -- Why can't the correct heading be stored in self.heading?
        #    It's because everytime 'snake' object is called, the heading is also initialised, so the heading will
        #    always be 0.0 in 'self.heading'.

    def create_snake(self):
        for starting_position in STARTING_POSITIONS:
            self.add_segment(starting_position)

    def add_segment(self, position):
        new_body = Turtle(shape="square")
        new_body.penup()
        new_body.color("white")
        new_body.goto(position)
        self.bodies.append(new_body)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.bodies[-1].position())

    def move(self):
        # Moving the snake from the last body segment(the tail). The last segment will move to the coordinates of
        # the previous segment to create the movement. Then the first segment(the head) will move forward.
        # e.g. 3-->2, 2-->1, 1-->forward(20), then loop

        # range(start, end[*not inclusive], step)
        for i in range(len(self.bodies)-1, 0, -1):
            self.bodies[i].goto(self.bodies[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
