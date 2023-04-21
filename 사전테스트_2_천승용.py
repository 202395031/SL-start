'''
작성일 : 2023년 4월 21일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 자판기 잔동 계산 프로그램을 작성하시오.
'''
# 1. 변수를 입력받는다.
coin = int(input("얼마를 넣을지 입력하시오. : "))

# 2. 받은 돈에 350을 뺀다
coin1 = coin - 350

# 3. 500원 짜리가 얼마나 나와야하는지 계산하기 위해 잔돈에 500원을 나눈 값에 몫과 나머지를 변수에 저장한다.
coin2 = coin1 // 500
coin2_1 = coin1 % 500

# 4. 3에서 나눈 값의 나머지를 100으로 나눳을때 몫과 나머지를 변수에 저장한다.
coin3 = coin2_1 // 100
coin3_1 = coin2_1 % 100

# 5. 4에서 나눈 값의 나머지를 50으로 나눳을때 몫과 나머지를 변수에 저장한다.
coin4 = coin3_1 // 50
coin4_1 = coin3_1 % 50

# 6. 잔돈이 얼마나 나오는지 출력한다.
print("500원짜리 {}개 100원짜리 {}개 50원짜리 {}개로 총 {}원 입니다.".format(coin2, coin3, coin4, coin1))