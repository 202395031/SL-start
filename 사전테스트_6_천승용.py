'''
작성일 : 2023년 4월 21일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 컴퓨터, 영어 과목의 점수를 입력 받아 두 과목 중 한 과목의 성적이 95점 이상이거나,
        두 과목의 합이 170점 이상이면 "합격입니다"를 출력하고,
        아니면 "불합격입니다."를 출력하는 프로그램을 작성하시오.
'''
# 1. 변수를 입력받는다.
score1 = int(input("컴퓨터 과목의 점수를 입력하시오. : "))
score2 = int(input("영어 과목의 점수를 입력하시오. : "))

# 2. 만약에 두 과목 중 한 과목의 성적이 95점 이상이거나, 두 과목의 합이 170점 이상이면 "합격입니다"를 출력
if score1 >= 95 or score2 >= 95 or score1 + score2 == 170 :
    print("합격입니다")
# 3. 아니면 "불합격입니다."를 출력
else :
    print("불합격입니다.")

