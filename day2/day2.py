#Day 2: 30 Days of python programming

first_name = "sefa"
last_name = "tunca"
full_name = "sefa tunca"
country = "Turkey"
city = "Kocaeli"
age = 21
year = 2024
is_married = False
is_true = True
is_light_on = False
name,nick = "sefa","bakwein"

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(name))
print(type(nick))

print(len(full_name))
print(len(first_name),len(last_name))


num_one, num_two = 5,4
print("num one =",num_one,"num two =",num_two)
total = num_one + num_two
print("total", total)
diff = num_one - num_two
print("diff",diff)
product = num_one * num_two
print("product",product)
division = num_one / num_two
print("division",division)
remainder = num_one % num_two
print("remainder",remainder)
exp = num_one ** num_two
print("exp",exp)
floor_division = num_one // num_two
print("floor_division",floor_division)

radius = 30

area = radius **2
print("area:",area)

import math
circum_of_circle = 2 * math.pi * radius 
print("circum_of_circle",circum_of_circle)


input_radius = int(input("Radius : "))

area2 = input_radius **2
print("area2:",area2)

import math
circum_of_circle2 = 2 * math.pi * input_radius 
print("circum_of_circle2",circum_of_circle2)


first_name = input("First name:")
last_name = input("Last name:")
country = input("Country:")
age = int(input("Age:"))

print("Fist name:",first_name)
print("Last name:",last_name)
print("Country:",country)
print("Age:",age)

help('keywords')