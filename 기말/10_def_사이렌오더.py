'''
학과 : 컴퓨터공학부
학번 : 202395031    
이름 : 천승용

사이렌 오더를 통해 음료를 미리 예약하느 ㄴ프로그램을 ㅁ나드시오.
메뉴는 
1. 아메리카노 2500원
2. 카페라때 3000원
3. 바닐라 라떼 3000원입니다.
메뉴 번호를 선택하면 해당 메뉴와 가격을 출력해 주는 부분을 함수로 작성하시오.

선택한 메뉴는 인수로 전달되어 가격이 결과 값으로 반환되는 함수로 작성하시오.

사용자가 음료를 선택하면 음료의 가격을 알려주는 프로그램
'''
def siren(num):
    if num == 1 :
        return '아메리카노는 2500원입니다.'
    elif num == 2 :
        return '카페라때는 3000원입니다.'
    elif num == 3 :
        return '바닐라 라떼는 3000원입니다.'
    else:
        return '\n없는 메뉴 입니다.\n'
while True:
    meue = int(input("1. 아메리카노\n2. 카페라때\n3. 바닐라 라때\n번호를 입력해주세요(종료:0) : "))
    if meue == 0:
        break
    print(siren(meue))

