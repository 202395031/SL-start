'''
작성일 : 2023년 4월 21일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 아이디와 패스워드를 입력 받아 로그인 인증 결과를출력하는 프로그램을 작성하시오.
'''
# 1. 아이디와 패스워드를 변수에 저장한다.
id = "admin"
pas = "pw1234"

# 2. 변수를 입력받는다.
id_p = input("아이디를 입력하세요. : ") 
pas_p = input("패스워드를 입력하세요. : ")

# 3. 만약 id와 id_p가 다르고 pas와 pas_p다르면 아이디와 패스워드가 틀렸습니다. 출력
if id != id_p and pas != pas_p :
    print("아이디와 패스워드가 틀렸습니다.")

# 4. 아니면 id만 다르다면 아이디가 틀렸습니다.를 패스워드만 틀렸으면 패스워드가 틀렸습니다. 출력
else :
    if id != id_p :
        print("아이디가 틀렸습니다.")
    elif pas != pas_p :
        print("패스워드가 틀렸습니다.")
# 5. 아니면 로그인 성공 출력
    else :
        print("로그인 성공")