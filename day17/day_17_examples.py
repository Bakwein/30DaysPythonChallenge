'''
try:
    print(10 + '5')
except:
    print('Something went wrong')


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.') # age str oldugudan dolayı!
except:
    print('Something went wrong')


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born #type error!
    print(f'You are {name}. And your age is {age}.') 
except TypeError:
    print('Type error occured') #buna girer
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
'''

#exception olmayıp else blogu varsa else'e girer
#finally her zaman calisir
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)



