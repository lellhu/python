'''
2023 05 20
정우진
turtle 모듈 활용하기-그래픽 모듈
'''
import turtle #터틀 모듈을 프로그램에 추가
t=turtle.Turtle() #터틀 모듈의 별명짓기(t)
t.shape("turtle") #커서의 모양

t.forward(100) #앞으로 전진
t.left(90) #왼쪽 90도 회전
t.forward(50) #앞으로 전진
t.left(90) #왼쪽 90도 회전
t.forward(100) #앞으로 전진
t.left(90) #왼쪽 90도 회전
t.forward(50) #앞으로 전진
t.left(90) #왼쪽 90도 회전

#반복문 이용한 직사각형 그리기
for i in range(2):
    t.forward(100) #앞으로 전진
    t.left(90) #왼쪽 90도 회전
    t.forward(50) #앞으로 전진
    t.left(90) #왼쪽 90도 회전

#반복문 이용한 정사각형 그리기
for i in range(4):
    t.forward(50)
    t.left(90)

#정삼각형 그리기
for i in range(3):
    t.forward(100)
    t.left(120)

#반지름이 100인 원 그리기
t.circle(100)

#오각형 그리기
for i in range(5):
    t.forward(100)
    t.left(72)

input() #입력 대기
