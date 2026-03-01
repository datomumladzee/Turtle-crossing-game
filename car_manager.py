import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_cars(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-240, 240)
            x = 300
            new_car.goto(x, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def detect_collision(self, player):
        for car in self.all_cars:

            car_half_width = 20
            car_half_height = 10

            player_half_size = 10

            x_overlap = abs(car.xcor() - player.xcor()) < (car_half_width + player_half_size-2)
            y_overlap = abs(car.ycor() - player.ycor()) < (car_half_height + player_half_size-2)

            if x_overlap and y_overlap:
                return True

        return False

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def reset_cars(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


