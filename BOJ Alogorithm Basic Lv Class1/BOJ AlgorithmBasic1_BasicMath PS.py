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
################################## 2023-08-10 #########################################

    ### 3: 소수 (Prime Number)

        ### 주어진 수 x 가 소수인지 아닌지 판별하는법

            # 1-1
                # 그냥 2부터 x-1까지 하나씩 for문을 통해 나누어보면된다
            
            # 1-2
                # 다만 좀더 효율적인 방법으로는 2 부터 x/2를 실행하면 된다(시간 비슷)
'''
            # 1-3 (제일빠른방법이다)
                # 2부터 루트x까지 탐색해도 소수판별가능
                # i ==2 to i*i <= x 
import math
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4)) # 4는 소수가 아님
print(is_prime_number(7)) # 7은 소수임


        ### N이하의 수중에 소수를 구하는 방법
            ####### 에라토스테네스의 체(Sieve of Eratosthenes) #########
                # 소수를 구할 때 제일 좋은 알고리즘

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)   # 루트 of n b/c 루트n으로 탐색하는게 시간이 더 빠름
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]     # 아래 for문을 요약 

    # for i in range(2,n):
    #     if sieve[i] == True
    #     return i


            ### Practice BOJ 1929번 소수 구하기
# 내 풀이(오답) 접근을 달리해보자
m , n = map(int, input().split())

sieve = [True] * n

for i in range(m,n+1):
    if sieve[i] == True:
        for j in range(i+i, n, i):
            sieve[j] = False

for i in range(m,n+1):
    if sieve[i] == True:
        print(i)

# 모범답안
    # 기존에 에라토스원리는 1부터 n까지
    # 따라서 n까지 구하고 다시for문으로 m,n으로 설정
M, N = map(int, input().split())

N += 1
sieve = [True] * N
for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False
for i in range(M, N):
    if i > 1:
        if sieve[i]:
            print(i)
'''
###############################  2023-08-12, 08-13 ####################################

        ########## 골드바흐의 추측(Goldbach's Conjecture) #####################
    # 정의 : 2보다 큰 모든 짝수는 두 소수의 합으로 표현이 가능하다
        # 번외 : 2에 3을더한 5보다 큰 모든 홀수는 세 소수의 합으로 표현이 가능하다 


### BOJ 6588번 골드바흐의 추측

t= int(input()) # number of test case

import math

def d(N): # 소수 판별 함수
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

for _ in range(t):
    n = int(input())

    a = n // 2
    b = a
    for _ in range(n//2):
        if d(a) and d(b):   # a,b가 모두 소수일때
            print(a, b)
            break
        else:
            a -= 1
            b += 1


        ############## 팩토리얼(Factorial) ######################

### BOJ 10872번 팩토리얼
import math

a = int(input())
print(math.factorial(a))



