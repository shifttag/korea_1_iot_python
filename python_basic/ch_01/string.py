name = "홍동현"

print(name)

# 문자열 사이에 문자열 추가 (join)
print(",".join(name))

# f포맷, 표현식 (fString)
print(f"{name}입니다")

# 문자열 안에서 찾고자 하는 문자열의 위치 반환
print(name.index('홍')) # index를 찾을 수 없으면 Error
print(name.rfind("동")) # 여러 개의 단어가 있다면 뒤에 단어의 글자 인덱스 반환
print(name.find('이'))  # index를 찾을 수 없으면 -1 

# 문자열 안에서 찾고자하는 문자열의 개수 반환
print(name.count('홍'))

# 문자열 길이
print(name.__len__())
print(len(name))

# 문자열 양 끝 공백 제거, lstrip: 왼쪽 공백 제거, rstrip: 오른쪽 공백 제거
print("  이름  ".strip())
print("  이름  ".lstrip())
print("  이름  ".rstrip())

# 문자열에서 수정 할 문자를 탐색하여 대체할 문자로 대입
print("010-1234/5678".replace("/", "").replace("-", ""))

# spilt 할 문자를 기준으로 나누어 list형태로 반환
print("홍동현, 홍길동, 홍삼".split(","))

address = "부산광역시 동래구 사직동 아파트 201동 201호"

# 인덱싱, 슬라이싱
print(address[0]) # 인덱싱
print(address[2:4]) # 슬라이싱
print(address[:4])
print(address[4:])
print(address[-1:])

print(address[:address.find("시 ") + 1])  # 부산광역시
print(address[address.find("시 ") + 2:address.find("구 ") + 1]) # 동래구

addressList = address.split(" ")
address1 = addressList[0]
address2 = addressList[1]
address3 = " ".join(addressList[2:])

print(f"주소 1: {address1} \n주소 2: {address2} \n주소 3: {address3} ")
print(f"""주소 1: {address1} 
주소 2: {address2} 
주소 3: {address3} """)

print("*" * 20)
print("1. 회원가입")
print("2. 로그인")
print("*" * 20)