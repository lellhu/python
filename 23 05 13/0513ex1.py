'''
2023 05 13
정우진
#문제 정의
    출력을 원하는 단을 입력받아서 구구단 출력하기
#문제분석
    변수:단(dan),반복횟수(su)
#알고리즘
    1. 변수 초기화
        dan 변수에 정수 입력
    2.논리(반복-while)
        (반복 조건)
'''
#while문
su=1
dan=int(input('외울 단:'))
print('**{}단**'.format(dan))

while su<=9:
    print('{}*{}={}'.format(dan,su,dan*su))
    su=su+1

#for문

dan=int(input('외울 단:'))
print('**{}단**'.format(dan))

for su in range(1,10):
    print('{}*{}={}'.format(dan,su,dan*su))
    su=su+1
    