from Scoreboard import scoreboard
from turtle import Screen
import time

from Snake import Snake
from Food import food

score=scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

f=food()
snake = Snake()

# Listen for key presses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    if snake.head.distance(f)<15:
        f.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.gameover()
    for segment in snake.segs[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.gameover()
screen.exitonclick()
