import db_connection
from datetime import date

if __name__ == "__main__":
    cur, db = db_connection.connect()
    sql = '''use aman_test'''
    cur.execute(sql)
    stmt = '''show tables like "attendance"'''
    res = cur.execute(stmt)
    if res:
        print('Table exists')
    else:
        sqlstm = '''create table attendance
        (student_name varchar(25),date date)'''
        cur.execute(sqlstm)
    s_name = input("Enter the name of student :")
    sqlstm2 = '''select stud_name 
                from aman_test.student'''
    cur.execute(sqlstm2)
    data = cur.fetchall()
    student_list = [i[0] for i in data]
    atten_list = []
    if s_name in student_list:
        sqlstmt = '''select student_name 
                        from aman_test.attendance'''
        cur.execute(sqlstmt)
        data2 = cur.fetchall()
        atten_list = [i[0] for i in data2]
        if s_name not in atten_list:
            sqlstm3 = '''INSERT INTO attendance
                    (student_name, `date`)
                    VALUES(%s,%s)'''
            recordtuple = (s_name, date.today())
            cur.execute(sqlstm3, recordtuple)
            print("Attendance Marked")
        else:
            print("Proxy: Attendance already marked")
    else:
        print("Proxy: Student does not exists")

    db.commit()
