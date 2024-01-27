#1
l = ['Thirty','Days','Of','Python']
str_ = " ".join(l)
print(str_)

#2-3-4
l = ['Coding','For','All']
company = " ".join(l)
print(str_)

#5
print("string -> {} and string length -> {}" .format(company,len(company)))

#6
print("company upper",company.upper())
#7
print("company lower",company.lower())

#8
print("capitalize",company.capitalize())
print("title",company.title())
print("swapcase",company.swapcase())

#9
print("first word ->",company[:6])
print()
#10
print(company)
print(company.index("Coding"))
print(company.find("Coding"))

#11
print(company.replace("Coding","Python"))
company = company.replace("Coding","Python")

#12 
str1 =  "Python for Everyone"
str1.replace("Everyone","All")
print(str1)

print()
#13
print(str1.split())
for s in str1.split():
    print(s)

#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

#15
company = "Coding For All."
print(company[0])
#16
print(company[10])

#17
str_1 = ""
for s in 'Python For Everyone'.split():
    str_1 += s[0]
print(str_1)

#18-19
for s in 'Coding For All'.split():
    str_1 += s[0]
print(str_1)

#20-21
print("Coding For All".index("C"))
print("Coding For All".index("F"))

#22
print("Coding For All People".rfind("I"))

#23
print('You cannot end a sentence with because because because is a conjunction'.index("because"))
print('You cannot end a sentence with because because because is a conjunction'.find("because"))

#24
print('You cannot end a sentence with because because because is a conjunction'.rindex("because"))

#25-27
str_temp = "You cannot end a sentence with because because because is a conjunction"
print(str_temp[str_temp.index("because"):str_temp.rindex("because")+7])

#26
print('You cannot end a sentence with because because because is a conjunction'.find("because"))

#28
print("Coding For All".startswith("Coding"))

#29
print("Coding For All".endswith("coding"))

#30
print('   Coding For All      '.strip(" "))

#31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#32
l1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(l1))

#33
print("I am enjoying this challenge\nI just wonder what is next.")

#34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

#35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square".format(radius,area))

#36

a,b = 8,6

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")
