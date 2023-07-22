'''
# 백준 1546번

import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))         # list안의 변수추가
max_score = max(m)

new_m = []
for x in m:                 # in range가 아니라 m 자체를 소환해서 리스트순환가능
    new_m.append(x / max_score *  100)
    
# print(sum(new_m) / n)       # list / int 형태이기 떄문에 런타임 error가 뜬다
avg = sum(new_m) / n
print(avg)


###### 5단계 문자열

# 백준 27866번 
import sys
input = sys.stdin.readline

s = list(input())               #  꼭 list형태로 만들지 않아도 []가 사용가능
i = int(input())                #  ex) 그냥 input()이어도 s[]가 작동한다
print(s[i-1])



# 백준 2743번

a = list(input())
print(len(a))
'''


# 백준 9086번

import sys
input= sys.stdin.readline

T = int(input())
a = []
for _ in range(T):
    a = list(input())
    print(a[0]+a[-2])        # list의 마지막은 -1을 통해 불러낼수 있다.
                             # 다만 이문제의 경우 for문으로 인해 -1은 \n 따라서 -2를 불러낸다
