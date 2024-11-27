from moduleTest import moduleTest, moduleTest2, StudentModule

# 호출하면 __pycache__ 생성 > 패키지 관리
moduleTest()
moduleTest2()

student = StudentModule("강감자", 23)

#? import 파일명
# import moduleTest

# moduleTest.moduleTest()
# moduleTest.moduleTest2()

# student2 = moduleTest.StudentModule("김감자", 22)

print(__name__) # moduleTest