person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

for key,value in person.items():
    print(key,value)

#For Else
#If we want to execute some message when the loop ends, we use else.
for iterator in range(1, 12, 2):
    pass
    #...
else:
    print('The loop ended')