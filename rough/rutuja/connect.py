import py_connect
import python_funtions
import json_funtions
from datetime import date

date = str(date.today())

if __name__ == "__main__":
    cursor=py_connect.db.cursor()
    cursor.connection.commit()

    sql='''use rutuja_test'''
    cursor.execute(sql)

    sql='''select student_name from rutuja_test.Student'''
    cursor.execute(sql)
    data1=cursor.fetchall()
    data2 = list(sum(data1,()))
    print(data2)

#maximun length funtion call
result=python_funtions.max_len(data2)
print('max lenght is=',result)

#max lenght names funtion call
python_funtions.largest_name(result,data2)

#check table
python_funtions.check_table(cursor)

#check whether the student exists in the student table
#if exists then make the entry if entry is already made then add proxy.

student_name=input('enter student name')
if student_name in data2:
    sql = '''select student_name from rutuja_test.Attendance'''
    cursor.execute(sql)
    attend_data = cursor.fetchall()
    attend_data2=[i[0] for i in attend_data]

    if student_name in attend_data2:
        print('proxy')
        reason='proxy'
        #write into new json file and then write in proxy table.
        file_name=json_funtions.write_funtion(student_name,date,reason)
        #read from json file
        json_funtions.read_funtion(file_name)
    else:
        sql = '''insert into rutuja_test.Attendance(student_name,date)values(%s,%s)'''
        data3=(student_name,date)
        cursor.execute(sql,data3)
        print("attendance successfully taken")

else:
    #if student doesnot exist then add in proxy table that the student doesnot exist.
    reason="student doesnt exits in list"
    print("student doesnt exits in list")

    #write in new json file and then in proxy table
    file_name=json_funtions.write_funtion(student_name,date,reason)
    #read from json file
    json_funtions.read_funtion(file_name)

py_connect.db.commit()
cursor.close()