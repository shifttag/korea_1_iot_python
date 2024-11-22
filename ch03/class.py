# 변수, 메소드
class User:
  
  def __init__(self, username:str, password:str, name:str, email:str|None="", address:str|None=""): 
    self.username = username
    self.password = password
    self.name = name
    self.email = email
    self.address = address

  def getUserInfo(self):
    return f'''
username: {self.username}
password: {self.password}
name: {self.name}
email: {self.email}
address: {self.address}
'''
  
user1 = User(username="aaaa", password="1234", name="홍동현");
print(user1.getUserInfo())

user2 = User(username="bbbb", password="1111", name="홍길동", email="bbbb@test.com", address="부산")
print(user2.getUserInfo())


'''
class Student
name  - str 필수
age   - int 필수
address   - str 선택

incrementAge() -> 호출되면 무조건 age 1씩 증가

getStudentInfo() -> 학생 정보 전체 출력
'''

class Student:
  def __init__(self, name: str, age: int, address: str|None=""):
    self.name = name
    self.age = age
    self.address = address

  def incrementAge(self):
    self.age = self.age + 1

  def getStudentInfo(self):
    return f'''
name: {self.name}
age: {self.age}
address: {self.address}
'''
  
student1 = Student(name="누구", age=14)
print(student1.getStudentInfo())
student1.incrementAge()
print(student1.getStudentInfo())

# def getNameAndAge(name="", age):    default가 앞 인자에 있으면 불편함
#   return f"이름: {name}, 나이: {age}"

# getNameAndAge("홍동현", 20)

from dataclasses import dataclass

@dataclass
class Student2:
  name: str = ""
  age: int = 0
  address: str | None = ""

  student2 = Student(name="홍동현")
  print(student2)