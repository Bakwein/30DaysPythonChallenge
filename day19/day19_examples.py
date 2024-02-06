# Syntax
#open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
'''
"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

f = open('./day19/test.txt')
print(f) # <_io.TextIOWrapper name='./day19/test.txt' mode='r' encoding='cp1254'>
t = f.read()
print(type(t))
print(t)
f.close()

#first 10 character
f = open('./day19/test.txt')
txt = f.read(10)
print(txt)
'''
MERHAB
ASD
'''
f.close()

print("")

f = open('./day19/test.txt')
line = f.readline()
print(line) #MERHAB
f.close()

f = open('./day19/test.txt')
lines = f.readlines()
print(lines) #['MERHAB\n', 'ASDH\n', 'ASDHHA\n', 'SDB\n', 'ASDHHAASDH\n']
f.close()

f = open('./day19/test.txt')
lines = f.read().splitlines()
print(lines) #['MERHAB', 'ASDH', 'ASDHHA', 'SDB', 'ASDHHAASDH']
f.close();


#with ile kullandıldığında biz yazmadan kesini otomatikman kapatır
with open('./day19/test.txt') as f:
    lines = f.read().splitlines()
    print(lines)


#append
with open('./day19/test2.txt','a') as f:
    f.write("eeeeee") #dosya yoksa oluşturur -dosya sonuna eeee yazar

#write
with open('./day19/test3.txt','w') as f:
    f.write('This text will be written in a newly created file')
    #dosya yoksa oluşturur - doysa varsa ve içinde içerik varsa onu siler sadece write içindeki kısım dosyada olur



with open('./day19/test4.txt','a') as f:
    f.write("za")

#dosya silme
import os
os.remove('./day19/test4.txt')


#veya

with open('./day19/test5.txt','a') as f:
    f.write("za")

if os.path.exists('./day19/test5.txt'):
    os.remove('./day19/test5.txt')
else:
    print("The file does not exists")


