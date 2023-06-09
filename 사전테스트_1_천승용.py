'''
작성일 : 2023년 4월 21일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 놀이공원 입장료 계산 프로그램을 작성하시오.
        10인 이상이면 20% 할인이 적용됩니다.
'''
# 1. 변수를 입력 받는다.
old1 = int(input("어린이(13세 미만)의 인원은 몇명입니까? : "))
old2 = int(input("보통(13세 ~ 64세)의 인원은 몇명입니까? : "))
old3 = int(input("경로우대(65세 이상)의 인원은 몇명입니까? : "))

# 2. 총 얼마인지 변수에 저장한다.
total = (old1 * 5000) + (old2 * 10000) + (old3 * 7000)

# 3. 만약 총 인원수가 10명이상이라면 20%할인된 가격을 출력한다.
if old1 + old2 + old3 >= 10:
    print("어린이 {} 명, 어른 {}명, 노인 {}명으로 총 {} 원 입니다.".format(old1, old2, old3, total*0.8))
    
# 4. 아니면 총 가격을 출력한다.
else:
    print("어린이 {} 명, 어른 {}명, 노인 {}명으로 총 {} 원 입니다.".format(old1, old2, old3, total))
