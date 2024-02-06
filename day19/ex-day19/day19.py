with open('./day19/ex-day19/obama_speech.txt') as f:
    
    readlines = f.readlines()
    #print(txt)
print("OBAMA")
print("line count-> {}".format(len(readlines)))

with open('./day19/ex-day19/obama_speech.txt') as f:
    txt = f.read()
print("word count-> {}".format(len(txt.split())))


with open('./day19/ex-day19/melina_trump_speech.txt') as f:
    
    readlines = f.readlines()
    #print(txt)
print("MELINA")
print("line count-> {}".format(len(readlines)))

with open('./day19/ex-day19/melina_trump_speech.txt') as f:
    txt = f.read()
print("word count-> {}".format(len(txt.split())))


with open('./day19/ex-day19/michelle_obama_speech.txt') as f:
    
    readlines = f.readlines()
    #print(txt)
print("MICHELLE OBAMA")
print("line count-> {}".format(len(readlines)))

with open('./day19/ex-day19/michelle_obama_speech.txt') as f:
    txt = f.read()
print("word count-> {}".format(len(txt.split())))

with open('./day19/ex-day19/donald_speech.txt') as f:
    
    readlines = f.readlines()
    #print(txt)
print("DONALD")
print("line count-> {}".format(len(readlines)))

with open('./day19/ex-day19/donald_speech.txt') as f:
    txt = f.read()
print("word count-> {}".format(len(txt.split())))

import json
import re
from collections import Counter

def most_spoken_languages(filename,num):
    json_file = open(filename,'r',encoding="utf-8")
    json_data = json_file.read()
    dct = json.loads(json_data)
    str_ = ""
    for e in dct:
        for k,v in e.items():
            if(k == "languages"):
                for s in v:
                    str_ += s + " "
    #print(str_)
    kelimeler = re.findall(r'\b\w+\b',str_)
    sayac = Counter(kelimeler)
    l_temp = sayac.most_common(num)
    print(l_temp)


most_spoken_languages("./day19/ex-day19/countries_data.json",10)

print()

most_spoken_languages("./day19/ex-day19/countries_data.json",3)



#siralanmis_liste = sorted(ornek_liste, key=lambda x: x['population'], reverse=True)

def most_populated_countries(filename,num):
    json_file = open(filename,'r',encoding="utf-8")
    json_data = json_file.read()
    dct = json.loads(json_data)
    siralanmis = sorted(dct, key=lambda x:x['population'],reverse=True)
    #print(siralanmis[:num])
    l = list()
    for s in range(num):
        l.append("country : {} , population : {}".format(siralanmis[s]["name"],siralanmis[s]["population"]))
    print(l)

print("\n")
most_populated_countries("./day19/ex-day19/countries_data.json",10)

print()

most_populated_countries("./day19/ex-day19/countries_data.json",3)



