# 2023년 4월 4일
'''
# 백준 10950번 for 활용문제
T = int(input())  
for _ in range(T): # t번만큼 아래의 코딩을  반복
    a,b= map(int, input().split())
    print(a+b)


# 8393번 합
n = int(input())
total = 0  # 변수에 0을 지정
for i in range(1,n+1):  
    total += i # total = total + i와 같은 의미
print(total) # 여기서 들여쓰기 주의! / total과 같은라인이면 모든 total
             # 계산과정이 들어간다. Thus print를 들여쓰기없이 입력


# 25304번 영수증
x = int(input())
n = int(input())
total = 0
for _ in range(1, n+1):
    a,b = map(int, input().split())
    total += (a*b)
    
if x == total:
    print("Yes")
else:
    print("No")
    '''

# 25314 
for _ in range(int(input())//4):
    print("long", end=" ")
    
print("int")

    
