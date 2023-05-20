'''
2023 05 20
정우진
터틀을 이용한 다각형 그리기
그리기 원하는 다각형을 입력 받아서 해당하는 다각형 그리기
한변 길이는 100
'''
import turtle
t=turtle.Turtle()
ver=turtle.textinput('다각형','원하는 다각형의 꼭짓점 수')
co=turtle.textinput('색상','색상 입력')
ver=int(ver)
t.color(co)

t.begin_fill()
for i in range(ver):
    t.forward(100)
    t.left(360/ver)
t.end_fill()

input()