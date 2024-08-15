from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.goto(0,270)


        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}", align="center", font=("Arial", 24, "normal"))
    def reset(self):
        if self.high_score<self.score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update()
    
    def increase_score(self):
        self.score+=1

        self.update()


