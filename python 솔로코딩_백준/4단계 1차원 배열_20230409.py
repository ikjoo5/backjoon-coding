### 4단계 배열
'''
# 백준 10807번

import sys
input = sys.stdin.readline
n = int(input())
n_list= list(map(int, input().split()))
v = int(input())

print(n_list.count(v))   # list안의 변수값들중에서 몇개인지 count해줌
    ### 코드에 에러 있음 -> n개수 입력값과 상관없이 리스트 개수를 늘려도 error x
    ### 추후에 배우는 내용으로 보완해보자

    
# 백준 10871번

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    if A[i] < x:                # A[]는 A리스트안에서 몇번째를 지정 
        print(A[i], end=(" "))
'''
'''
# 백준 10818번
    # 내답
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

print(min(n_list), max(n_list))
'''
    # 순차검색으로 해결하는 방안
input()
l = list(map(int, input().split()))
min, max = 1000000, -1000000

for item in l:
  if item > max:
    max = item
  if item < min:
    min = item

print(min, max)


