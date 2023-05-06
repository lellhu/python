'''
2023 05 06
정우진
시퀀스 자료형의 특징
'''
from cgi import print_arguments


str='once' #문자열 자료형
str_list=['t','w','i','c','e'] #리스트 자료형
num_tup=(5,3,2,1,4) #튜플 자료형
num1=[1,2,3]
num2=[4,5,6]
i=3

print(str[3])  #인덱싱-str변수의 인덱스 3 위치 원소 추출
print(str_list[2:]) #슬라이싱-인덱스 2~끝까지 추출
print(num_tup[:3]) #슬라이싱-처음부터 인덳, 2까지 추출

print('str변수의 길이는 {}이다.'.format(len(str)))
print('문자 "s"는 str_list에 있는 원소인가? {}'.format('s' in str_list))
print('once'*3) #문자열 'once' 3번 반복
print(num1+num2) #리스트 변수 2개 연결하기

