from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # snake.color = food.pencolor()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()
    # print(food.pencolor())

screen.exitonclick()
