import PythonConnection
from datetime import date

if __name__ == "__main__":
    cur, mydb = PythonConnection.connect()
    sql = '''use swateja_test'''
    cur.execute(sql)
    stmt = '''show tables like "attendance"'''
    result = cur.execute(stmt)
    if result:
        print('Table Exists')
    else:
        sql1 = '''create table attendance
        (student_name varchar(25),date date)'''
        cur.execute(sql1)
    s_name = input("Enter the name of student :")
    #compare the student list
    sql2 = '''select student_name from swateja_test.student'''
    cur.execute(sql2)
    data = cur.fetchall()
    student_list = [i[0] for i in data]
    attendance_list = []
    if s_name in student_list:
        sql = '''select student_name 
                        from swateja_test.attendance'''
        cur.execute(sql)
        data2 = cur.fetchall()
        attendance_list = [i[0] for i in data2]
        if s_name not in attendance_list:
            sqlstm3 = '''INSERT INTO attendance
                    (student_name, `date`)
                    VALUES(%s,%s)'''
            resultdata = (s_name, date.today())
            cur.execute(sqlstm3, resultdata)
            print("Attendance Marked")
        else:
            print("Proxy: Attendance already marked")
    else:
        print("Proxy: Student does not exists")

    mydb.commit()
