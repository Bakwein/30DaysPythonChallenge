#old style with %

first_name = "sefa"
last_name = "tunca"
lang = "python"
formatted_str = "I am %s %s and i am learning %s" %(first_name,last_name,lang)
print(formatted_str)

import math
radius = 50
area = math.pi * (radius**2)
print("radius -> %d and area -> %.2f" %(radius,area)) # d yerine s de yazabilirim, sorun olmuyor.

python_libraries = ['Django', 'Flask', 'NumPy', 24, 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string)

#str.format
a,b=4,3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {1} is {0:.2f}.'.format(area, radius) # 2 digits after decimal
print(formated_string)

#f-strings
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f"{a} - {b} = {a - b}")
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
#bir tane eksik olsa bile hata verir tam karakter sayısı kadar değişken olmalı
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n


challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
#print(challenge.index(sub_string, 9)) # error

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
#print(challenge.rindex(sub_string, 9)) # error

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'