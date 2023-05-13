'''
2023 05 13
정우진
#문제정의
    정수 2개와 연산자(+,-,*,/)1개를 입력 받아서 사칙연산
    을 수행하는 계산기 프로그램 만들기
#문제 분석
    변수:첫번째 수(num1),두번째 수(num2) 연산자(buho)
#알고리즘
    1.첫번째 수와 연산자,두번째 수에 값입력 받기
        num1=int(input('첫번째 수:'))
        buho=input('연산자 입력(+,-,*,/,**):')
        num2=int(input('두번째 수:'))
    2.계산하기
'''
num1=int(input('첫번째 수:'))
buho=input('연산자 입력(+,-,*,/,**):')
num2=int(input('두번째 수:'))

if buho=='+':
    print('{}+{}={}'.format(num1,num2,num1+num2))
elif buho=='-':
    print('{}-{}={}'.format(num1,num2,num1-num2))
elif buho=='*':
    print('{}*{}={}'.format(num1,num2,num1*num2))
elif buho=='/':
    print('{}/{}={}'.format(num1,num2,num1/num2))
elif buho=='**':
    print('{}**{}={}'.format(num1,num2,num1**num2))
else:
    print('연산자 없음.')