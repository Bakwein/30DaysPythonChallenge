#json to dict

import json

json_file = open('./day19/test.json','r',encoding="utf-8")
json_data = json_file.read()

person_dct = json.loads(json_data)

for k,v in person_dct.items():
    print(k,";")
    for k,v in v.items():
        print(k,v)


#dict to json
    
new_person = {
    "name": "sefa",
    "country": "tr",
    "city": "kocaeli",
    "skills": ["cpp", "c", "Python"]
}

person_dct["person2"] = new_person

updated_data = json.dumps(person_dct,indent=4)

with open('./day19/test.json', 'w') as f:
    f.write(updated_data)



#csv

import csv
with open('./day19/deneme.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

#excel
    
'''
import xlrd
excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)

'''


#xml

'''
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>


import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)

# output
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills


'''
