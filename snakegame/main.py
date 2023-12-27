import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
add = 0.1
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    speed = time.sleep(add)

    snake.move()
    food
    scoreboard

    #detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        #add score
        scoreboard.add_score()
        #extend snake
        snake.extend()
        snake.extend()
        if add > .05:
            add -= .005

    #detect collision with wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.gameover()

    #detect collision with tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
                game_is_on = False
                scoreboard.gameover()






screen.exitonclick()
