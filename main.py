from snake import Snake
from turtle import Turtle,Screen
from new_food import Food
from scoreboard import scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.new_foodie()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or  snake.head.ycor()>280 or snake.head.ycor()< -280:
        score.reset()
    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
           score.reset()
           snake.reset()









screen.exitonclick()