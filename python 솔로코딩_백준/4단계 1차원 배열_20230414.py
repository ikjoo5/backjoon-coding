
# 20230413 코딩 4단계 1차원 배열 문제풀이
'''
# 백준 3052번

import sys
input = sys.stdin.readline
L = []
for i in range(10):
    a = int(input())
    b = a % 42
    L.append(b)

L2 = set(L)                # set  함수를 통해 중복을 제거하며 나열하고 자료형으로 변환
L3 = list(L2)              # 자료형을 다시 리스트형으로 복귀
print(len(L3))             # len 함수는 길이를 구해준다

# 백준 10811번

import sys
imput = sys.stdin.readline

n,m = map(int, input().split())
L = []
for x in range(1,n+1):
    L.append(x)

for y in range(m):
    i, j = map(int, input().split())
    temp = L[i-1:j]                  # L.sort(reverse = True)는 오름차순후 배열뒤집기
    temp.reverse()
    L[i-1 : j] = temp
    
for z in range(n):
    print(L[z], end = " ")
'''

# 백준 1546번
import sys
input = sys.stdin.readline

n = int(input())
for x in range(n):
    m = int(input())