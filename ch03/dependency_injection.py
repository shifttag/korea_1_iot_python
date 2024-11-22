# 의존성 주입
from dataclasses import dataclass

@dataclass
class Repository:   
  
  def insert(self, entity: dict):
    print(f"{entity} -> 데이터를 추가합니다.")

class Service:    # 의존성 주입이 된 잘 짜진 코드
  repository: Repository

  def __init__(self, repository: Repository):
    self.repository: Repository

  def addData(self, dto: dict):
    entity = dto
    self.repository.insert(entity)

# class Service:    # Service가 Repository를 의존
#   repository: Repository

#   def addData(self, dto: dict):
#     repository = Repository()
#     entity = dto
#     repository.insert(entity)

repository = Repository()
service = Service(repository)

service.addData({"name": "홍동현", "age": 25})

# 코드 가져와야함
# 실행 안됨