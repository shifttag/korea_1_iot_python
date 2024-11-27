from src import User, UserDatabase, concat

def main():
  print("user project start!!!")
  newUser = User(username='aaaa', password='1234', name='선하영', email='abcd@example.com')
  UserDatabase().insert(newUser)
  concat(1, 10)



if __name___ == "__main__":
  main()