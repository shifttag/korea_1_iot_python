print("\n")
isClose = False

# not 키워드 사용 (! 사용 대신)
# 구현부가 비워져있다는 의미로 pass를 씀
# while not isClose:
#   pass
while not isClose:
  print("반복 실행!!")
  flag = input("멈추겠습니까?(Y/N)")
  if flag in ['y', 'Y']:
    isClose = True