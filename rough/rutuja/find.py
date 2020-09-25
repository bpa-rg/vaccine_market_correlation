import json
import py_connect
import read_from_S3
def read_file_name(database):
    cursor = py_connect.db.cursor()
    cursor.connection.commit()

    sql = '''use '''+database
    cursor.execute(sql)
    sql="""select file_name from proxy_list where r_read=0"""
    cursor.execute(sql)
    file_name=str(cursor.fetchone())
    file_name=file_name.replace("(","")

    file_name=file_name.replace(")","")
    file_name=file_name.replace("'","")
    file_name=file_name.replace(",","")
    database=database.replace("_test","")
    print(file_name)
    file_location="devs/"+database+"/"+file_name
    print(file_location)
    data=read_from_S3.read_from_S3(file_location)
    a = json.loads(data)

    cursor = py_connect.db.cursor()
    cursor.connection.commit()

    sql = '''use rutuja_test'''
    cursor.execute(sql)

    sql="""insert into rutuja_test.Proxy_students values(%s,%s,%s,%s)"""
    data1=(a['name'],a['date'],a['reason'],database)
    cursor.execute(sql,data1)
    print("entry successfull")

    database=database+"_test"
    sql = '''use '''+database
    cursor.execute(sql)

    if(database=='swateja_test'):
        sql = '''UPDATE swateja_test.proxy_list SET r_read = 1 WHERE r_read=0;'''
        cursor.execute(sql)
    else:
        sql = '''UPDATE aman_test.proxy_list SET r_read = 1 WHERE r_read=0;'''
        cursor.execute(sql)


    py_connect.db.commit()
    cursor.close()



