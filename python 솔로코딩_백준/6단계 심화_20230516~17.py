# 2023-05-16 ~ 05-17

# 백준1316번
'''
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:        # 수가 연속이면 다음 j로 passing
            pass
        elif word[j] in word[j+1:]:     # 위에 if가정이 false일경우 문자를 스캔하여 오류탐색
            cnt -= 1
            break

print(cnt)
'''

# 백준 25206번 (복습필수)

rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total_gpa = 0
total_grade = 0
for _ in range(20):
    subject, gpa, grade = input().split()
    gpa = float(gpa)        # 실수형으로 만들어준다 int 사용x b/c 예제에 3.0등으로 이루어짐
    if grade != 'p':
        total_gpa += gpa
        total_grade += gpa * grade_list[rating.index(grade)]   # 학점 * 과목평점
    elif grade == 'p':
        break

print('%.6f' % (total_grade / total_gpa))

        
        
    
    

