from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.createCars(280, 10)

    def createCars(self, xPos, yPos):
        self.penup()
        self.setheading(-180)
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_len=2)
        self.goto(xPos, yPos)
        