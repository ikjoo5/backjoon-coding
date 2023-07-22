### 2023-07-20 

### 12단계 브루트포스

# 백준 2232번

    ### 내답 
t = []
n = int(input())
m = n-1         # 큰 수 부터 찾게 된다
while m>1: 
    m2 = list(map(int, str(m)))
    result = sum(m2) + m
    if result ==n:
        t.append(m)
        m = m-1
    else:
        m = m-1
if len(t) == 0:
    print("0")
else:
    print(min(t))

'''
    ### 모범답안
        # 제일 작은수부터 찾기때문에 코드수가 적고 시간도 적게 든다
n = int(input())
result = 0
for i in range(1, n+1):         # 제일 작은수를 출력하고싶기에 1부터 찾는다
    nums = list(map(int, str(i)))
    result = sum(nums) + i
    if result == n:
        print(i)
        break
    if i == n:
        print(0)​
'''   

