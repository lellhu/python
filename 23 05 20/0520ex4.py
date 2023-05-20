'''
2023 05 20
정우진
터틀 활용2-입력, 색채우기
'''
import turtle
t=turtle.Turtle()
co=turtle.textinput('색상','색상입력')
rad=turtle.numinput('반지름','반지름의 길이')
t.color(co)

t.begin_fill() #색 채우기 시작
t.circle(rad) #원 그리기
t.end_fill() #색 채우기 끝

input()