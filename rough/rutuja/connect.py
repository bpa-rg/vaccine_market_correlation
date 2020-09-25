import py_connect
import python_funtions
import json_funtions
from datetime import date
import upload_file_to_S3_
import find
import read_from_S3
#import read_from_S3
#import json

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
        file_location='C:\\Users\\SAI\\PycharmProjects\\pythonProject\\'
        file_location+=file_name
        sql = '''insert into rutuja_test.proxy_list(file_name,r_read)values(%s,%s)'''
        data3 = (file_name, 1)
        cursor.execute(sql, data3)
        print("filename successfully taken")
      #  uploaded = upload_file_to_S3_.upload_to_aws(file_location,'bpa-rg-rough', 'devs/rutuja', file_name)
        print(file_name)
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

    file_location = 'C:\\Users\\SAI\\PycharmProjects\\pythonProject\\'
    file_location += file_name
    sql = '''insert into rutuja_test.proxy_list(file_name,r_read)values(%s,%s)'''
    data3 = (file_name, 1)
    cursor.execute(sql, data3)
    print("filename successfully taken")

    # uploaded = upload_file_to_S3_.upload_to_aws(file_location, 'bpa-rg-rough', 'devs/rutuja', file_name)
    print(file_name)

    #read from json file
    json_funtions.read_funtion(file_name)

#take parameter from user.
dbname=input("enter database")

#find the file name from s3
find.read_file_name(dbname)

py_connect.db.commit()
cursor.close()