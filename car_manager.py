from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = [] # create a List of Cars
    
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1: 
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)




# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.createCars()
        
        
#     def createCars(self):
#         """Create a Car on a random Y Position"""
#         self.randomYPos = random.randint(-250, 250)
#         self.randomColor = random.randrange(0, len(COLORS))

#         self.penup()
#         self.setheading(-180)
#         self.shape("square")
#         self.color(COLORS[self.randomColor])
#         self.shapesize(stretch_len=2)
#         self.goto(x=250 ,y=self.randomYPos)
    
#     def moveCars(self):
#         """Move Cars at the Start with a Movement Speed of 5"""
#         self.forward(STARTING_MOVE_DISTANCE)
    
#     # TODO 
#     def nextLevel(self):
#         """increase Car Movement Speed and increase the Amount of Cars"""
#         pass