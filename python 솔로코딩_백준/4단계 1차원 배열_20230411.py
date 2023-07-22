'''
# 백준 10810번

import sys
input= sys.stdin.readline

n,m = map(int, input().split())
L = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())     #  공 넣은수 최신화

    for y in range(i-1, j):     # 리스트를 k값을 토대로 최신화
        L[y] = k

for x in range(n):          # 0부터 n번까지 리스트안의 변수를 꺼내 나열
    print(L[x], end=" ")

    

    # 모범답안
    
바구니개수N , 반복횟수M= map(int,input().split())

바구니=[0] * 바구니개수N  # 0으로 채운다.

for _ in range(반복횟수M):
    시작,끝,채울번호= map(int,input().split())

    for m in range(시작-1,끝):
        바구니[m]=채울번호


숫자리스트문자로= ' '.join(str(n) for n in 바구니)

print (숫자리스트문자로)

    

# 백준 10813번
    # 풀이 1
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
L = []
for x in range(1,n+1):
    L.append(x)

for _ in range(m):
    i, j= map(int, input().split())
    L[i-1], L[j-1] = L[j-1], L[i-1]       # 파이썬스러운 풀이
    
for z in range(n):
    print(L[z], end=" ")
    
   
    #풀이 2
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
L = []
temp = 0                # 변수를 한개 더 생성해 삼각 교환으로 풀이
for x in range(1,n+1):
    L.append(x)

for _ in range(m):
    i, j= map(int, input().split())
    temp = L[i-1]
    L[i-1] = L[j-1]
    L[j-1] = temp

for z in range(n):
    print(L[z], end=" ")
'''


#백준 5597번

import sys
input = sys.stdin.readline
q=[]
for x in range(1,31):
    q.append(x)

for _ in range(28):
    data= int(input())
    q.remove(data)

print(min(q))
print(max(q))

