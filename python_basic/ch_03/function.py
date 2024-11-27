def fx01():
  pass

# 함수 정의
def fx02():
  print("fx02 호출")

# 함수 호출
fx02()

class A:
  pass

# 파이썬, 자바스크립트는 인터프리터 언어이기 때문에 오버로딩 X > 한 줄씩 읽어서 내려오기 때문에
# 오버로딩이 하고 싶으면 상황을 나누어 주어야 함
# 매개변수에 default값을 넣어서 처리 가능
# null 대신 None 사용

# b:A | None=A() >> b에 A라는 객체가 들어오거나, 없으면 A() 객체 생성
def fx03(a:int, b:A | None=A(), c=None):
  print(a)
  print(b)
  print(c)

fx03(10)
fx03(1, "문자열", [])

def fx04(*args):
  print(args)

# 매개변수 5개가 아니라 tuple 1개 들어온 것 >> tuple은 () 생략 가능하니까!
fx04(1,2,3,4,5)

# 2번째 명시한 매개변수에 None을 허용하면 호출할 때 3번째 매개변수가 2번째로 호출이 되기 때문에 같이 default값을 잡아줘야함!
def requestGet(
    url:str | None="http://localhost",
    port:int | None=8080,
    params:dict | None=dict()):
  print(url)
  print(port)
  print(params)
  return "Response"

# None을 넣어주거나, 명시적으로 매개변수명을 넣어줌
responseDate = requestGet("http://localhost", None, {"name": "선하영", "age": 27})
# responseDate = requestGet(url="http://localhost", params={"name": "선하영", "age": 31})

# 람다는 : 뒤에 하위(줄바꿈)로 정의하지 X >> 간단한 수식을 사용할 때 사용!
# 람다는 타입 지정이 안 됨 >> :으로 지정하면 lambda의 끝으로 인식
req = lambda url="http://localhost", port=8080, params=dict(): {"url": url, "port": port, "params": params}
print(req("http://localhost", 8080, {"name": "선하영", "age": 27}))