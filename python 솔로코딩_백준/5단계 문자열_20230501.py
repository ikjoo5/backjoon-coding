# 2023/05/01

# 백준 2675번

    ### First draft

t = int(input())
A = 0                # 빈 값을 여기가 아니라 for문 안에

for in range(t):
    r(횟수), s(문자열) = map(input().split())    # 굳이 map이 아니라 나중에 int처리
    for i in s:
        A += (s[i] * r)     # r int화, []불필요! i가 숫자가아니라 자동으로 문자리턴

print(A)   # print위치가 여기면 마지막 input 값만 출력된다

    ### 수정

t = int(input())

for x in range(t):
    r,s = input().split()
    a = ""
    for i in s:
        a += (i * int(r))
    print(a)


# 백준 1152번



