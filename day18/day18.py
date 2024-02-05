paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

import re
from collections import Counter

kelimeler = re.findall(r'\b\w+\b',paragraph)
print(kelimeler)
sayac = Counter(kelimeler)
print(sayac)


str_ = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."


regex1 = r'[- ]\d+'
nums = re.findall(regex1,str_)
print(nums)
nums_int = [lambda x:int(x)]

lst = list(map(lambda x:int(x),nums))
print(lst)
lst = sorted(lst)
print(lst)
print(lst[len(lst)-1] - lst[0])

def is_valid_variable(x):
    regex_ = r'[^A-Za-z _]+'
    matches = re.findall(regex_,x)
    if len(matches) > 0:
        return False
    return True

l = ['first_name','first-name','1first_name','firstname']

for e in l:
    print(is_valid_variable(e))

fltr = filter(is_valid_variable,l)
print(list(fltr))


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(x):
    return re.sub(r'[^A-Za-z ]', '', x)


print(clean_text(sentence))

def most_frequent_words(x):
    kelimeler = re.findall(r'\b\w+\b',x)
    s = Counter(kelimeler)
    return_l = list()
    for a,b in s.items():
        if b > 1:
            return_l.append([a,b])
    return return_l

print(most_frequent_words(clean_text(sentence)))
