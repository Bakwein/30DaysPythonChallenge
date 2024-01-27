fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4] #banana
second_fruit = fruits[-3] #orange
last_fruit = fruits[-1] #lemon
print(first_fruit,second_fruit,last_fruit)

print()

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # ('banana', 'orange', 'mango', 'lemon')
print(all_fruits)
orange_mango = fruits[-3:-1]  # ('orange', 'mango')
print(orange_mango)
orange_to_the_rest = fruits[-3:] #('orange', 'mango', 'lemon')
print(orange_to_the_rest)