'''
2023 04 29
정우진
#문제정의
    숫자를 입력 받아서, 양수, 음수, 0을 구분하는 프로그램 만들기
#문제 분석
    변수:su
#알고리즘
    1.변수 선언
        su변수에 숫자 입력 받기
    2.프로그램 논리(선택:if~elif~else)
    if su>0:
        "양수"
    elif su<0:
        "음수
    else:
        "0"
'''

su=int(input('숫자 입력:')) #su변수에 값 입력

if su>0: #조건문 1
    print('양수') #조건문1이 참일때 실행
elif su<0: #조건문 2
    print('음수') #조건문2가 참일때 실행
else:
    print('0') #조건문이 모두 거짓일때 실행