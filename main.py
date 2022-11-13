from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
food.refresh()
screen.listen()

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increasescore()
        scoreboard.refresh()
        snake.increasesize()
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
    for seg in snake.segments:
        if seg == snake.head:
            pass
        else:
            if snake.head.distance(seg)<10:
                game_on = False






gam = Turtle()
gam.penup()
gam.color("white")
gam.write(f"Game Over", align="center", font=('Arial', 25, 'normal'))

screen.exitonclick()
