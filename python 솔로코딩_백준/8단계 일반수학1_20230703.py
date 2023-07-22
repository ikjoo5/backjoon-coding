### 2023-07-03 ###
### 백준 2720번
'''
import sys
input = sys.stdin.readline

test_number = int(input())

for _ in range(test_number):
    money = int(input())
    for x in [25,10,5,1]:
        print(money//x, end = ' ')
        money = money%x

### 백준2903번
import sys
input = sys.stdin.readline

n = int(input())
start = 2

for _ in range(n):
    start = start + (start-1)

print(start*start)
'''
    