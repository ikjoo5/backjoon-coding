### 2023/04/28
'''
### 백준 11654번

# import sys
# input = sys.stdin.readline    -> 이 문제의 경우 문자열을 포함하기에
#                                  sys.stdin.realine 사용하면 안됨, only 정수

a = input()
print(ord(a))       # ord() : 문자의 아스키 코드값을 리턴하는 함수
                    # chr() : 아스키코드값을 입력하면 코드의 문자 리턴


### 백준 11720번

# 내가 생각한 이상적인 답변
n = int(input())
x = input()         # 문자열의 숫자를 입력받고 그 자리수를 수로 치환해덧셈
print(sum(map(int,x)))  # map(int, ) 활용

# for문 활용

n = int(input())
x = input()
t = 0
for y in range(n):
    t += int(x[y])      int화 잊지말기
print(t)
'''

