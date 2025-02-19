import mysql.connector as connection

mydb=connection.connect(host="localhost",user="root",passwd='123wer')

cursor=mydb.cursor()

cursor.execute('select * from sudhanshu.ineuron')

for i in cursor.fetchall():
    print(i)