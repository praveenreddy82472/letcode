class Car:
    def __init__(self,name,model,engine,color,speed,abs,security):
        self.name =  name
        self.model = model
        self.engine = engine
        self.color= color
        self.speed = speed
        self.abs = abs
        self.security = security
    def show(self):
        print('Welcome the Reddy Industries LMT...')
        print("******** Reddy AutoMobile Industries ********")
        print("#"*40)
        print('Name of the car:',self.name)
        print('Model of the car:',self.model)
        print('Engine of the car:',self.engine)
        print('Color of the car:',self.color)
        print('Speed of the car:',self.speed)
        print('AbsYstem of the car:',self.abs)
        print('Security of the car:',self.security)
        print('Thank You!')
print('Welcome')
print('****** Reddy Industries PVT LMT...! *******')
print('----------->Be a part of Indian Environment')
print('Reddy Automobile Industries')
n1 = input('Enter the name of the car:')
n2 = input('Enter the name of the model:')
n3 = input('Enter the name of the Engine:')
n4 = input('Enter the name of the color:')
n5 = float(input('Enter the name of the speed:'))
n6 = input('You need Abs..Enter TRUE|FALSE:')
n7 = input('Enter the Level Of security[Basic|Intermediate|Advance]:')
print('Thank You')

c = Car(n1,n2,n3,n4,n5,n6,n7)
c.show()
