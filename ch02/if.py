num1, num2, num3 = list(map(int, input("숫자 3개 입력: ").split(" ")))

if num1 % 4 == 0:
  print("num1은 4의 배수")
elif num2 % 4 == 0:
  print("num2는 4의 배수")
elif num3 % 4 == 0:
  print("num3는 4의 배수")
else:
  print("4의 배수 없음")

# if inputNumber % 2 == 0:
#   print("짝수")
# else:
#   print("홀수")