print()

nums = [10, 20 , 30, 40]

# forEach와 같은 역할
for num in nums:
  print(num)

nums = range(10)
print(list(nums)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
  print(i) # 0부터 10 전까지의 숫자 출력

nums = range(10, 20)
print(list(nums)) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

nums = range(10, 20, 2) 
print(list(nums)) # [10, 12, 14, 16, 18]

for i in range(10):
  pass

# for (int i = 0; i < 10; i++) {

# } // 위와 같은 형태

for i in range(10):
  for j in range(5):
    print(f'i: {i}, j: {j}')

# cf) 줄바꿈 없애기
# print("aaaaa", end="")
# print("bbbbb") # aaaaabbbbb 한 줄로 붙어서 출력

'''
*        *****
**       **** 
***      *** 
****     **
*****    * 
'''

for i in range(1, 6):
  # print("*" * i, end="\t\t")
  # print("*" * (6 - i))
  print(f'{"*" * i}\t\t{"*" * (6 - i)}')

for i in range(5, 0, -1):
  print("*" * i)

# for i in range(5):
#   print("*" * (i + 1), " " * (5 - i))

# for i in range(5):
#   print("*" * (5 - i), " " * i)

# for i in range(5):
#   for j in range(i + 1):
#     print("*", end="")
#   print()

# for i in range(5):
#   print("*" * (i + 1))

# for i in range(5):
#   print("*" * (5 - i))