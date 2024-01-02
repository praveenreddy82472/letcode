import mysql.connector

from log import logging

#from python.ResultsDisplay.build import marks


def StudentdatabaseMarksWise(x,y,z,w,t,h,e,m,s,s1):

    logging.info("MarksWiseDatabase Requested Allowed")
    mydb = mysql.connector.connect(host='localhost', user='root', password='praveen987@', database='tenthResultsdb')
    logging.info("MarksWise Database Created")
    print('MarksWise Database Connected')
    dn = mydb.cursor(buffered=True)
    print('0.exit')
    print('1.created')
    print('2.Read')
    print('3.inserted')
    print('4.delete')
    option = int(input('Enter the option:'))
    while True:
        if option == 1:
            dn.execute("Create TABLE markswise(name VARCHAR(255), DOB VARCHAR(255), Results VARCHAR(255), TotalMarks VARCHAR(255),Telugu VARCHAR(255), Hindi VARCHAR(255), English VARCHAR(255), MathaMetics VARCHAR(255),Science VARCHAR(255),SocialStudies VARCHAR(255))")
            print("table created")
            logging.info("Table Created")
            option = int(input('Enter the option:'))
            # print(option)
        elif option == 3:
            sql = "insert into markswise(name,DOB,Results,TotalMarks,Telugu,Hindi,English,MathaMetics,Science,SocialStudies) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            record = (x, y, z, w, t, h, e, m, s, s1)
            dn.execute(sql, record)
            mydb.commit()
            print('Records Inserted Successfully')
            logging.info("Inserted the data into database")
            option = int(input('Enter the option:'))
            # print(option)
        elif option == 2:
            print('Read the data')
            dn.execute('select * from markswise')
            data = dn.fetchall()
            for i in data:
                print(i)
                logging.info('Reading the from database')
            option = int(input('Enter the option:'))
            # print(option)
        elif option == 0:
            logging.info("Exit the database")
            break
