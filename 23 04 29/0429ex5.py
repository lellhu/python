'''
2023 04 29
정우진
 조건이 여러개인 경우의 조건문 연습
 #문제 정의
    점수가 90이상이면 "A"
    점수가 80이상 90미만이면 "B"
    점수가 70이상 80미만이면 "C"
    점수가 70미만이면 "F"를 출력하는 프로그램
#문제 분석
    변수:점수(jumsu)
#알고리즘
    1. 변수 선언
        jumsu변수에 성적 입력 받기
    2.프로그램 논리(선택:if~elif~else)
        (조건식) if jumsu>=90:
                    (참) "A"
                elif jumsu>=80
                    (참) "B"
                elif jumsu>=70
                    (참) "C"
                else:
                    "F"
'''

jumsu=int(input('점수 입력:')) #정수 입력

if jumsu>=90: #조건식1
    print("A") #조건1 참일때만 실행
elif jumsu>=80: #조건식2
    print('B') #조건2 참일때만 실행
elif jumsu>=70: #조건식3
    print('c') #조건3 참일때만 실행
else:
    print('F') #모두 거짓일 때만 실행
