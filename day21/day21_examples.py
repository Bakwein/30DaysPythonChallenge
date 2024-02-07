class Person:
    pass
print(Person) #<class '__main__.Person'>

p = Person()
print(p) #<__main__.Person object at 0x0000027EAAA6AEF0>

#construcotr
class Person:
    def __init__(self,name):
        self.name = name

p = Person("Sefa")
print(p.name) #Sefa
print(p) #<__main__.Person object at 0x0000020FF416BE80>

class Person:
    def __init__(self,firstname,lastname,age,country,city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} yo. he lives in {self.city}'

p1 = Person("sefa","tunca",21,"Tr","Kocaeli")
print(p1.firstname)
print(p1.lastname)
print(p1.age)
print(p1.country)
print(p1.city)
'''
sefa
tunca
21
Tr
Kocaeli
'''

print(p1.person_info()) #sefa tunca is 21 yo. he lives in Kocaeli



class Person:
    def __init__(self,firstname = "Sefa", lastname = "Tunca", age = 250, country = "Tr", city = "Kocaeli"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skils = []
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} yo. he lives in {self.city}'
    def add_skill(self,skill):
        self.skils.append(skill)
    
p2 = Person()
print(p2.person_info()) #Sefa Tunca is 250 yo. he lives in Kocaeli
p3 = Person("ali","yilmaz",55,"Tr","İstanbul")
print(p3.person_info()) #ali yilmaz is 55 yo. he lives in İstanbul

p3.add_skill("HTML")
p3.add_skill("CSS")
p3.add_skill("Python")
print(p3.skils) #['HTML', 'CSS', 'Python']

#INHERITANCE - KALITIM

class Student(Person):
    pass

s1 = Student("veli","yildirim",52,"Tr","İzmir")
print(s1.person_info()) #veli yildirim is 52 yo. he lives in İzmir


#Overriding parent method

class Student(Person):
    def __init__(self,firstname = "mehmet",lastname = "yilmaz", age = 33, country = "Tr", city = "Kocaeli", gender = "male"):
        self.gender = gender
        super().__init__(firstname,lastname,age,country,city)
    def person_info(self):
        gender = "He" if self.gender == "male" else "She"
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'


s5 = Student("Veli","Muş",35,"Tr","Çorum","male")
s6 = Student("Ayşe","Yıldırım",52,"tr","İstanbul","female")

print(s5.person_info()) #Veli Muş is 35 years old. He lives in Çorum, Tr.
print(s6.person_info()) #Ayşe Yıldırım is 52 years old. She lives in İstanbul, tr.


