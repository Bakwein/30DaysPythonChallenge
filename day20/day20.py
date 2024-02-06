import requests

url = 'https://www.gutenberg.org/cache/epub/72889/pg72889-images.html'

response = requests.get(url)
print(response)
txt = response.text
#print(txt)

from bs4 import BeautifulSoup

soup = BeautifulSoup(txt, 'html.parser')
ret_txt = soup.get_text()
#print(ret_txt)

words = ret_txt.split()

from collections import Counter

x = Counter(words)
most_20 = x.most_common(20)
l_1 = list()
for a,b in most_20:
    l_1.append(a)
ret_list = list()
for s in l_1:
    if s.isalpha():
        ret_list.append(s)
print(ret_list[:10])



url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
print(response)
print(response.status_code)
countries = response.json()

#
#siralanmis_liste = sorted(ornek_liste, key=lambda x: x['population'], reverse=True)

c = sorted(countries,key=lambda x:x['population'],reverse=True)

for s in range(10):
    print(c[s]['name'])
    print()

total_len = 0
all_l = list()
l_ = list()
for s in c:
    x = s.get('languages')
    if x  != None and x not in l_:
        l_.append(x)
    if x != None:
        all_l.append(x)

sef = list() 
for e in all_l:
    for k in e:
        sef.append(k)



s = Counter(sef)
ret = s.most_common(10)
print(ret)


print(len(l_))


cat_pi = requests.get('https://api.thecatapi.com/v1/breeds')
data = cat_pi.json()

import numpy

l = list()

for el in data:
    eleman = (int(el['weight']['metric'].split()[0]) + int(el['weight']['metric'].split()[-1]) )/2
    l.append(eleman)

median = numpy.median(l)
mean = numpy.mean(l)
min_metric = min(l)
max_metric = max(l)
sd = numpy.std(l)

print("CAT WEIGHT")
print(median)
print(mean)
print(min_metric)
print(max_metric)
print(sd)


'''def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def freq_origin(data):
    origins = []
    for breed in data:
        origins.append(breed['origin'])
    print(sort_dict_by_value(dict(Counter(origins)), True))'''


origins = []
for breed in data:
    origins.append(breed['origin'])
sort = sorted(origins,key = lambda x:x[1], reverse = True)

hm = Counter(sort)
print(hm)



