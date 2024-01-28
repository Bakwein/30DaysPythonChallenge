#1
dog = dict()

#2 
dog['name'] = "Karabas"
dog['color'] = "Black"
dog['Breed'] = "Terrier"
dog['Legs'] = 4
dog['Age'] = 21

#3

student = {
    "First Name" : "Ali",
    "Last Name" : "Demir",
    "Gender" : "Male",
    "Age" : 32,
    "Marital Status" : "Single",
    "Skills" : ["Python","C","C++","Java"],
    "Country" : "Turkey",
    "City" : "İstanbul",
    "Adress": {
        "Street" : "Demir St.",
        "zipcode" : 340021
    }
}
#4
print(len(student))

#5
print(student["Skills"])
print(type(student["Skills"]))

#6
student["Skills"].append("C#")
student["Skills"].append("HTML")
print(student["Skills"])

#7
print(student.keys())

#8
print(student.values())

#9
print(student.items())

#10 
del student["Skills"]
print(student)
student.pop("Adress")
print(student)
student.popitem()
print(student)

del student
#print(student) #ERROR

