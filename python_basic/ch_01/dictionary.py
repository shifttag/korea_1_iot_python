# Map 자료형
# key, value
# key 중복 불가, 순서 없음

dict1 = dict()
dict1 = {
  "name": "홍동현",
  "age": 25
}

print(dict1)

list1 = ['a', 'b', 'c']
tuple1 = 'a', 'b', 'c'
dict1 = {'10': 'aa', '20': 'bb', '30': 'cc'}

print(list1[0])
print(tuple1[0])
print(dict1['10'])

dict1['40'] = 'd'

dict1.update({'40': 'e', '50': 'f'})
print(dict1)

# value 조회
print(dict1.get('20'))
print(dict['20'])

# 쌍 삭제
print(dict1.pop('30'))
print(dict1)

print(dict1.items())

for item in dict1.items():
  print(item[1])

for value in dict1.keys():
  print(value)

keys1 - list(dict1.keys())
print(keys1)