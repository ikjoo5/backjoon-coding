### 2023-07-09

### 9단계 약수, 배수와 소수 ###

### 백준 1978번
'''
    # solution1 : for, if 활용 풀이

n = int(input())

numbers = map(int, input().split())

sosu = 0
for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu += 1  # error가 없으면 소수.
print(sosu)


    # solution2 : break 활용

n = int(input())
numbers = map(int, input().split())
count = 0

for num in numbers:
    for i in range(2, num+1): 
        if num % i == 0:
            if i == num:       # 자기 자신제외
                count += 1
            break               # 자기 자신을 제외한 나머지 숫자에 나머지가 0인 순간 소수가 아니므로 break
              
print(count)

'''

### 백준 2581번

m = int(input())
n = int(input())
sosu_list = []
for num in range(m, n+1):    # n+1로 자기자신까지 검사

    for x in range(2,num+1):
        if num % x == 0:
            if x == num:
                sosu_list.append(x)
            else:
                break       # 나머지가 0인 순간 소수가 아니므로 break

if len(sosu_list) == 0:
    print(-1)
else:
    print(sum(sosu_list), min(sosu_list), sep = '\n')    # 출력값 맞춰주기
