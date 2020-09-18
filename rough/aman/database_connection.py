import pymysql


def connect():
    db = pymysql.connect('bparg-dev.c77oqtjkwuky.us-east-2.rds.amazonaws.com', 'admin', 'admin123')
    cursor = db.cursor()
    return cursor, db


if __name__ == "__main__":
    cur, db = connect()
    sql = '''select stud_name 
             from aman_test.student'''
    try:
        cur.execute(sql)
        data = cur.fetchall()
        student_list = [i[0] for i in data]
        s_name = max(student_list, key=len)
        print("Longest name is", s_name)
    except:
        print("Error: unable to fetch data")

    db.close()
