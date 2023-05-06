'''
2023 05 06
정우진
반복문 - while 
'''
#1~10까지 출력하기

i=1 #반복 변수 초기화
while i<=10: #반복 조건
    print(i, end=' ') #i 출력
    i=i+1 #i 1씩 증가(증감식)
print()

#1~10까지 합계 구하기
su1=1
hab=0

while su1<=10:
    hab=hab+su1
    su1=su1+1

print(hab)

#1~입력받은 숫자 까지 합계 구하기
su1=1
hab=0
key=int(input('입력할 수:'))

while su1<=key:
    hab=hab+su1
    su1=su1+1

print(hab)