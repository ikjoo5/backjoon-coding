### 2023-07-05
# 8단계 일반수학1

# 백준 2869번
'''
    # solution1 : 가능하나 문제에서 제시한 시간을 초과하므로 다른식으로 대체해야됨 solve without while loop
a,b,v = map(int, input().split())
total = 0
day = 0
while v > total:
    total = total + a
    day += 1
    if total >= v:
        print(day)
        break
    else:
        total -= b

print(day)
'''

    # solution 2
a,b,v = map(int, input().split())

if (v-b) % (a-b) == 0:              # a-b = 하루가는 거리 , v-b = 총 높이에서 밤에 미끄러지는 거리 제외
    print((v-b) // (a-b))           
else:
    print((v-b) // (a-b) +1)        # 거리가 미끄러진만큼 부족하다 = 하루만 더 올라가면 된다

# 백준 10757번
a,b = map(int, input().split())
print(a+b)      # 다른 언어에서 큰수끼리의 합은 메모리과부화로 터지지만 파이썬은 터지지않는다 그저 갓....