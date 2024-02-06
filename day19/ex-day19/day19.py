with open('./day19/ex-day19/obama_speech.txt') as f:
    
    readlines = f.readlines()
    #print(txt)
print("OBAMA")
print("line count-> {}".format(len(readlines)))

with open('./day19/ex-day19/obama_speech.txt') as f:
    txt = f.read()
print("word count-> {}".format(len(txt.split())))

'''
sayac = Counter(kelimeler)
l_temp = sayac.most_common(num)
'''

import re
from collections import Counter

sayac_obama = Counter(txt.split())
l_obama = sayac_obama.most_common(10)
print(l_obama)


with open('./day19/ex-day19/melina_trump_speech.txt') as f:
    
    readlines = f.readlines()
    #print(txt)
print("MELINA")
print("line count-> {}".format(len(readlines)))

with open('./day19/ex-day19/melina_trump_speech.txt') as f:
    txt = f.read()
print("word count-> {}".format(len(txt.split())))

sayac_melina = Counter(txt.split())
l_melina = sayac_melina.most_common(10)
print(l_melina)


with open('./day19/ex-day19/michelle_obama_speech.txt') as f:
    
    readlines = f.readlines()
    #print(txt)
print("MICHELLE OBAMA")
print("line count-> {}".format(len(readlines)))

with open('./day19/ex-day19/michelle_obama_speech.txt') as f:
    txt = f.read()
print("word count-> {}".format(len(txt.split())))

sayac_michelle = Counter(txt.split())
l_michelle = sayac_michelle.most_common(10)
print(l_michelle)

with open('./day19/ex-day19/donald_speech.txt') as f:
    
    readlines = f.readlines()
    #print(txt)
print("DONALD")
print("line count-> {}".format(len(readlines)))

with open('./day19/ex-day19/donald_speech.txt') as f:
    txt = f.read()
print("word count-> {}".format(len(txt.split())))

sayac_donald = Counter(txt.split())
l_donald = sayac_donald.most_common(10)
print(l_donald)

print("\n\n")

import json

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


email_list = list()
with open('./day19/ex-day19/email_exchanges_big.txt') as f:
    txt = f.read()
    words = txt.split()
    
for s in words:
    if "@" in s:
        email_list.append(s)

print(email_list)
print("\n\n")

def find_most_common_words(path,num):
    sayac2 = Counter(words)
    l_temp = sayac2.most_common(num)
    print(l_temp)

find_most_common_words('./day19/ex-day19/email_exchanges_big.txt', 10)


find_most_common_words('./day19/ex-day19/email_exchanges_big.txt', 5)






with open('./day19/ex-day19/romeo_and_juliet.txt') as f:
    txt = f.read()

print("\n")
sayac_rj = Counter(txt.split())
rj_list = sayac_rj.most_common(10)
print(rj_list)

import csv

with open('./day19/ex-day19/hacker_news.csv') as f:
    csv_reader = csv.reader(f,delimiter=',')
    line_count = 0
    pyt_counter = 0
    js_counter = 0
    just_java_counter = 0
    for row in csv_reader:
        if "python" in row[1] or "Python" in row[1]:
            pyt_counter +=1
        if "JavaScript" in row[1] or "javascript" in row[1] or "Javascript" in row[1]:
            js_counter +=1
        if "JavaScript" not in row[1] and "java" in row[1]:
            just_java_counter +=1
        

    print(pyt_counter)
    print(js_counter)
    print(just_java_counter)

stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def two_file_common_words(path1,path2):
    with open(path1) as f1:
        words = f1.read().split()
        sayac1 = Counter(words)
        l1 = sayac1.most_common(100)
        real_l1 = list()
        for a,b in l1:
            real_l1.append(a.lower())

    with open(path2) as f2:
        words2 = f2.read().split()
        sayac2 = Counter(words2)
        l2 = sayac2.most_common(100)
        real_l2 = list()
        for a,b in l2:
            real_l2.append(a.lower())

    common_list = list()
    for el in real_l1:
        if el in real_l2:
            common_list.append(el)

    print(common_list)
    return_list = list()
    for st in common_list:
        if st not in stop_words:
            return_list.append(st)
    print(return_list)
            
    



two_file_common_words('./day19/ex-day19/melina_trump_speech.txt','./day19/ex-day19/michelle_obama_speech.txt')










