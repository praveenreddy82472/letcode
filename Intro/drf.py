import mysql.connector
class info:
    def __init__(self,name,age,number):
        self.name = name
        self.age = age
        self.number = number
    def printed(self):
        print("#" * 20, "CHEJERLA REDDY'S FOUNDATION", "#" * 20)
        print(" " * 20, "___________________________", " " * 20)
        result = "Name:{0}\tAge:{1}\tNumber:{2}".format(self.name, self.age, self.number)
        print(result)
    def __str__(self):
        result = "Name:{0}\tAge:{1}\tNumber:{2}".format(self.name, self.age, self.number)
        return result
    def show(self):
        f = open('coo.txt','a')
        i = info.__str__(self)
        f.write(i+'\n')
        f.close()

    def database(self):
        x = self.name
        y = self.age
        z = self.number
        print('--->DataBase Allocating<---')
        mydb = mysql.connector.connect(host='localhost', user='root', password='praveen987@', database='praveendb1')
        print('Database Connected')
        dn = mydb.cursor(buffered=True)
        print('1.created')
        print('2.Read')
        print('3.inserted')
        print('4.delete')
        option = int(input('Enter the option:'))
        while True:
            if option == 1:
                dn.execute("Create TABLE drf(name VARCHAR(255), age VARCHAR(255), number VARCHAR(255))")
                print("table created")
                option = int(input('Enter the option:'))
                # print(option)
            elif option == 3:
                sql = "insert into drf(name,age,number) VALUES (%s,%s,%s)"
                record = (x, y, z)
                dn.execute(sql, record)
                mydb.commit()
                print('Records Inserted Successfully')
                option = int(input('Enter the option:'))
                # print(option)
            elif option == 2:
                print('Read the data')
                dn.execute('select * from drf')
                data = dn.fetchall()
                for i in data:
                    print(i)
                option = int(input('Enter the option:'))
                # print(option)
            else:
                print('Invalid option')
                option = int(input('Enter the option:'))
                break

def list1():
        f = open('coo.txt','r')
        r1 = f.read()
        print('Printing the Detail of Members in the Group')
        print(' '*4,"--Name--",'  '*1,"--Age--",'  '*2,"--Number--")
        print(r1)


while True:
    option = input('Do you want to Enter the Details[yes|no]:')
    if option == 'yes':
        name = input("Enter Name:")
        age = int(input("Enter age:"))
        number = input("Enter Number:")
        i = info(name,age,number)
        i.__str__()
        i.show()
        i.database()
    else:
        list1()
        break





