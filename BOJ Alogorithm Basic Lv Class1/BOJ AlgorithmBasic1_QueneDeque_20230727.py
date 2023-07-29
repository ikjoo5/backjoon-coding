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

############################################################

###### 2023-07-28

### BOJ 11866번
from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int, input().split())
quene = deque([])
new_quene = []

for x in range(1,n+1):
    quene.appendleft(x)

while len(quene) > 0:
    for y in range(k):
        if y == k-1:
            new_quene.append(quene[-1])
            quene.pop()
        else:
            quene.appendleft(quene[-1])
            quene.pop()

print("<", ", ".join(map(str, new_quene)), ">", sep="")



### BOJ 1966번
    # 오답!!
        # b/c 중복숫자의 index를 해결 못함
import sys
from collections import deque

input = sys.stdin.readline

case_number = int(input())

for _ in range(case_number):
    waitlist = deque([])
    printed = deque([])
    print_number, m = map(int, input().split())
    array = map(int, input().split())
    
    count = 0

    for x in array:
        waitlist.append(x)
    
    mark_m = waitlist[m]
    
    while len(waitlist) > 0:
        if waitlist[0] != max(waitlist):
            waitlist.append(waitlist[0])
            waitlist.popleft()
        elif waitlist[0] == max(waitlist):
            printed.append(waitlist[0])
            waitlist.popleft()
            count +=1
    
    print(printed.index(mark_m)+1)
    print(count)


    ### 내 풀이접근에서 가장 모범답안
        # 문제의 어려운점은 중복 숫자들이 존재할때 내가 원하는 값을 서칭완료해도 index가 맞아야된다
        # 따라서 deque이나 리스트를 index용으로 추가한다
        # 최종적으로 우리는 두개의 리스트를 굴린다
        # [1,1,9,1,1,1] == [0,1,2,3,4,5] 이둘을 원하는 index순서의 숫자를 출력할때까지 같이 push pull 

import sys

# 테스트 케이스의 수
case = int(sys.stdin.readline())

for _ in range(case):
    # 문서의 개수 N,  몇 번째로 인쇄되었는지 궁금한 문서가 
    # 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M
    n, m = map(int, sys.stdin.readline().split())
    
    # N개 문서의 중요도
    priority = list(map(int, sys.stdin.readline().split()))
    
    # N개 문서의 기존 순서 저장
    index = [i for i in range(n)]

    # 몇 번째로 인쇄할지 카운트하는 변수
    count = 0
    
    while True:
        # 현재 문서가 중요도가 제일 높다면
        if priority[0] == max(priority):
            # 몇 번째로 출력 되는지 카운트
            count += 1
            # 궁금한 문서인지 확인
            if index[0] == m:
                print(count)
                break
            # 궁금한 문서가 아니라면 리스트에서 탈출
            else:
                del priority[0]
                del index[0]
        # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
        else:
            # 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치
            priority.append(priority[0])
            del priority[0]
            index.append(index[0])
            del index[0]

###############################################################

####### 2023-07-29

### BOJ 10866번

from collections import deque
import sys

n = int(sys.stdin.readline())
quene = deque([])
for x in range(n):
    order = sys.stdin.readline().split()

    if order[0] == 'front':
        if len(quene) != 0:
            print(quene[0])
        else:
            print('-1')

    elif order[0] == 'back':
        if len(quene) != 0:
            print(quene[-1])
        else:
            print('-1')

    elif order[0] == 'empty':
        if len(quene) == 0:
            print('1')
        else:
            print('0')

    elif order[0] == 'size':
        print(len(quene))

    elif order[0] == 'pop_front':
        if len(quene) == 0:
            print('-1')
        else:
            print(quene[0])
            quene.popleft()

    elif order[0] == 'pop_back':
        if len(quene) == 0:
            print('-1')
        else:
            print(quene[-1])
            quene.pop()

    elif order[0] == 'push_front':
        quene.appendleft(int(order[1]))
    
    elif order[0] == 'push_back':
        quene.append(int(order[1]))


### BOJ 1021번

from collections import deque
import sys

input = sys.stdin.readline()

n,m = map(int, input().split())
quene = deque([])
new_quene = []      # 추출한 수를 넣어두는 리스트

need_number = list(input().split())     # 뽑아야 하는 숫자들

for x in range(1,n+1):
    quene.append(x)

while len(new_quene) < m:



# 모범답안 
    # 내가 생각하고 구상한 코드와 비슷하지만 훨씬 간견하다
from collections import deque

n, m = map(int, input().split())    # 큐의 크기 n과 뽑아내려고 하는 수의 개수 m을 입력값으로 받기
position = list(map(int, input().split()))  # 뽑아내려는 수의 위치를 입력값으로 받기
dq = deque([i for i in range(1, n+1)])  # deque([1, 2, 3,...,n])

count = 0   # 2, 3번 수행하면 카운트 올리기
for i in position:  # 뽑아내려는 수의 위치 하나씩 반복문 돌리기
    while True:     # 뽑을 때까지 계속 돌리기
        if dq[0] == i:  # dq의 첫인덱스가 뽑아내려는 수의 위치와 같다면 1번 수행
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:  # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 작을때는 왼쪽으로 움직여야 최소
                while dq[0] != i:   # dq의 첫번째 인덱스가 i와 같아질때까지 반복
                    dq.append(dq.popleft())  
                    count += 1
            else:   # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 클때는 오른쪽으로 움직여야 최소
                while dq[0] != i:
                    dq.appendleft(dq.pop())  
                    count += 1
print(count)
