'''
숫자 추측 게임 만들기

[문제 분석]
사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값(1~30)을 비교한다.
몇번 만에 맞혔는지 알려준다.

사용자에게 힌트를 준다.
사용자가 입력한 값이 랜덤 값보다 크면 '숫자는 작다' 라고 한다.
사용자가 입력한 값이 랜덤 값보다 작으면 '숫자는 크다' 라고 한다.

사용자가 값을 입력하여 힌트를 받을 때 마다 count 를 증가시킨다.
'''
# 1. random 함수를 불러온다.
# 2. 무한 반복한다.
#   1) 변수를 저장한다.(랜덤 값을 받는다.(1~30))
#   2) 무한 반복한다.
#       2-2-1. 만약 0을 입력하면
#           2-2-1-1. break
#       2-2-2. 변수를 입력받는다.
#       2-2-3. 만약에 입력받은 변수가 랜덤 값보다 크면
#           2-2-3-1 숫자는 작다 를 출력한다.
#           2-2-3-2 count +1
#       2-2-4. 만약에 입력받은 변수가 랜덤 값보다 작으면
#           2-2-4-1 숫자는 작다 를 출력한다.
#           2-2-4-2 count +1
#       2-2-5 아니면
#           2-2-5-1 count +1
#           2-2-5-2 count 출력
#           2-2-5-3 정답 을 출력
#   4) 계속 하시겠습니까 출력
#   5) 만약 3) 의 질문에서 n을 입력햇으면
#       2-5-1 종료 출력
#       2-5-2 break
import random
while True:
    count = 0
    randomnum = random.randint(1, 30)
    while True:
        num = int(input("1~30까지의 아무 숫자를 입력하시오 : "))
        if num == 0 :
            break
        if num > randomnum :
            print("숫자는 작다.")
            count += 1
        elif num < randomnum :
            print("숫자는 크다.")
            count += 1
        else:
            count += 1
            print("답은 {}으로".format(randomnum))
            print("{}번만에 맞추셨습니다.".format(count))
            print("종료")
            break
    pua = input("계속 하시겠습니까?(y/n) : ")
    if pua == "n" or pua == "N":
        print("종료")
        break
        