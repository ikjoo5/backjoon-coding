### 2023-07-10

### 9단계 약수, 배수와 소수 ###

### 백준 11653번

n = int(input())
i = 2
while n!=1:
    if n%i == 0:
        print(i)
        n = n/i
    else:
        i+=1

### 10단계 기하 : 직사각형과 삼각형 ###

### 백준 27323번
a = int(input())
b = int(input())

print(a*b)