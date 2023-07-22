### 2023-07-11

### 10단계 기하

# 백준 1085번
'''
x,y,w,h = map(int, input().split())
t = [x,y]
t.append(w-x)
t.append(h-y)
print(min(t))
'''

# 백준 3009번
x = []
y = []

for _ in range(3):
    a,b= map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(3):
    if x.count(x[i]) == 1:
        x4 = x[i]
    if y.count(y[i]) == 1:
        y4 = y[i]
print(x4, y4)