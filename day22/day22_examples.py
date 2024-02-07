#web scrapping

import requests
from bs4 import BeautifulSoup

url = "https://pomofocus.io"

response = requests.get(url)
status = response.status_code
print(status)
content = response.content
#print(content)
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print("")
print(soup.get_text())