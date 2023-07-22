### 2023-07-14

### 10단계 기하

#백준 14215번
'''
a,b,c = map(int, input().split())
t = [a,b,c]
t.sort()

if (t[0] + t[1]) > t[2]:
    print(a+b+c)
elif (t[0] + t[1]) <= t[2]:
    print(2*(t[0] + t[1]) - 1)
'''



### 11단계 시간 복잡도

# 백준 24262번

print('1', '0', sep = '\n')


# 백준 24263번

# def MenOfPassion(A, n):
# 	answer = 0
#     for i in range(n):
#     	answer = answer + A[i]
#     return answer

print(input())
print(1)