#1
print("------------1------------")
"""
<결과값>
110
210
310
"""

list = [100, 200, 300]

for n in list:
    print(n + 10)


#2
print("------------2------------")
"""
<결과값>
오늘의 메뉴: 김밥
오늘의 메뉴: 라면
오늘의 메뉴: 튀김
"""

list = ["김밥", "라면", "튀김"]

for s in list:
    print("오늘의 메뉴: " + s)


#3
print("------------3------------")
"""
<결과값>
6
4
4
"""

list = ["SK하이닉스", "삼성전자", "LG전자"]

for s in list:
    print(len(s))


#4
print("------------4------------")
"""
<결과값>
dog 3
cat 3
parrot 6
"""

list = ['dog', 'cat', 'parrot']

for s in list:
    print(s, len(s))



#5
print("------------5------------")
"""
<결과값>
d
c
p
"""

for s in list:
    print(s[0])


#6
print("------------6------------")
"""
<결과값>
3 x 1
3 x 2
3 x 3
"""

list = [1, 2, 3]

for n in list:
    print("3 x", n)


#7
print("------------7------------")
"""
<결과값>
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
"""

for n in list:
    print("3 x", n, "=", 3*n)


#8
print("------------8------------")
"""
<결과값>
나
다
라
"""

list = ["가", "나", "다", "라"]

for s in list[1:]:
    print(s)


#9
print("------------9------------")
"""
<결과값>
가
다
"""

for s in list[ : :2]: #[시작:끝:증감폭]
    print(s)


#10
print("------------10------------")
"""
<결과값>
라
다
나
가
"""

for s in reversed(list):
    print(s)
