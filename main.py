from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# # TODO : 1 Create a snake body
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# TODO : 2 MOve the snake body
game_is_on = True
while game_is_on:
    screen.update()  # updates the screen after all the segments are moved
    time.sleep(0.2)
    snake.move()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        if food.dot_number % 3 == 0:
            food.big_food()
            scoreboard.turtle_score(size="small")
        elif (food.dot_number-1) % 3 == 0 and (food.dot_number-1) != 0:
            scoreboard.turtle_score(size="large")
            food.small_food()
        else:
            food.small_food()
            scoreboard.turtle_score(size="small")
        food.refresh()
        snake.extend()

    # detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        food.reset()


    # detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            food.reset()


screen.exitonclick()