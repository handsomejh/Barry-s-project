#建立数据库，并将数据导入

# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('URL_LIB.db')
# 创建一个Cursor:
cursor = conn.cursor()
#cursor.execute("select * from url_table where url like ('{idf}')".format(idf='www.taobao.com'))
cursor.execute("select * from class")
s=cursor.fetchall()
print(s)
'''
for line in open("data.txt",encoding='utf-8'):
    try:
        columns = line.split('\t')#分隔符为\t读取文件
    except:
        print("读取文件错误")
        continue
    # 在fenlei表中查询相应的大分类映射
    columns[1]=columns[1][:-1]
    try:
        cursor.execute("select big from map_table where fenlei=('{idf}')".format(idf=columns[0]))
        #记录下来对应的大分类
        big=cursor.fetchone()[0]
        # 在分类表中查询相应的小分类映射
        cursor.execute("select small from map_table where fenlei=('{idf}')".format(idf=columns[0]))
        #记录下对应的小分类
        small=cursor.fetchone()[0]
        #用小分类去查小分类表ID
        cursor.execute("select ID from class where name=('{idf}')".format(idf=small))
        #记录下ID
        ID=cursor.fetchone()[0]
        #用大分类去查大分类表PID
        cursor.execute("select PID from P_class where P_name=('{idf}')".format(idf=big))
        #记录下PID
        PID = cursor.fetchone()[0]
        #把数据插入url_table中
    except:
        print("读取错误"+big+" "+small+" "+ID+" "+PID)
        continue
    try:
        cursor.execute("insert into url_table (url,PID,ID) values ('{idf}','{idx}','{idy}')".format(idf=columns[1],idx=PID,idy=ID))
    except:
        continue
print('-'*50)

'''
#查询测试
cursor.execute("select * from url_table where ID=('{idf}')".format(idf='23.3'))
s=cursor.fetchone()
cursor.execute("select P_name from P_class where PID=('{idf}')".format(idf=s[0]))
print(cursor.fetchone()[0])
cursor.execute("select ID from url_table where url=('{idf}')".format(idf='www.baidu.com'))
s=cursor.fetchone()
cursor.execute("select name from class where ID=('{idf}')".format(idf=s[0]))
print(cursor.fetchone()[0])


# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
