import pymysql

def saveCoupangData(coupangData: list):
    try:
        connection = pymysql.connect(host='localhost',port=3306,user='root',passwd='hongdong2@',db='coupang_db')
        try:
            cursor = connection.cursor()
        except Exception as e:
            print(e)    # SQL 오류
        finally:
            connection.close()

        connection.close()
    except Exception as e:
        print("데이터베이스 연결 실패")