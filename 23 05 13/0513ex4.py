'''
2023 05 13
정우진
반복문을 탈출하는 break(if 조건문과 보통 함께 사용)
'''

i=1 #i 초기화

while True: #무한 반복
    print(i) #i출력
    if i >=3: #선택 조건(반복 종료 조건)
        break #반복문 강제 종료
    i+=1 #i 1 증가