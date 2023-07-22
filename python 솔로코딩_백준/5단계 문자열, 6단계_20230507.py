# 2023-05-07

# 백준 5622번
'''
# 내답 = 쓰레기 슈발...
a = input()
time = 0
for x in a:
    if x == 'A' or x=='B' or x=='C':
        time = time + 3
    elif x == 'D' or x=='E' or x=='F':
        time = time + 4
print(time)

# 내답 수정
if x == 'A' or 'B' or 'C':

if x == 'A' or x=='B' or x=='C':

로 바꿔야 합니다.

B는 True로 취급되기에 어떤 글자가 들어와도 else if문으로 들어가지 않습니다.

if x == 'A' or 'B' or 'C':는  if True: 와 같다고 보시면 됩니다.


# 모법답안
alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alpabet_list :  
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in word :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                time += alpabet_list.index(unit) +3  # time = time + index +3
                # +3인 이유는 index는 0부터 시작하고 1은 2초이기때문에 3을더해 맞춘다
print(time)


# 모범답안 2

arr = [['A','B','C'], #3초 
       ['D','E','F'],
       ['G','H','I'],
       ['J','K','L'],
       ['M','N','O'],
       ['P','Q','R','S'],
       ['T','U','V'],
       ['W','X','Y','Z']]

sum = 0 
word = input()

for munja in word :
    time= 3
    for each_arr in arr :
        if munja in each_arr:
            break               # 만약 문자가 arr안에 없다면 break대신 +1이다. 천재다....
        time +=1

    sum +=time

print(sum)  
'''

# 백준 25083 6단계 심화
print("         ,r\'\"7")
print("r`-_   ,\'  ,/")
print(" \\. \". L_r\'")
print("   `~\\/")
print("      |")
print("      |")