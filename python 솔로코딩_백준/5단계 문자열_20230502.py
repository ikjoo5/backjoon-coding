# 2023/05/02
'''
# 백준 1152번

    ## first draft(오답)

# 문장을 한 단어로 취급하고 공백으로 개수 구하기?

a = input()
b = 1
for x in a:
    if x == " ":
        b = b+1
print(b)            # 이런식으로 하면 단어사이에 공백이 여러개면 하나로 취급 x

    ## 정답

word = input().split()      # 꼭 단어의 개수에 맞게 abc설정안하고 a만해도 가능
print(len(word))            # input().split()에서 변수 하나만 입력하면
                            # 리스트형식으로 출력 / 여러개입력시 값을 나눔



# 백준 2908번
    ## first draft(오답)

a,b = input().split()
x = int(reversed(a))        # reverse활용방식이 틀렸다
y = int(reversed(b))

if x > y:
    print(x)
else:
    print(y)

    ## 정답1(reverse)
    
a,b = input().split()
x = int("".join(reversed(a)))        # reverse활용방식이 틀렸다
y = int("".join(reversed(b)))

if x > y:
    print(x)
else:
    print(y)

    ## 정답 2(연산자활용)
num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else :
    print(num2)
'''
'''
### reverse 요약

reversed()함수를 list나 tuple로 바꾸려면 다음과 같이 쓰면 된다.

l = ['a', 'b', 'c']
t = ('a', 'b', 'c')

list(reversed(l))  # ['c', 'b', 'a']
tuple(reversed(t)) # ('c', 'b', 'a')
l과 t 자리에 꼭 리스트와 튜플이 들어가야하는 것은 아니다.
문자열로 만들려면 join을 사용하면 된다.

l = ['a', 'b', 'c']

''.join(reversed(l))  # 'cba'
reverse() 함수는 있는데 이는 list 타입에서 제공하는 함수이다. 이는 reversed 함수와 달리 값을 반환하지 않는다.

l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
d = {'a': 1, 'b': 2, 'c': 3}
s = 'abc'

l.reverse()  # list의 순서를 뒤집어줌
t.reverse()  # AttributeError: 'tuple' object has no attribute 'reverse'
d.reverse()  # AttributeError: 'dict' object has no attribute 'reverse'
s.reverse()  # AttributeError: 'str' object has no attribute 'reverse'
l = ['a', 'b', 'c']
l_reverse = l.reverse()

print(l_reverse)  # None
print(l)  # ['c', 'b', 'a']
이를 이용하면 문제는 쉽게 풀린다.
나의 정답 코드는 다음과 같다.

a, b = input().split()
a = int(''.join(reversed(a)))
b = int(''.join(reversed(b)))
if a > b : print(a)
if a < b : print(b)
'''

