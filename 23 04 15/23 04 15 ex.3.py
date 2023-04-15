'''
2023.04.15
정우진
숫자형 자료활용-산술연산 연습
문자형 자료활용-문자열 더하기,곱하기
'''

su1=10 #su1변수에 정수 10 저장
su2=5 #su2변수에 정수 5 저장
str1='python' #str1에 문자열 저장
str2="programming" #str2에 문자열 저장

print('{}+{}={}'.format(su1,su2,su1+su2)) #덧셈결과
print('{}-{}={}'.format(su1,su2,su1-su2)) #뺄셈결과
print('{}*{}={}'.format(su1,su2,su1*su2)) #곱셈결과
print('{}/{}={}'.format(su1,su2,su1/su2)) #나눗셈결과
print('{}//{}={}'.format(su1,su2,su1//su2)) #su1을 su2로 나눈 몫
print('{}%{}={}'.format(su1,su2,su1%su2)) #su1을 su2로 나눈 나머지
print('{}**{}={}'.format(su1,su2,su1**su2)) #su1을 su2만큼 곱한 제곱근

print() #한줄 띄우기
print('문자열 연결하기(+):',str1+str2) #문자열 연결
print('문자열 곱하기(*):',str1*3) #문자열 반복(3번)
