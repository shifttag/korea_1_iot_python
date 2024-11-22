from dataclasses import dataclass
from overrides import overrides

@dataclass
class Person:
  name: str
  age: int

  def move(self):
    print(f"""{self.name}({self.age})님이 움직입니다.""")

@dataclass
class Student(Person):
  score: int

  def study(self):
    print("공부를 합니다")

  @overrides
  def move(self):
    super().move()
    print("학생이 움직입니다")

@dataclass
class Teacher(Person):
  subject: str

  def lesson(self):
    print("수업을 합니다.")
  
  @overrides
  def move(self):
    print("선생이 움직입니다")

person = Person(name="이름모르는사람", age=30)
student = Student(name="황상기", age=33, score=60)
teacher = Teacher(name="김준일", age=31, subject="python")

print(person)
print(student)
print(teacher)

person2:Person = student
print(person2)

person3:Teacher = person2
print(person3)

print(isinstance(person3, Student))

persons = [ person, student, teacher ]

for p in persons:
  p.move()
  if isinstance(p, Student):
    p.study()
  elif isinstance(p, Teacher):
    p.lesson()