'''
# 2023년 4월 3일 코딩

# 백준 2480번 주사위 세개
a, b, c = map(int, input().split())
if a ==b==c:
    d = 10000 + (a*1000)
    print(d)
elif (a != b) and (b!=c) and(a!=c):
    d1= max(a,b,c) *100
    print(d1)
elif a==b:
    print(a*100 +1000)
elif a==c:
    print(a*100 +1000)
elif b==c:
    print(b*100 +1000)
'''

# 백준 2739번 구구단
#  for문을 작성하게 되면 in 뒤에 위치한 반복 가능한 iterable 자료형의 요소를
#  하나씩 꺼내서 변수에 선언하게 된다. 그리고 range의 끝값은 함수값에 포함이 안된다.
N = int(input())
for i in range(1,10):
 print(N,'*',i,'=',N*i)

