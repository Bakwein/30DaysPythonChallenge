
import requests
from bs4 import BeautifulSoup
import json
import re

url = "http://www.bu.edu/president/boston-university-facts-stats/"

response = requests.get(url)
print(response)
print(response.status_code)
response_content = response.content
soup = BeautifulSoup(response_content, 'html.parser')
str_ = str(soup)
print(str_)
with open("./day22/soup_output.txt","w") as f:
    f.write(str_)
data = {}

data["title"] = soup.title.get_text()

data["facts-stats"] = {}
facts=[]
values=[]
# Get all h4 text
 # Get all h4 text
for key in soup.find('section', {'class' : 'facts-stats'}).find_all('h4'):
    facts.append(key.get_text())

for value in soup.find('section', {'class' : 'facts-stats'}).find_all('h2'):
    values.append(value.get_text())

data["facts-stats"] = dict(zip(facts,values))



print(data)

print("\n\n")

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

#print(soup)

table = soup.select("tbody td b a")
print(table,"\n\n")
def get_president_list(table):
    arr = []
    final = []
    for i in range(len(table)):
        if table[i].text == 'George Washington':
            arr = table[i:]
    for i in range(len(arr)):
        if arr[i].text == 'Joe Biden':
            arr = arr[:i+1]
            break
    for i in range(len(arr)):
        final.append(f"{i+1}.{arr[i].text}")
    return final

print(get_president_list(table))
