'''
2023 05 13
정우진
#문제정의
    정수를 입력받아서 직각삼각형 별 출력하기
#문제분석
    변수:정수(num),줄반복(i),별찍기반복(j)
#알고리즘
    1.변수 초기화
        num 변수에 정수 입력
    2.논리(중첩반복)
        (줄반복)for i in range(1,num+1):
            (별 찍기 반복) for j in range(1,i+1):
'''
num=int(input('반복 횟수 입력:'))

for i in range(1,num+1): #줄 반복
    for j in range(1,i+1): #별 찍기 반복
        print('*',end=' ') #별 출력

    print() # 줄바꿈