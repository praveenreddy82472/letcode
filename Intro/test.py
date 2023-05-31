import mysql.connector
def database():
    x = self.name
    y = self.age
    z = self.number
    print('--->DataBase Allocating<---')
    mydb = mysql.connector.connect(host='localhost', user='root', password='praveen987@', database='praveendb1')
    print('Database Connected')
    dn = mydb.cursor(buffered=True)
    option = int(input('Enter the option:'))
    print('1.created')
    print('2.Read')
    print('3.inserted')
    print('4.delete')
    while True:
        if option == 1:
            dn.execute("Create TABLE drf(name VARCHAR(255), age VARCHAR(255), number VARCHAR(255))")
            print("table created")
            option = int(input('Enter the option:'))
            #print(option)
        elif option == 3:
            sql = "insert into drf(name,age,number) VALUES (%s,%s,%s)"
            record = (x,y,z)
            dn.execute(sql, record)
            mydb.commit()
            print('Records Inserted Successfully')
            option = int(input('Enter the option:'))
            #print(option)
        elif option == 2:
            print('Read the data')
            dn.execute('select * from drf')
            data = dn.fetchall()
            for i in data:
                print(i)
            option = int(input('Enter the option:'))
            #print(option)
        else:
            print('Invalid option')
            option = int(input('Enter the option:'))
            break
            #print(option)

database()