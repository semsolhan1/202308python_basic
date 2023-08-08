'''
* 튜플 (tuple)

- 튜플은 값의 집합이라는 측면에서는 리스트와 유사하지만
값을 한 번 저장한 후에는 내부 요소의 편집이 불가능합니다.

- 튜플은 상수 리스트라고도 부르며 ()를 사용하여 표현합니다.

- 튜플도 문자열과 리스트와 마찬가지로 시퀀스 자료형 입니다. (인덱스 o)
'''

points = (87, 97, 34, 45, 100)
print(type(points))

sum = 0
for p in points:
    sum += p
print(f'총점: {sum}점, 평균:{sum / len(points):0.1f}점')

# 튜플을 만들때는 ()를 생략할 수 있습니다.
print('-' * 40)
tu = 1, 3, 5, 7, 9
print(type(tu))

# 튜플은 리스트와 마찬가지로 unpackiging이 가능합니다.
n1, n2, n3, n4, n5 = tu
print(n1, n2, n3, n4, n5)

# 튜플로 가능한 문법(내부 요소값을 바꾸지 않는 행위)
print(tu[2])
print(tu[1:3])
print(tu + (10, 11))
print(tu * 2)
print('원본 튜플:', tu)

# 튜플로 불가능한 문법(내부 요소값을 바꾸는 행위)
# tu[2] = 19 (x)
# tu.append(10) (x)
# del(tu[0]) (x)

# tuple이 지원하는 메서드는 intdex(), count() 뿐입니다.
