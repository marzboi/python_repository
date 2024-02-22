from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.l_score} | {self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        if player == 'left':
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.update_scoreboard()
