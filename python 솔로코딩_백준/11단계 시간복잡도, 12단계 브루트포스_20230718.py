### 2023-07-18

# 11단계 시간 복잡도
'''
# 백준 24266번
n = int(input())
print(n**3)
print(3)

# 백준 24267번
n = int(input())

print(int((n*(n-1)*(n-2))/6))
print(3)
'''
######### 시간복잡도는 추후에 복습이 필요하다... 개념이 어려운건 아닌데 문제가 헷갈리고 어렵다 수학도 매우 부족해보임!!   ########################


# 12단계 브루트 포스

# 백준 2789

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
nlst = []
for i in range(N):  
    for j in range(i+1, N):
        for k in range(j+1, N):                     # 요런식으로 모든수를 점검하게 설정
            three =  lst[i] + lst[j] + lst[k]
            if three > M:                           # max를 초과한경우는 그냥 pass
                continue
            else:
                nlst.append(three)                  # 리스트에 세수의합을 추가
print(max(nlst))