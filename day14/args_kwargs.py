#*args, **kwargs

def kuvvet_al(x,y): #positional arguments
	return x**y

#buna 2 parametre harici bir parametre sayılı işlem uygularsak hata alırız


def bilgi_ver(ad,soyad="girilmedi",yas="girilmedi"): #yas="girilmedi" -> keyword argument
	return "Ad: {} , Soyad: {} , Yas: {}".format(ad,soyad,yas)

print(bilgi_ver("Ali",34)) #dedigimizde 35'ü soyad olarak algılar çözüm;
print(bilgi_ver("Ali",yas=34))

#bir fonkisyona kaç tane parametre vereceğimzii bilmiyorsak ve bunu tüm parametre
#sayılarında kullanmak istiyorsak *args, **kwargs kullanırız

def topla2(x,y):
	return x+y

def topla3(x,y,z):
	return x+y+z

#!!!!
def topla(*args):
	print(args) # -> *args = (1,2,3,4), *args kullanımı ile istenildiği kadar parametre verilebilir
#args -> type(*args) -> tuple
topla(1,2,3,4)


def carp(*args):
	carpim = 1
	for arg in args:
		carpim *= arg
	return carpim

print(carp(2,3,5,10)) #600



def fonk(**kwargs): # istenilen kadar keyword parametresi girilebilir
	print(kwargs) # -> {"ad":"ali", "soyad":"demir", "yas":34} #kwargs -> dict

fonk(ad = "ali", soyad = "demir", yas = 34)



def fonk2(zorunlu,*args,**kwargs):
	print(zorunlu)
	print("**")
	for arg in args:
		print(arg)
	print("**")
	for k,v in kwargs.items():
		print(k,v)

fonk2(2,3,4,5,6,7,ad = "Ali", yas = 23)

'''
2
**
3
4
5
6
7
**
ad Ali
yas 23
'''