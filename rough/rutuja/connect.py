
import py_connect

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

student_name=input('enter student name')
date=input('enter date')
if student_name in data2:
    sql = '''select student_name from rutuja_test.Attendance'''
    cursor.execute(sql)
    attend_data = cursor.fetchall()
    attend_data2=[i[0] for i in attend_data]
    if student_name in attend_data2:
        print('proxy')
    else:
        sql = '''insert into rutuja_test.Attendance(student_name,date)values(%s,%s)'''
        data3=(student_name,date)
        cursor.execute(sql,data3)
        print("attendance successfully taken")
else:
    print("student doesnt exits in list")


"""
for x in data2:
    if stud_name==data2:
        flag= 0
        break

    else:
        flag= 1


if(flag==0):
    sql = '''insert into  rutuja_test.Attendance values(stud_name,date)'''
    cursor.execute(sql)
else:
    print('student doesnt exist')
"""
py_connect.db.commit()
cursor.close()