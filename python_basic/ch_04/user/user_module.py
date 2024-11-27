from dataclasses import dataclass

# @dataclass 어노테이션: 자동으로 생성자 만들어주고, toString 역할 가능 (lombok과 비슷함!)
@dataclass
class User:
  username: str
  password: str
  name: str
  email: str

class UserDatabase:
  def insert(self, user: User):
    print(f"insert Data -> {user}")

  def select(self, username: str):
    print(f"select Data -> search username: {username}")

  def update(self, user: User):
    print(f"update Data -> {user}")

  def delete(self, username: str):
    print(f"delete Data -> search username: {username}")

if __name__ == "__main__":
  userDatabase = UserDatabase()
  userDatabase.insert(User('aaa', '1234', '김감자', 'potato@example.com'))
  newUser = User(name='강감자', password='1111', username='bbb', email='potato2@example.com')
  userDatabase.insert(newUser)