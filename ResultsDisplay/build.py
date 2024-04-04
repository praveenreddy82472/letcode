from filehandling import *
from db import *
from db1 import *
from datetime import datetime
from mongodb import mongodb
import json
class marks:

    def __init__(self,name,DOB):
        self.name = name
        self.DOB = DOB
        #self.Result = Result
        #self.TotalMarks = TotalMarks
        self.date = datetime.now()
        logging.info('Build Class Started')

    def subject(self):
        print('')
        logging.info("Students Enter the subject wise marks")
        print('Enter the Marks of the subjects---->>>>>>>>')
        print(" ")
        self.Telugu = int(input('Telugu:'))
        self.Hindi = int(input('Hindi:'))
        self. English  = int(input('English:'))
        self.MatheMatics = int(input('MatheMatics:'))
        self.Science = int(input('Science:'))
        self.SocialStudies = int(input('SocialStudies:'))
        self.TotalMarks = self.Telugu+self.Hindi+self.English+self.MatheMatics+self.Science+self.SocialStudies

    def Final(self):
        if self.Telugu >=35  and self.Hindi >= 35 and self.English >= 35 and self.MatheMatics >= 35 and self.Science >= 35 and self.SocialStudies >= 35:
            self.Result = "Pass"
            logging.info("Student Result Processing")
            print(self.Result)
        else:
            self.Result = "Fail"
            print(self.Result)

    def subjectsMarks(self):
        print(" ")
        print("Subject Wise Marks --->>>>>>>>>>>>>>>>>>")
        print(" ")
        print(">> Telugu:",self.Telugu)
        print(">> Hindi:",self.Hindi)
        print(">> English:",self.English)
        print(">> MatheMatics:",self.MatheMatics)
        print(">> Science:",self.Science)
        print(">> SocialStudies:",self.SocialStudies)
        print(">> TotalMarks:",self.TotalMarks)


    def __str__(self):
        print("-<>----<>----<>----<>-----<>-----<>--------<>-------<>------<>------<>-")
        print("AndhraPradesh")
        print("Secondary School Education")
        print("-<>----<>----<>----<>-----<>-----<>--------<>-------<>------<>------<>-")
        print('10th Class Final Examination Results')
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print('Name:',self.name)
        print('DOB:',self.DOB)
        print('Result:',self.Result)
        print('TotalMarks:',self.TotalMarks)
        logging.info('String function execution')
    def store(self):
        logging.info('Store the Result to a Variable')
        result = f"Date:{self.date} \t Name:{self.name} \t DOB:{self.DOB} \t TotalMarks:{self.TotalMarks} \t Result:{self.Result}"
        return result

    def data_to_store_infile(self):
        file_path = 'example.txt'  # text file
        file_mongodb = "jsonfile.json"
        data_to_append = self.store()  # create a variable to store information
        result_text = append_to_file(file_path, data_to_append)  # calling function of filehandling
        #print(result_text)


        #string to json data into the file
        result = f"Date:{self.date}  Name:{self.name}  DOB:{self.DOB}  TotalMarks:{self.TotalMarks}  Result:{self.Result}"
        data = json.dumps(result)
        result_json = append_to_file(file_mongodb, data)  # calling function of filehandling
        #print(result_json)

    def databasecalling(self):
        logging.info('database accessing')
        Studentdatabase(self.name, self.DOB, self.Result, self.TotalMarks)
        StudentdatabaseMarksWise(self.name, self.DOB, self.Result, self.TotalMarks,self.Telugu,self.Hindi,self.English,self.MatheMatics,self.Science,self.SocialStudies)
        data = [{
            "Date": str(self.date),
            "Name": self.name,
            "DOB": self.DOB,
            "TotalMarks": self.TotalMarks,
            "Result": self.Result
        }]
        mongodb(data)


if __name__ == "__main__":

    while True:


        Name = input("Enter the name of the student:")
        DOB = input("Enter the Date of Birth student:")
        #result = input("Enter the Result of the Student:")
        m = marks(Name,DOB)
        m.subject()
        m.Final()
        m.__str__()
        m.data_to_store_infile()
        m.databasecalling() #database calling
        option = input('Do You want to Know the subjects Marks[YES|NO]:')
        if option == 'yes':
            m.subjectsMarks()
        else:
            print("Choose the correct Option...!")
        print('Thank You')
        print('Govt of Andhra Pradesh...!')
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("INDIA")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        option2 = input('Do you want to continue or exit..')
        if option2 == "yes":
            continue
        else:
            break
