#key:value -> item

# syntax
empty_dict = {}
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
print(len(person)) # 7

#Accessing Dictionary Items
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error -> böyle bir key yok
#error almamak için get kullanabiliriz. get eğer öyle bir key yoksa None döner
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

#eleman ekleme
person['job_title'] = 'Instructor'
person['skills'].append('HTML')

#elemean düzenleme - var olan bir key üzerine yeni değer üzerine yazılır
person['first_name'] = 'Eyob'
person['age'] = 252

#key var mi kontrol
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

#key ve value silme
#pop(key) -> o keyi ve value'yu siler
#popitem() -> son keyi ve value'yu siler
#del -> o keyi ve value'yu siler

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('first_name')        # Removes the firstname item
print(person) #{'last_name': 'Yetayeh', 'age': 250, 'country': 'Finland', 'is_married': True, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'address': {'street': 'Space street', 'zipcode': '02210'}}
person.popitem()# Removes the address item
print(person)  #{'last_name': 'Yetayeh', 'age': 250, 'country': 'Finland', 'is_married': True, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']}
del person['is_married']        # Removes the is_married item
print(person) #{'last_name': 'Yetayeh', 'age': 250, 'country': 'Finland', 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']}

#itemleri listeleme
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

#clear 
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

#del
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

#copy a dict
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

#keysleri listeye alma
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])

#valueleri listeye alma
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])