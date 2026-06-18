from turtle import Screen, Turtle

from ball import Ball
from score import Score
from field import Field
from player import Player
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.tracer(0)
game_over = Turtle()
game_over.color('white')
game_over.hideturtle()

field = Field()

score_1 = Score(-80, 345)
score_2 = Score(80, 345)

player_1 = Player(-370, 0)
player_2 = Player(370, 0)

ball = Ball()

screen.listen()

keys = {
    'w': False,
    's': False,
    'Up': False,
    'Down': False,
    }

def key_press(key):
    keys[key] = True

def key_release(key):
    keys[key] = False

screen.listen()

for k1 in keys:
    screen.onkeypress(lambda k=k1: key_press(k), k1)

for k2 in keys:
    screen.onkeyrelease(lambda k=k2: key_release(k), k2)

waiting = True
game_is_on = True

def start_game():
    global game_is_on, waiting, moves
    waiting = False

screen.onkeypress(start_game, 'space')

while game_is_on:
    if waiting:
        screen.update()
        time.sleep(0.01)
        continue

    if keys['w']:
        player_1.move_up()
    if keys['s']:
        player_1.move_down()
    if keys['Up']:
        player_2.move_up()
    if keys['Down']:
        player_2.move_down()

    ball.move()
    ball.hit_x()
    ball.hit_y(player_1.xcor(), player_1.ycor())
    ball.hit_y(player_2.xcor(), player_2.ycor())

    if ball.xcor() >= 390:
        score_1.increase_score()
        ball.reset_ball()
        waiting = True
    if ball.xcor() <= -390:
        score_2.increase_score()
        ball.reset_ball()
        waiting = True
    if score_1.score == 10 or score_2.score == 10:
        ball.hideturtle()
        game_over.write('Game Over!', align='center', font=('Courier', 40, 'bold'))
        game_is_on = False

    screen.update()
    time.sleep(0.01)

screen.exitonclick()