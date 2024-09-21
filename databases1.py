import pymysql # type: ignore
con=pymysql.connect(host='localhost',user='root',password='Nikita0421@V')
print("connection opened successfully")
obj_cursor=con.cursor()
str_query='show databases'
row_affected=obj_cursor.execute(str_query)
print(row_affected)
res_set=obj_cursor.fetchall()
for e in res_set:
    for e1 in e:
        print(e1,end='')
    print()