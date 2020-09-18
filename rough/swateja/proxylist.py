import PythonConnection
import json
from datetime import date
def write(s_name, reason):
    date1 = str(date.today())
    dict = {
        "name": s_name,
        "date": date1,
        "reason": reason
    }

    json_object = json.dumps(dict)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

def read():
    with open('sample.json') as openfile:
        json_data = json.load(openfile)
    return json_data

def sql_write():
    proxy_list = read()
    sqlstm3 = '''INSERT INTO proxy(student_name, `date`,reason)VALUES(%s,%s,%s)'''
    result = (proxy_list['name'], proxy_list['date'], proxy_list['reason'])
    cursor.execute(sqlstm3, result)
    
if __name__ == "__main__":
    cursor, mydb = PythonConnection.connect()

    sql='''use swateja_test'''
    cursor.execute(sql)

    sql='''select student_name from swateja_test.student'''
    cursor.execute(sql)
    data1=cursor.fetchall()
    data2 = list(sum(data1,()))
    print(data2)



stmt = "SHOW TABLES LIKE 'Attendance'"
cursor.execute(stmt)
result = cursor.fetchone()
if result:
    print('Table exists')
else:
     sql = '''create table Attendance (student_name VARCHAR(15),date Varchar(15))'''
     cursor.execute(sql)


stmt = "SHOW TABLES LIKE 'proxy'"
cursor.execute(stmt)
result = cursor.fetchone()
if result:
    print('Table exists')
else:
     sql = '''create table  swateja_test.proxy(student_name VARCHAR(15),date Varchar(15),reason Varchar(50))'''
     cursor.execute(sql)

s_name=input('enter student name')
date=date.today()
if s_name in data2:
    sql = '''select student_name from swateja_test.Attendance'''
    cursor.execute(sql)
    attend_data = cursor.fetchall()
    attend_data2=[i[0] for i in attend_data]
    if s_name in attend_data2:
        print("proxy:attendance already marked")
        reason1 = "proxy:attendance already marked"
        print(reason1)
        write(s_name, reason1)
        sql_write()
    else:
        sql = '''insert into swateja_test.Attendance(student_name,date)values(%s,%s)'''
        data3=(s_name,date)
        cursor.execute(sql,data3)
        print("attendance is marked")
else:
    print("proxy:Not Exist")
    reason2 = "proxy: Student Not Exist"
    write(s_name, reason2)
    sql_write()
mydb.commit()
cursor.close()