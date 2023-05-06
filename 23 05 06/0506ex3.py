'''
2023 05 06
정우진
반복문 - for
'''
#시퀀스 변수로 반복문 범위 정하기

for i in [1,2,3,4,5,6,7,8,9,10]: #반복 조건
    print(i, end=' ') #i 출력

print() #줄바꿈

#range() 함수로 반복문 범위 정하기
for i in range(1,11): #반복 조건
    print(i, end=' ') #i 출력

print() #줄바꿈

#1~10까지 합계를 출력 하시오.
sum=0 #합계 저장

for num in range(1,11): #반복 변수
    sum=sum+num #합계 구하기

print('1~10까지의 합계는 {}이다.'.format(sum))

#1~입력받은 숫자까지 합계 구하기
hab=0
num2=int(input('숫자 입력:'))

for num1 in range(1,num2):
    hab=hab+num1

print('1~{}까지의 합계는 {}이다.'.format(num2,hab))
