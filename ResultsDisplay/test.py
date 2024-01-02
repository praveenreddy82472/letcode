import mysql.connector

def Studentdatabase():
    print('--->DataBase Allocating<---')
    mydb = mysql.connector.connect(host='localhost', user='root', password='praveen987@', database='TenthResultsdb')
    print(mydb)
    print('Database Connected')





Studentdatabase()

