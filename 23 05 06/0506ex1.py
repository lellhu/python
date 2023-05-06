'''
2023 05 06
정우진
시퀀스 자료형 연습
'''
line_up=[] #원소가 없는 리스트 변수 만들기
line_up.append('거북이') #리스트에 원소 추가하기
print(line_up)

line_up.append('토끼') #리스트의 마지막에 원소 추가하기
print(line_up)

line_up.insert(1,'다람쥐') #인덱스 1 위치에 원소 추가하기
print(line_up)

line_up.remove('거북이') #특정 원소 제거하기
print(line_up)

num_list=[5,3,8,2,10] #리스트 변수
num_list.insert(2,4) #인덱스 2 자리에 원소 4 추가하기
num_list.remove(10) #원소 10 삭제하기
print(num_list)

num_list.sort() #오름차순 정렬
print(num_list)
