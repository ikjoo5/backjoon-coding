'''
# 15552번 sys.stdin.readline() 활용
    ## input 함수활용 version
T = int(input())
for _ in range (1,T+1):
    a,b= map(int, input().split())
    print(a+b)

    ## sys.stdin.readline() 활용 version
import sys

t= int(sys.stdin.readline())    # input을 sys.stdin.readline으로 변경으로생각

for _ in range(t):
    a,b= map(int,sys.stdin.readline().split())
    print(a+b)
        '''

# 백준 11021번 f string 활용 문제

import sys
t= int(sys.stdin.readline())

for i in range(t):
    a,b= map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a+b}')
    # f ' ' 형식이다. 이안에 일반 form은 고정값 {}괄호안값은 변수값 출력가능

