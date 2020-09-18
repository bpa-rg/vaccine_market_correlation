
import py_connect
import json
from datetime import date

if __name__ == "__main__":
    cursor=py_connect.db.cursor()
    cursor.connection.commit()

    sql='''use rutuja_test'''
    cursor.execute(sql)

    sql='''select student_name from rutuja_test.Student'''
    cursor.execute(sql)
    data1=cursor.fetchall()
    #print(data1)
    data2 = list(sum(data1,()))
    print(data2)

def max_len(list):
        max=-1
        for i in data2:
            if len(i) > max:
               max = len(i)
        return max;

result=max_len(data2)
print('max lenght is=',result)

def largest_name(int):
    for i in data2:
        if len(i) == result:
            print(i)

largest_name(result)

#new_tablename=input('enter table name')

stmt = "SHOW TABLES LIKE 'Attendance'"
cursor.execute(stmt)
result = cursor.fetchone()
if result:
    print('Table exists')
else:
     sql = '''create table Attendance (student_name VARCHAR(15),date Varchar(15))'''
     cursor.execute(sql)


stmt = "SHOW TABLES LIKE 'Proxy_students'"
cursor.execute(stmt)
result = cursor.fetchone()
if result:
    print('Table exists')
else:
     sql = '''create table  rutuja_test.Proxy_students(student_name VARCHAR(15),date Varchar(15),reason Varchar(50))'''
     cursor.execute(sql)

student_name=input('enter student name')
date=date.today()
if student_name in data2:
    sql = '''select student_name from rutuja_test.Attendance'''
    cursor.execute(sql)
    attend_data = cursor.fetchall()
    attend_data2=[i[0] for i in attend_data]
    if student_name in attend_data2:
        print('proxy')

        dictionary = {
                         "name": student_name,
                         "date": date,
                         "reason":'proxy'

        }

        json_object = json.dumps(dictionary, indent=4)
        with open("sudent_record.json", "w") as outfile:
            outfile.write(json_object)

        new_file = open('sudent_record.json', )
        data = json.load(new_file)
        print(dictionary)
        new_file.close()
    else:
        sql = '''insert into rutuja_test.Attendance(student_name,date)values(%s,%s)'''
        data3=(student_name,date)
        cursor.execute(sql,data3)
        print("attendance successfully taken")
else:

    dictionary= {
                 "name": student_name,
                 "date": date,
                 "reason":"student doesnt exits in list",

                }
    print("student doesnt exits in list")

    json_object = json.dumps(dictionary, indent=4)
    with open("student_record.json", "w") as outfile:
        outfile.write(json_object)

    new_file = open('student_record.json', )
    data = json.load(new_file)

    print(data)
    student_name = dictionary["name"]
    data = dictionary["date"]
    reason = dictionary["reason"]

    sql = '''insert into rutuja_test.Proxy_students(student_name,date,reason)values(%s,%s,%s)'''
    proxy1 = (student_name, date, reason)
    cursor.execute(sql, proxy1)

    new_file.close()

#student_name=dictionary["name"]
#data=dictionary["date"]
#reason=dictionary["reason"]

#sql = '''insert into rutuja_test.Proxy_students(student_name,date,reason)values(%s,%s,%s)'''
#proxy1=(student_name,date,reason)
#cursor.execute(sql,proxy1)

py_connect.db.commit()
cursor.close()