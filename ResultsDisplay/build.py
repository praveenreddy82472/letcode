from filehandling import *
from db import *
from db1 import *
class marks:

    def __init__(self,name,DOB):
        self.name = name
        self.DOB = DOB
        #self.Result = Result
        #self.TotalMarks = TotalMarks
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
        result = f"Name:{self.name} \t DOB:{self.DOB} \t TotalMarks:{self.TotalMarks} \t Result:{self.Result}"
        return result

    def databasecalling(self):
        logging.info('database accessing')
        Studentdatabase(self.name, self.DOB, self.Result, self.TotalMarks)
        StudentdatabaseMarksWise(self.name, self.DOB, self.Result, self.TotalMarks,self.Telugu,self.Hindi,self.English,self.MatheMatics,self.Science,self.SocialStudies)


if __name__ == "__main__":

    while True:


        Name = input("Enter the name of the student:")
        DOB = input("Enter the Date of Birth student:")
        #result = input("Enter the Result of the Student:")
        m = marks(Name,DOB)
        m.subject()
        m.Final()
        m.__str__()
        file_path = 'example.txt'
        data_to_append = m.store()
        result = append_to_file(file_path, data_to_append) #filehandling
        print(result)
        m.databasecalling()  #database calling
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
