'''
작성일 : 2023년 4월 21일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 정수를 입력 받아 정육면체의 부피를 구하시오.
'''
# 1. 변수를 입력받는다.
num = int(input("정육면체의 가로, 세로, 높이 중 하나를 입력하시오. : "))

# 2. 정육면체의 부피를 계산한 값을 출력한다.
print("가로 세로 높이가 {}인 정육면체의 부피는 {}입니다.".format(num, num**3))