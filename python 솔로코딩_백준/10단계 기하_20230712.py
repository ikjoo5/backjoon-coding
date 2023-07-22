### 2023-07-12 ###

### 10단계 기하
'''
# 백준 15894번
n = int(input())
print(n*4)
'''
# 백준 9063번

n = int(input())
x_list = []
y_list = []
for _ in range(n):
    x,y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

z = max(x_list) - min(x_list)
x = max(y_list) - min(y_list)

if n == 0:
    print(0)
else:
    print(z*x)