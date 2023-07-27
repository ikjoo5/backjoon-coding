### 2023-07-27

# 알고리즘 기초 강의 1/2

###### 큐와 덱 

### 1. Quene 란?
    # 한쪽끝에서만 자료를 push하고 다른 반대쪽에서 pop하는 자료구조
    # 스택과는 다르다 : stack = first in last out
    # 큐는           : quene = first in first out(FIFO)
    
### BFS에서 정말 중요하게 다룬다 ###


# 큐의 기본 명령어들
    # front : 큐의 가장 앞에 있는 자료를 봄
    # back : 큐의 가장 맨뒤
    # empty : check whether quene is empty or not
    # size : count the number of the quene

# 파이썬의 경우 리스트로 이용해 큐를 구현하면 시간이 오래걸림
# 따라서 collection의 deque을 사용하거나 quene를 따로 구현


### 2. 덱 Deque
    # double ended quene의 약자이다
    # 정의 : 양끝에서만 자료를 넣고 양끝에서 자료를 빼는 구조
    # 사실상 stack과 quene의 기능을 포함하기에 둘다 구현을 시킬 수 있게됨

# 덱의 기본 명령어들
    # from collections import deque를 기입
    # 기본형태 : quene = deque([])
    # append나 pop을 왼쪽에서 가능 
        # .appendleft(), popleft()

    ### 역시 BFS에서 중요하게 다룬다 ###



### 큐와 덱 기본 연습

    ### BOJ 18258번
'''
import sys
from collections import deque

input = sys.stdin.readline      # 사용 안할경우 시간초과
n = int(input())
quene = deque([])

for _ in range(n):
    x = input().split()

    if x[0] == 'front':
        if len(quene) == 0:
            print('-1')
        else:
            print(quene[0])
    elif x[0] == 'back':
        if len(quene) == 0:
            print('-1')
        else:
            print(quene[-1])
    elif x[0] == 'size':
        print(len(quene))
    elif x[0] == 'pop':
        if len(quene) == 0:
            print('-1')
        else:
            print(quene[0])
            quene.popleft()
    elif x[0] == 'empty':
        if len(quene) == 0:
            print('1')
        else:
            print('0')
    else:                       # 무조건 push만 남는다
        x1 = int(x[-1]) 
        quene.append(x1)
'''

    ### BOJ 2164번
from collections import deque

n = int(input())
quene = deque([])

for x in range(1, n+1):
    quene.appendleft(x)

while len(quene) > 1:
    quene.pop()
    quene.appendleft(quene[-1])
    quene.pop()

print(quene[0])