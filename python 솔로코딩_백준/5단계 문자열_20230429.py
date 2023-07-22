# 20230429


# 백준 10809번
'''
# solution 1
s = list(input())   ## index를 활용하기에 list형태로 출력

A ='abcdefghijklmnopqrstuvwxyz'

for i in A:
    if i in s:
        print(s.index(i), end =" ") 
    else:
        print(-1, end=" ")      # find와 다르게 index는 -1처리를 하지않아 직접입력필요

# soultion 2   find함수 활용

S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')         ## find함수는 문자열에서 검색후 위치리턴
                                        ##    없을경우 자동으로 -1처리
'''

# solution 3  아스키코드 활용

word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for x in alphabet :
    print(word.find(chr(x))) 
