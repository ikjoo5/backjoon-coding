### 2023-05-09
'''
# 백준 3003번

import sys
input= sys.stdin.readline

a = [1,1,2,2,2,8]
b = input().split()
c= []

for x in range(6):
    y = int(a[x]) - int(b[x])
    c.append(y)
    print(c[x], end = " ")


# 백준 2444번

### 내답 너무 어렵게 생각했다.
a = int(input())
b = 2*a-1
t = -1

for x in range(a):
    if t < b:
        t = t + 2 
        print("*"*t)
    elif t >= b:
        t = t - 2
        print("*"*t)
'''
### 모범답안

N = int(input())

for i in range(1,N):
    print(' '*(N-i)+'*'*(2*i-1))    # N 번째에 제일 max 별의 개수

for i in range(N,0,-1):             # range(시작,끝값,-1) -1은 역순으로 출력
    print(' '*(N-i)+'*'*(2*i-1))
