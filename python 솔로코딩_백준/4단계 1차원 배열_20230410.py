'''
# 백준 2562번

    # 내 첫 답(오답) b/c 이런식이면 문제의 입력값과 틀림
import sys
input = sys.stdin.readline

n = list(map(int, input().split()))

print(max(n))
print(n.index(max(n))+1)

    # 모범답안
import sys
input= sys.stdin.readline

n=[]
for _ in range(9):
    i = int(input())        # for문으로 9번 반복 및 추가로 리스트 완성
                            # 그리고 문제입력과 값이 다음줄에 추가가능
                            # if 입력값이 12 31 41...이었다면 위와같이하면됨
    n.append(i)             # append로 함수추가

print(max(n))
print(n.index(max(n))+1)    # index함수로 위치 찾기 but index starts from 0
                            # thus add +1


'''
# 백준 10810번

import sys
input= sys.stdin.readline

n,m = map(int, input().split())
L = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())

    for m in range(i-1, j):
        L[m] = k

print(L)
    
'''
    # 모범답안
    
바구니개수N , 반복횟수M= map(int,input().split())

바구니=[0] * 바구니개수N  # 0으로 채운다.

for _ in range(반복횟수M):
    시작,끝,채울번호= map(int,input().split())

    for m in range(시작-1,끝):
        바구니[m]=채울번호


숫자리스트문자로= ' '.join(str(n) for n in 바구니)

print (숫자리스트문자로)
    
    '''
