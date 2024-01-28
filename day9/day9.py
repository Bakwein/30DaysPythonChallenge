#LEVEL1

#1
age = int(input("Enter your age: "))
print("You are old enough to drive.") if age > 18 else print("You need {} more years to learn to drive".format(18-age))

#2

your_age = int(input("Enter your age: "))
my_age = 21
if(your_age > my_age):
    print("You are {} years older than me.".format(your_age-my_age))
elif(my_age > your_age):
    print("I am {} years older than you.".format(my_age-your_age))
else:
    print("We are the same age.")

#3

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: ")) 
if(num1 > num2):
    print("{} is greater than {}".format(num1,num2))
elif(num2 > num1):
    print("{} is greater than {}".format(num2,num1))
else:
    print("{} = {}".format(num1,num2))


#LEVEL2
#1
grade = int(input("Grade: "))
if(grade >= 90 and grade <= 100):
    print("A")
elif(grade >= 70 and grade <= 89):
    print("B")
elif(grade >= 60 and grade <= 69):
    print("C")
elif(grade >= 50 and grade <= 59):
    print("D")
elif(grade >= 0 and grade <= 49):
    print("F")
else:
    print("Input error!")

#2

season = input("Season : ")
if(season == 'September' or season == 'October' or season == 'November'):
    print("Autumn")
elif(season == 'December' or season == 'January' or season == 'February'):
    print("Winter")
elif(season == 'March' or season == 'April' or season == 'May'):
    print("Spring")
elif(season == 'June' or season == 'July' or season == 'August'):
    print("Summer")
else:
    print("Input error")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']

input_fr = input("Fruit : ")
if(input_fr in fruits):
    print("That fruit already exist in the list")
else:
    fruits.append(input_fr)
    print("new list -> ",fruits)

#LEVEL3
    
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#1
if("skills" in person):
    print(person.get("skills"))
else:
    print("skills not found")

#2
if("skills" in person):
    if("Python" in person.get("skills")):
        print("Python found!")
    else:
        print("Python does not found")
else:
    print("skills not found")

#3

if("skills" in person):
    if(len(person.get("skills")) == 2 and "JavaScript" in person.get("skills") and "React" in person.get("skills")):
        print("He is a front end developer")
    elif("Node" in person.get("skills") and "Python" in person.get("skills") and "MongoDB" in person.get("skills")):
        print('He is a backend developer')
    elif("React" in person.get("skills") and "Node" in person.get("skills") and "MongoDB" in person.get("skills")):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

#4
if(person.get("is_married") == True and person.get("country") == "Finland"):
    print("{} {} lives in {}. He is married.".format(person.get("first_name"),person.get("last_name"),person.get("country"))) 