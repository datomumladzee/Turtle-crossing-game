from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_display()

    def reset_scoreboard(self):
        self.level = 1
        self.update_display()

    def increase_level(self):
        self.level += 1
        self.update_display()

    def update_display(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", align="left", font=("Arial", 14, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER! Press 'R' to Restart", align="center", font=("Arial", 20, "bold"))