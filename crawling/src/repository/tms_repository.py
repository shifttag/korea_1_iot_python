import pymysql

def findBoard(webtoonTitle: str):
    foundWebtoon = None
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='hongdong2@', db='naver_webtoon_db')
        try:
            cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
            sql = f"""
select 
    wt.webtoon_id, 
    wt.title, 
    group_concat(at.author_name SEPARATOR ' / ') as author, 
    wt.rating, 
    wt.img_url, 
    ct.category_name 
from
    webtoon_tb wt
    left outer join author_group_tb agt on(agt.webtoon_id = wt.webtoon_id)
    left outer join author_tb at on(at.author_id = agt.author_id)
    left outer join category_tb ct on(ct.category_id = wt.category_id)
where
    wt.title = %s
group by
    wt.webtoon_id, 
    wt.title,
    wt.rating,
    wt.img_url,
    ct.category_name"""
            cursor.execute(sql, (webtoonTitle))
            result = cursor.fetchone()
            result['rating'] = float(result['rating'])
            return result
        except Exception as e:
            print("SQL 오류", e)
        finally:
            connection.close()
    except Exception as e:
        print("데이터베이스 연결 실패", e)




'''
    1. console에서 input() webtoon 제목을 하나 입력 받는다.
    2. 해당 제목의 webtoon 정보를 DB에서 select한다.
    {
        webtoonId: 1,
        title: "참교육",
        author: "채옹택 / 한가람",
        rating: 9.89,
        imgUrl: "https://~~~~",
        categoryName: "월"
    }
    3. 제목 -> 홍동현(웹툰 제목: 참교육)
        내용 -> webtoonId: 1, 
                title: "참교육", 
                author: "채옹택 / 한가람", 
                rating: 9.89, 
                imgUrl: "https://~~~~",
                categoryName: "월"
'''