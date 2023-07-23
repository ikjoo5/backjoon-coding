### 2023-07-23

### Stack 문제풀이
'''
### BOJ 9012번

T = int(input())

for _ in range(T):
    stack = []
    test = input()
    for x in test:      # 입력에 공백이 없어 일일이 분리시켜 스택(리스트)에 주입
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack:   # if stack is not empty
                stack.pop()
            else:       # stack is empty
                print("NO")
                break
        
    else:       # break로 끓기지 않았을떄 수행
                # else 없이 아래코딩만 주입하면 NO와 YES가 동시에 출력된다
        if stack:       # 위과정이 끝나고 stack"("이 존재하면 wrong
            print("NO")
        else:
            print("YES")



### BOJ 4949번

# 내답 (오류) / ([ (([( [ ] ) ( ) (( ))] )) ]). 해결불가
while True:
    stack_1 = []
    stack_2 = []
    sentence = input()

    if sentence[0] == '.':
        break

    for x in sentence:
        if x == '(':
            stack_1.append(x)
        elif x == '[':
            stack_2.append(x)
        
        elif x==')':
            if stack_2:     # stack_2 '[' 가 존재한다는것은 ']' 가 밖에 있다는 뜻이라 오류
                print('no')
                break
            elif stack_1:
                stack_1.pop()
            else:
                print("no")
                break
        elif x ==']':
            if stack_1:     # 위에 케이스와 동일
                print("no")
                break
            elif stack_2:
                stack_2.pop()
            else:
                print("no")
                break
    else:
        if stack_1 or stack_2:
            print("no")
        else:
            print("yes")

# 모범답안 
    # '['와 '('를 같이 스택해줘야된다

while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')

'''
### BOJ 1874번

n = int(input())

stack = []

for i in range(n):
    m = int(input())
    

