set1 = set()
set1 = {'a', 'b', 'c'}

print(set1)
print(set1.pop())
print(set1)

for data in set1:
  if data == 'b':
    print(data)

set2 = {1, 2, 3, 4}
set3 = set1.union(set2)
print(set3)

print(set1 & set2)

set4 = set([1,1,1,2,3,4,5,5,5])
print(set4)

print(set1 - set2)