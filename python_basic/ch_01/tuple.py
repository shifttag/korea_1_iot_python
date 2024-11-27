# 튜플(tuple) : 리스트랑 동일한 구조(값의 구조, 수정, 삭제 불가능)
tuple1 = ()
tuple1 = tuple()

tuple1 = (1, 2, 3)
print(tuple1[1:])

tuple1 = tuple1 * 3
print(tuple1)

# tuple1.append(10) - Error

tuple2 = (10, ) # 쉼표를 찍어줌으로써 튜플로 생성
tuple3 = 1, 2, 3  # 괄호를 생략하여 생성 가능
print(tuple3)

def add(n1, n2, n3):
  return n1 + n2, n2 + n3, n1 + n3

print(add(10, 20 ,30))