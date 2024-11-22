# num1 = int(input("숫자1: "))
# num2 = int(input("숫자2: "))

# 입력값: 10, 20 or 10 20
# num1AndNum2 = input("숫자1, 숫자2: ").split(", ")
num1AndNum2Input = input("숫자1, 숫자2: ").replace(",", "").split(" ")
num1AndNum2 = list(map(int, num1AndNum2Input))
print(num1AndNum2)

num1, num2 = num1AndNum2
print(num1)
print(num2)

nums = ['1', '2', '3', '4']
num2 = map(int, nums)
print(num2)
def parseInt(strNum):
  return int(strNum)
num3 = list(map(parseInt, nums))
print(num3)

# nums.map(strNum => int(strNum)) 위에 함수와 list형식 반환

nums4 = list(map(lambda strNum: int(strNum), nums))