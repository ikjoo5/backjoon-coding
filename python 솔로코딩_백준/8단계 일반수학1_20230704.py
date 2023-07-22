### 2023-07-04
'''
# 백준 2292번
n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)
'''


# 백준 1193번
#### 존나 어렵고 헷갈리니까 다시 복습하자
 # 규칙을 찾는게중요하다
n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line%2 == 0: #짝수 라인 일때
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print("%d/%d"%(top,bottom))