'''
# 백준 11022번

import sys
t = int(sys.stdin.readline())

for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')
    

# 백준 2438번

n= int(input())

for i in range(1, n+1):
    print('*'*i)


# 백준 2439번
    # Method 1
n = int(input())

for i in range(1,n+1):
    st= "*"*i
    print(st.rjust(n))  # rjust값은 자리수 & 오른쪽 정렬 5면 5자리수로 출력

    # Method 2

n = int(input())
for i in range(n):
    print(" "*(n-1-i)+'*'*(i+1))

# 백준 10952번 while 활용 문제!!
    # while을 몰랐을때 나의 답
import sys
input = sys.stdin.readline

for _ in range(10):
    a,b = map(int, input().split())
    if a != 0 and b!= 0:
        print(a+b)
    else:
        print("")
        
    # using while
import sys
input = sys.stdin.readline

while True:
    a,b = map(int, input().split())
    if a == 0 and b== 0:
        break
    print(a+b)
    '''
# 백준 10951번
    # 내 답변 = 런타임 에러
import sys
input = sys.stdin.readline

while True:
    a,b = map(int, input().split())
    if a <= 0 and b >= 10:
        break
    print(a+b)

    # 모범답안
import sys
input = sys.stdin.readline

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break

    # 답안 2
try:
    while True:
        A, B = map(int, input().split())
        print(A+B)
except:
    print("error")     # 위와 비슷하나 while이 try안에 있어 무한반복 x
    
    
        
