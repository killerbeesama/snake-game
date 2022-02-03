from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()


screen.onkeypress(snake.left,'a')
screen.onkeypress(snake.right,'d')
screen.onkeypress(snake.up,'w')
screen.onkeypress(snake.down,'s')

food = Food()
scoreboard = ScoreBoard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    if snake.head.distance(food) < 15:
        food.update_food()
        scoreboard.update_score()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    for turtles in snake.new_turtle:
        '''if the turtles in new_turtle is new_turtle[0] we are going to pass else the the head has collided with the body and also the snake head moving distance should be more than 10 or 10 else it will result in being too close to the body making the condition true'''
        if turtles == snake.head:
            pass
        elif snake.head.distance(turtles) < 10:
            game_on = False
            scoreboard.game_over()

    
screen.exitonclick()