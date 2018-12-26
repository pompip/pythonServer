import sqlite3

class StudentTable:

    def create(self):
        comm = sqlite3.connect("blog.db")
        cursor = comm.cursor()
        cursor.execute('create table student (id primary key,name ,age)')
        cursor.close()
        comm.commit()
        comm.close()

    def insert(self,id,name,age):
        comm = sqlite3.connect("blog.db")
        cursor = comm.cursor()
        cursor.execute('insert into student (id,name,age) values ("%s","%s","%s")'%(id,name,age))
        cursor.close()
        comm.commit()
        comm.close()

    def find(self):
        comm = sqlite3.connect("blog.db")
        cursor = comm.cursor()
        cursor.execute("select * from student")
        values = cursor.fetchall()
        cursor.close()
        comm.commit()
        comm.close()
        return values

table = StudentTable()
# table.create()
# table.insert("5","chong3","23")
for student in table.find():
    print(student)