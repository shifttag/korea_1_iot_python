# 선언 및 초기화 방법
list1 = [1, 2, 3, 4]
# list1 = list()

print(list1[0])
print(list1[0:2])

print(list1.index(3))

list1.append(5) # 해당 값을 리스트 마지막에 추가
list1.pop(2)  # 해당 인덱스 번호 삭제 후 리턴
list1.remove(1) # 해당 값 삭제
print(list1)

list2 = list1[:]  # 깊은 복사 방법
list2.sort()
print(list2)
list2.reverse()
print(list2)

list2.append(4)

print(list2)
list1.insert(1, 10)
print(list1)

list2.clear()

list3 = list1.copy()  # 깊은 복사 방법

list1.extend(list3)
print(list1)

print(list3 + [1, 2, 3, 4])
print(list3 * 3)

list4 = [1, "홍동현", [10, 20], 3.14, [30, 40]]
print(list4)

print(list4[2::2])