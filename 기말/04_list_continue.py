'''
학과 : 컴퓨터공학부
학번 : 202395031    
이름 : 천승용

continue
'''
# 리스트의 값 10개 중에서 10보다 큰 수를 출력하시오.
numbers = [1,2,3,4,5,6,7,8,9,10]
print("리스트 값 중 10보다 큰수 - 반복문 사용")

for i in numbers:
    if i >= 10:
        print(i, end=' ')
print()

print("리스트 값 중 10보다 큰 수 - continue 사용")

for i in numbers:
    if i < 10 :
        continue
    print(i, end=',' )
print()

# 1~30 사이의 수 중에서 7의 배수만 출력하시오. - continue 사용
# 7로 나누어 나머지가 0인 수
print("1~30 사이 중 7의 배수 출력")
for i in range(1,31):
    if i % 7 != 0:
        continue    
    print(i, end=' ')
print()
    