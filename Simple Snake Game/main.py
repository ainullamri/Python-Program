from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

#screen set up
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Ular-ularnya Inul")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
scoreboard = ScoreBoard()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    #detect collision with body or tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
