age = 21
height = 1.87
comp = 1 + 2j

base =   int(input("Enter base: "))
height = int(input("Enter height: "))
print("The are of the triangle is",(1/2)*base*height)

a = int(input("Enter side a:"))
b = int(input("Enter side b:"))
c = int(input("Enter side c:"))
print("The perimeter of the triangle is", a+b+c)

#rectangle
length = int(input("Enter length: "))
width = int(input("Enter width: "))
print("rect area",length*width)
print("rect perimeter",2*(length+width))

#circle
import math
radius = int(input("Enter radius: "))
print("circle area:", math.pi * (radius**2))
print("circle circum:",2*math.pi*radius)

#y = 2x-2
first_choice =  int(input("Enter first x:"))
second_choice = int(input("Enter second x:"))

first_y = 2 * first_choice - 2
second_y = 2 * second_choice - 2

slope = (second_y-first_y)/(second_choice-first_choice)
print("slope:",slope)

euclidean = (((second_y-first_y)**2)+((second_choice-first_choice)**2) ** (1/2))
print("euclidean:",euclidean)

second_slope = (10-2)/(6-2)

compare = slope is second_slope
print("compare:",compare)

first_num = int(input("Enter first num: "))

#y = x^2 + 6x + 9
print("res: ",(first_num**2)+(6*first_num)+9)

sec_num = int(input("Enter second num: "))
print("res: ",(sec_num**2)+(6*sec_num)+9)

print("len('falsy') is len('dragon')",len('falsy') is len('dragon'))
print("is in python","is" in "python")
print("is in dragon","is" in "dragon")
print("on in python","on" in "python")
print("on in dragon","on" in "dragon")
print(""" "jargon" in "I hope this course is not full of jargon" ""","jargon" in "I hope this course is not full of jargon")

len_python = len("python")
print("len python:",len_python)
float_len = float(len_python)
print("float_len:",float_len)
string_len = str(len_python)
print("string len:",string_len)

num = int(input("enter num for num%2:"))
print("num%2 == 0 :",num%2 == 0)

print("7//3 == 2.7:",7//3 == 2.7)

print("'10' is 10",'10' is 10)

print("int(9.8) == 10",int(9.8) == 10)

hours = int(input("Enter hours:"))
rate_per_hour = int(input("Enter rate per hour:"))
print("Your weekly earning is",hours*rate_per_hour)

years = int(input("Enter numbers of years have lived:"))
print("You gave lived for",years*31536000,"seconds")

num_ = int(input("Enter num for script:"))
print(num_,num_**0,num_**1,num_**2,num_**3)


