# 2023년 4월 3일 코딩
'''
# 백준 9498번 if, elif 활용
a =int(input())   # 앞선 두 정수의 활용과 달리 single 정수 이기에 map 사용안함
if a>= 90:
    print('A')
elif a>=80 :
    print("B")   
elif a>=70:
    print("C")
elif a>=60:
    print("D")
else:
    print("F") 
    

# 백준 2753번 윤년 구하기
a = int(input())
if ((a%4 == 0) and (a%100 != 0) or (a%400 == 0)):
    print("1")
else:
    print("0")


# 백준 14681번 사분면 고르기
a = int(input('x값:'))
b = int(input("y값:"))
if a>0 and b>0:
    print("1")
elif a>0 and b<0:
    print("4")
elif a<0 and b<0:
    print("3")
elif a<0 and b>0:
    print("2")
else:
    print("error")


# 백준 2884번 알람 시계
    ### 내 정답
a, b = map(int, input().split())
c = b - 45
if c>=0:
    print(a,c)
elif (c<0) and (a!=0):
    print(a-1,c+60)
elif (c<0) and (a==0):
    print("23",c+60)
    ### 간결한 코딩
H, M = map(int, input().split())

if M < 45 :	# 분단위가 45분보다 작을 때 
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1	
        M += 60
        
print(H, M-45)	
'''    

# 백준 2525번 오븐 시계
    ### 내 답
a ,b= map(int, input().split())
c = int(input())
d = b + c
if d < 60:
    print(a,d)
elif d>=60:
    a1 = a + int(d/60)
    b1 = d%60
    if a1 <24:
        print(a1,b1)
    elif a1 >= 24:
        print(a1-24, b1)
    ### 간결한 답 (연산자 가능할때)
H, M = map(int, input().split())
timer = int(input()) 
H += timer // 60
M += timer % 60
if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
print(H,M)

