### 2023-07-22 ###

### 백준 알고리즘 기초강의

###### 알고리즘 시작

### 시간 복잡도
    # 이 방법으로 작성한 코드가 대략 얼마나 걸리는지 유추가능하다

    # 시간 복잡도는 소스를 보고 계산할 수 도 있고, 소스를 작성하기 전에 먼저 계산가능
    # 따라서 문제를 풀기전에 먼저 생각한 방법의 시간 복잡도를 계산해보고 이게 시간 안에 수행될 거 같은 경우에만 구현하는것이 좋다

    # 보통 1억개의 범위를 처리하는데 1초가 걸리기에 이를 기준으로 한다.
    # 가능한 코드가 이 1초범위 안에 들어오게 하는게 좋은 코드이다


###### 스택
    # 스택은 기본적으로 LIFO : last in first out

    # 스택의 특성상 맨위 or 맨 오른쪽의 항목만 추가하거나 제거가능하다
    # 만약 중간의 것을 사용해야되는 상황이라면 스택을 사용하면 안된다!! 즉 맨위를 사용해야되는 경우에만 사용
        # ex. 데이터가 중간에 바뀌면 안되는것들 경우에 스택이나 튜플 같은것을 사용

    # 파이썬의 경우 리스트가 스택과 같은역할을 한다
 
    # stack의 top = [size-1] 


### 스택 문제풀이 ###
'''
# 백준 10828번
    # 유의점
c = input().split()     # 출력이 리스트형식으로 된다 c = ['sadf', 'sdf', 'asdf']

    # 모범답안
import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
'''

# 백준 10773번
import sys
input = sys.stdin.readline

n = int(input())
num_list = []
for _ in range(n):
    order = int(input())

    if order == 0:
        num_list.pop()
    else:
        num_list.append(order)
print(sum(num_list))


### 2023-07-24
### 백준 1874번

n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur += 1
    # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.

    if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
        stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
        answer.append("-")
    else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO")         # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데
        flag = 1            # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
        break               

if flag == 0:
    for i in answer:
        print(i)
