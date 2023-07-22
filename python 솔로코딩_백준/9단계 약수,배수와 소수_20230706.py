### 2023-07-06
# 9단계 약수, 배수와 소수
'''
### 백준 5086번
while True:
    a, b = map(int, input().split())
    if b > a and b%a ==0:
        print('factor')
    elif a > b and a%b==0:
        print('multiple')
    elif a == 0 and b == 0:
        break
    else:
        print('neither')
    

### 백준 2501번
a,b = map(int, input().split())
factor_list = []
for x in range(1,a+1):
    if a % x == 0:
        factor_list.append(x)

if len(factor_list) < b:
    print(0)
else:
    print(factor_list[b-1])
'''

### 백준 9506번

while True:
    n = int(input())
    t = []
    if n == -1:
        break
    
    for x in range(1,n):    # n+1으로 하면 자기자긴도 약수가 되므로 주의    
        if n % x ==0:       # 약수일때 리스트에 추가
            t.append(x)
        
    if sum(t) == n:     # 완전수일때
        print(f'{n} =', end = ' ') 
        for x in t[:-1]: 
            print(f'{x}', end = ' + ')  # 마지막에 +가 남아서 제외한 나머지
        print(t[-1])                    # 마지막 약수
    else:   # 완전수가 아닐경우
        print(f'{n} is NOT perfect.')