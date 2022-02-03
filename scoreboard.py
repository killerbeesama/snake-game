from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.scoreboard = 0
        self.score()


    def score(self):
        self.write(f'SCORE:  {self.scoreboard}',align='center', font=('Arial', 20, 'bold'))


    def update_score(self):
        self.clear()
        self.scoreboard += 1
        self.score()


    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER',align='center', font=('Arial', 20, 'bold'))

