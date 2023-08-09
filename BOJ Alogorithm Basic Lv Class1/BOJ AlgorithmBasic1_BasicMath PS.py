###### 2023-08-07

###### 수학 ######

    ### 1 : 나머지연산(Modular Arithmetic)

        #  기본formatdms a%b : a를 b로 나눈 나머지
        # 그외
            # (a+b) % m = ((a%m) + (b%m)) % m
            # (a*b) % m = ((a%m) * (b%m)) % m
            # 뺄셈의 경우 음수가 나올 가능성이 있기에 나누는 수를 한번 더해서 양수로 만들어준다
                # (a-b) % m = ((a%m) - (b%m) + m) % m


    ### 2: 최대공약수 (GCD: Greatest Common Divisor)    /   최소공배수 (LCM: Least Common Multiple)

        # G = GCD(A,B) 일때
        # A*B = GCD * LCM
        # LCM = (A*B) / G
############ 2023-08-09 continue ################
'''
        # 유클리드 호제법으로 최대공약수 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# or

def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)    # b가 더 클경우 a와b의 위치를 swap

        # 파이썬 math lib 사용
import math
a, b = 10, 15
math.gcd(a, b)  # 5


    ### 연습 BOJ 1934번 최소공배수
import math
t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    print(math.lcm(a,b))
    

    ### BOJ 13241번 최소공배수(유클리드 호제법으로 풀이)

def gcd(a,b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


x,y = map(int, input().split())
g = gcd(x,y)
print(int(x*y / g))
'''

    ### BOJ 2609번 최대공약수와 최소공배수
a,b = map(int, input().split())

def gcd(x,y):
    if x % y == 0:
        return y
    elif y == 0:
        return x
    else:
        return gcd(y, x % y)
print(gcd(a,b), int(a*b/gcd(a,b)), sep = '\n')





