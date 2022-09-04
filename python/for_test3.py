print("------------1------------")
"""
<결과값>
-20
-3
"""

list = [3, -20, -3, 44]

for n in list:
    if n < 0:
        print(n)


print("------------2------------")
"""
<결과값>
3
"""

list = [3, 100, 23, 44]

for n in list:
    if n % 3 == 0:
        print(n)


print("------------3------------")
"""
<결과값>
12
18
"""

list = [13, 21, 12, 14, 30, 18]

for n in list:
    if n < 20:
        if n % 3 == 0:
            print(n)


print("------------4------------")
"""
<결과값>
study
python
language
"""

list = ["I", "study", "python", "language", "!"]

for n in list:
    if len(n) > 3:
        print(n)


print("------------5------------")
"""
<결과값>
A
D
"""

list = ["A", "b", "c", "D"]

for n in list:
    if n.isupper(): #isupper: 대문자 여부 판별
        print(n)


print("------------6------------")
"""
<결과값>
b
c
"""

for n in list:
    if not n.isupper():
        print(n) 


print("------------7------------")
"""
<결과값>
Dog
Cat
Parrot
"""

list = ['dog', 'cat', 'parrot']

for n in list:
    print(n[0].upper() + n[1:]) #upper: 대문자로 변경


print("------------8------------")
"""
<결과값>
hello
ex01
intro
"""

list = ['hello.py', 'ex01.py', 'intro.hwp']

for n in list:
    split = n.split(".") #split: 문자열을 입력된 구분자로 분할해서 리스트로 반환 
    print(split[0])


print("------------9------------")
"""
<결과값>
intra.h
define.h
"""

list = ['intra.h', 'intra.c', 'define.h', 'run.py']

for n in list:
    split = n.split(".")

    if split[1] == 'h':
        print(n)


print("------------10------------")
"""
<결과값>
intra.h
intra.c
define.h
"""

for n in list:
    split = n.split(".")
    if (split[1] == 'h') or (split[1] == 'c'):
        print(n)