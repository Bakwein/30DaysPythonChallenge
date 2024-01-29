#LIST COMPREHENSION
#One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list 
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

print()
numbers = [i for i in range(0,11)]
print(numbers)

squares = [i * i for i in range(0,11)]
print(squares)

num2 = [(i,i*i) for i in range(0,10)]
print(num2)

even = [i for i in range(0,10) if i%2 == 0]
print(even)

odd = [i for i in range(11) if i % 2]
print(odd)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
edited_numbers = [i for i in numbers if i >0]
print(edited_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
one_dimensional = [i for num in list_of_lists for i in num]

#LAMBDA
#Lambda işlevi, adı olmayan küçük, anonim bir işlevdir. Herhangi bir sayıda argüman alabilir ancak yalnızca bir ifadeye sahip olabilir. Lambda işlevi, JavaScript'teki anonim işlevlere benzer. Başka bir fonksiyonun içine anonim bir fonksiyon yazmak istediğimizde buna ihtiyacımız var.

x = lambda param1,param2,param3:param1+param2+param3
print(x(2,3,4))

add_two_num = lambda x,y : x+y
print(add_two_num(3,2))

# Self invoking lambda function
print((lambda a, b: a + b)(2,3))

square = lambda x:x**2
print(square(6))

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22

#Lambda Function Inside Another Function

def power(x):
    return lambda n: x ** n

cube = power(2)(3)  # function power now need 2 arguments to run, in separate rounded brackets
print(cube)


