import pymysql

db=pymysql.connect(host='localhost',user='root',password='wangdan',db='test',port=3306)

cur=db.cursor()
# 创建用户表
sql='create table user (id varchar(20) primary key, name varchar(20))'
# cur.execute(sql)
# 插入一行记录，注意mysql的占位符是%s
cur.execute('insert into user(id,name) values (%s,%s)',['1','Michael'])
print(cur.rowcount)
# 提交事务
db.commit()
cur.close()

# 运行查询
cursor=db.cursor()
cursor.execute('select * from user where id =%s',('1',))
values=cursor.fetchall()
print(values)
# 关闭Cursor和Connection
cursor.close()
db.close()