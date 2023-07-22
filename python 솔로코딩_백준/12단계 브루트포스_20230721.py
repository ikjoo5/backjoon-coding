### 2023-07-21

# 12단계 브루트 포스

### 백준 19532번
'''
# 내답  = 오류!! 
    # zerodivisionerror로 풀 수가 없다. 왜냐면 0으로 나누는것을 불가
import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int, input().split())

y = (d*c - a*f) / (d*b - a*e)
x = (c-b*y) / a
x , y = int(x), int(y)
print(x, y)

# 모범답안
    # 애초에 파이썬은(컴퓨터는) xy소거법으로 풀 이유가 없다.
import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())

for i in range(-999,1000):
    for j in range(-999,1000):
        if a*i + b*j == c and d*i + e*j == f:
            print(i,j)

'''
### 백준 1018번 ############################
    # 이해못함 무조건 디시풀어야됨!!

N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))