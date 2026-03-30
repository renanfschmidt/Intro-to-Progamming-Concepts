from dictonaries import students


class Vehicle:
    def __init__(self,brand,type,doorCount,model):
        self.brand = brand
        self.type = type
        self.doorCount = doorCount
        self.model = model

newCar=Vehicle("BMW","car",2,"M")
oldCar=Vehicle("BMW","car","3","M")
#print(newCar.brand)#
#print(oldCar.doorCount)#

class Person:
     def __init__(self,age,name,major):
         self.age = age
         self.name = name
         self.major = major
class Classroom:
     def __init__(self,course):
       self.People = []
       self.course = course
     def addPerson(self,Person):
         self.People.append(Person)
student=Person(2,"student")
student2=Person(3,"student2")
student3=Person(4,"student3")

IntroClass=Classroom('Intro to Programming Concepts')
IntroClass.add_Person(student)
IntroClass.add_Person(student2)
IntroClass.add_Person(student3)
for person in IntroClass.People:
    print(person.name)

