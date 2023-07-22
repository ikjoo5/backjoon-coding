### 2023-07-13

# 10단계 기하
'''
# 백준 10101번
a = int(input())
b = int(input())           
c = int(input())
total = a+b+c


if total ==  180:
    if a == 60 and b==60 and c==60:
        print("Equilateral")
    elif a != b and b != c and c!=a:
        print("Scalene")
    elif a == b or b==c or a==c:
        print("Isosceles")
else:
    print("Error")
'''

# 백준 5073번

while True:
    a,b,c = map(int, input().split())
    t = [a,b,c]
    t.sort()

    if a == b==c==0:
        break
    
    if t[2] >= (t[0] +t[1]):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a != b and b!=c and a!=c:
        print("Scalene")
    elif a==b or b==c or a==c:
        print("Isosceles")
    
    
