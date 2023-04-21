'''
작성일 : 2023년 4월 21일
학과 : 컴퓨터공학부
학번 : 202395031
이름 : 천승용
설명 : 태어난 년도를 입력 받아 띠를 출력하는 프로그램을 작성하시오.
'''
# 1. 변수를 입력받는다.
year = int(input("년도를 입력하세요. : "))

# 2. 만약 year을 12로 나눴을때 나머지가 1이라면 쥐띠입니다. 출력
if year % 12 == 1:
    print("{}년은 쥐띠입니다.".format(year))
    
# 3. 만약 year을 12로 나눴을때 나머지가 2이라면 소띠입니다. 출력
elif year % 12 == 2:
    print("{}년은 소띠입니다.".format(year))
    
# 4. 만약 year을 12로 나눴을때 나머지가 3이라면 범띠입니다. 출력
elif year % 12 == 3:
    print("{}년은 범띠입니다.".format(year))
    
# 5. 만약 year을 12로 나눴을때 나머지가 4이라면 토끼띠입니다. 출력
elif year % 12 == 4:
    print("{}년은 토끼띠입니다.".format(year))
    
# 6. 만약 year을 12로 나눴을때 나머지가 5이라면 용띠입니다. 출력
elif year % 12 == 5:
    print("{}년은 용띠입니다.".format(year))
    
# 7. 만약 year을 12로 나눴을때 나머지가 6이라면 뱀띠입니다. 출력
elif year % 12 == 6:
    print("{}년은 뱀띠입니다.".format(year))
    
# 8. 만약 year을 12로 나눴을때 나머지가 7이라면 말띠입니다. 출력
elif year % 12 == 7:
    print("{}년은 말띠입니다.".format(year))
    
# 9. 만약 year을 12로 나눴을때 나머지가 8이라면 양띠입니다. 출력
elif year % 12 == 8:
    print("{}년은 양띠입니다.".format(year))
    
# 10. 만약 year을 12로 나눴을때 나머지가 9이라면 원숭이띠입니다. 출력
elif year % 12 == 9:
    print("{}년은 원숭이띠입니다.".format(year))
    
# 11. 만약 year을 12로 나눴을때 나머지가 10이라면 닭띠입니다. 출력
elif year % 12 == 10:
    print("{}년은 닭띠입니다.".format(year))
    
# 12. 만약 year을 12로 나눴을때 나머지가 11이라면 개띠입니다. 출력
elif year % 12 == 11:
    print("{}년은 개띠입니다.".format(year))
    
# 13. 아니면 돼지띠입니다. 출력
else :
    print("{}년은 돼지띠입니다.".format(year))