# 2023-05-15

# 백준 4344번
'''
import sys
input = sys.stdin.readline

test_case = int(input())

for x in range(test_case):
    N = list(map(int, input().split()))     # 리스트로 묶어서 표현 가
    t = sum(N[1:])
    avg = t / N[0]
    count = 0           # 평균 넘는 학생들을 구하기위해 여기서 카운트 0 선언
    for y in N[1:]:     # N리스트안의 첫번째값을 제외한 수들
        if y > avg:     # 평균값을 넘는 개수 셈하는 함수식
            count = count + 1
    rate = (count / N[0]) * 100
    print(f'{rate:.3f}%')   # f-string 표기법 활용
            
'''
# 백준 2941번

## 내답 ㅅㅂ 반성하자......
word = input()
a = word.count("c=")
b = word.count("c-")
c = word.count("dz=")
d = word.count("d-")
e = word.count("lj")
f = word.count("nj")
g = word.count("s=")
h = word.count("z=")
total = a + b+c+d+e+f+g+h
print(len(word) - total)

# 모범답안

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # replace 함수를 쓰면 간단하다...
print(len(word))

    
