# 2023-05-14

# 백준 1157번    (복습 필요!!)

a = input()
word = a.upper()    # word = baaa

word_list = list(set(word)) # set는 리스트안의 중복제거 thus word_list = [b,a]
cnt=[]

for i in word_list:         
    count = word.count(i)
    cnt.append(count)       # word안의 알파벳 counting -> cnt = [1,3]

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))])

    
