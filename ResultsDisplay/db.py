import mysql.connector
import sys
from log import logging

#from python.ResultsDisplay.build import marks


def Studentdatabase(x,y,z,w):

    print('--->DataBase Allocating<---')
    logging.info("Database Requested Allowed")
    mydb = mysql.connector.connect(host='localhost', user='root', password='praveen987@', database='tenthResultsdb')
    logging.info("Database Created")
    print('Database Connected')
    dn = mydb.cursor(buffered=True)
    print('0.exit')
    print('5.show_databases')
    print('1.created')
    print('2.Read')
    print('3.inserted')
    print('4.delete')
    option = int(input('Enter the option:'))
    while True:
        if option == 1:
            dn.execute("Create TABLE grade(name VARCHAR(255), DOB VARCHAR(255), Results VARCHAR(255), TotalMarks VARCHAR(255) )")
            print("table created")
            logging.info("Table Created")
            option = int(input('Enter the option:'))
            # print(option)
        elif option == 3:
            sql = "insert into grade(name,DOB,Results,TotalMarks) VALUES (%s,%s,%s,%s)"
            record = (x, y, z, w)
            dn.execute(sql, record)
            mydb.commit()
            print('Records Inserted Successfully')
            logging.info("Inserted the data into database")
            option = int(input('Enter the option:'))
            # print(option)
        elif option == 2:
            print('Read the data')
            dn.execute('select * from grade')
            data = dn.fetchall()
            for i in data:
                print(i)
                logging.info('Reading the from database')
            option = int(input('Enter the option:'))
            # print(option)
        elif option == 5:
            print("show the tables in databases")
            # Define the SQL query to delete all rows from the table
            delete_query = "SHOW TABLES"
            # Execute the delete query
            dn.execute(delete_query)
            # Fetch all table names
            tables = dn.fetchall()
            # Print the table names
            print("Tables in the database:")
            for table in tables:
                print(table[0])
            mydb.commit()
            option = int(input('Enter the option:'))
        elif option == 4:
            pass
        elif option == 0:
            logging.info("Exit the database")
            break
