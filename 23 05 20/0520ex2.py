'''
2023 05 20
정우진
turtle 스파이덜 그리기
'''

import turtle #터틀 모듈을 프로그램에 추가

colors=['white','purple','blue','dark blue','grey','light blue'] #
t=turtle.Turtle() #터틀 모듈의 별명짓기(t)

turtle.bgcolor('black')
t.speed(50)
t.width(2)
length=10

while length<1000:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length+=5

input()
