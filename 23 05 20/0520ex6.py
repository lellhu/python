'''
2023 05 20
터틀로 집그리기
'''
import turtle
t=turtle.Turtle()

t.color('light yellow')

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.up()
t.goto(0,100)
t.color('red')
t.down()
t.begin_fill()
for i in range (3):
    t.forward(100)
    t.left(120)
t.end_fill()
input()