#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

flt = [i for i in numbers if i <= 0]
print(flt)

#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

one_dim = [i for s in list_of_lists for t in s for i in t]
print(one_dim)

#3

ret = [(t,t**0,t**1,t**2,t**3,t**4,t**5) for t in range(11) ]
print(ret)

#4

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

ret2 = [[i[0].upper(),i[0][:3].upper(),i[1].upper()] for t in countries for i in t]
print(ret2)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

ret3 = [{"country":i[0].upper(),"city":i[1].upper()} for t in countries for i in t]
print(ret3)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

ret4 = ["{} {}".format(i[0],i[1]) for t in names for i in t ]
print(ret4)

#7

#a - slope
#ax+b
x = lambda a:a[:a.find("x")]
print(x("2x+3"))

#b - y kestiği yer
print((lambda a:a[a.find("x")+2:])("2x+3"))
