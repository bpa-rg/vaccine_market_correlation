import db_connection
from datetime import date
import json


def write_json(s_name, reason):
    date_string = str(date.today())
    stud_dic = {
        "name": s_name,
        "date": date_string,
        "reason": reason
    }
    json_object = json.dumps(stud_dic)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)


def read_json():
    with open('sample.json') as openfile:
        json_data = json.load(openfile)
    return json_data


def write_database():
    proxy_list = read_json()  # reading data from json
    sqlstm3 = '''INSERT INTO proxy_list
                            (student_name, `date`,reason)
                            VALUES(%s,%s,%s)'''
    recordtuple = (proxy_list['name'], proxy_list['date'], proxy_list['reason'])
    cur.execute(sqlstm3, recordtuple)
    print("Proxy_list updated")


if __name__ == "__main__":
    cur, db = db_connection.connect()
    sql = '''use aman_test'''
    cur.execute(sql)

    # creating attendance table
    stmt = '''show tables like "attendance"'''
    res = cur.execute(stmt)
    if res:
        print('attendance Table already exists')
    else:
        sqlstm = '''create table attendance
        (student_name varchar(25),date date)'''
        cur.execute(sqlstm)
        print("Attendance table created")

    # Creating proxy_list table
    stmt = '''show tables like "proxy_list"'''
    reslt = cur.execute(stmt)
    if reslt:
        print('proxy_list Table already exists')
    else:
        createstmt = '''create table proxy_list
                                 (student_name varchar(25),date date,reason varchar(50))'''
        cur.execute(createstmt)
        print("Proxy_list table created")

    # Code to check proxy attendance
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
            proxy_reason1 = "Proxy: Attendance already marked"
            print(proxy_reason1)
            write_json(s_name, proxy_reason1)
            write_database()
    else:
        proxy_reason2 = "Proxy: Student does not exists"
        print(proxy_reason2)
        write_json(s_name, proxy_reason2)
        write_database()

    db.commit()
    db.close()
