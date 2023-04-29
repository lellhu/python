num1=int(input('첫번째 수:'))
num2=int(input('두번째 수:'))
buho=input('연산자 입력(1=+ 2=- 3=* 4=/ 5=**):')

if buho=='1':
    print(num1+num2)
elif buho=='2':
    print(num1-num2)
elif buho=='3':
    print(num1*num2)
elif buho=='4':
    print(num1/num2)
elif buho=='5':
    print(num1**num2)
else:
    print('1부터 5까지 숫자 이외에는 입력 불가합니다.')