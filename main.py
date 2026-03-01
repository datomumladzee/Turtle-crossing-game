import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


def start_game():
    scoreboard.reset_scoreboard()
    car_manager.reset_cars()
    player.go_to_start()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_cars()
        car_manager.move()

        # Detect car collision
        if car_manager.detect_collision(player):
            game_is_on = False
            scoreboard.game_over()
            screen.onkey(start_game, "r")

        # Detect successful crossing
        if player.ycor() > 280:
            player.go_to_start()
            car_manager.increase_speed()
            scoreboard.increase_level()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(start_game, "r")

# Start the first game
start_game()

screen.exitonclick()


