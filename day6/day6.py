#1

t = tuple()
t1 = ("Ali","Veli")
t2 = ("Ayşe","Fatma")
siblings = t1 + t2
print(t1,t2,siblings,sep="\n")

print(len(siblings))
father_mother = ("Hayriye","Kerem")
family = siblings + father_mother
print(family,len(family))

#2

sib1 = family[:-2]
fm = family[-2:]

print(sib1)
print(fm)

fruit = ("apple","pear","cherry","melon","kiwi","lemon")
vegetable = ("mint","chili","eggplant","spinach","carrot")
animals = ("leon","tiger","crocodile","horse","bear")

food_stuff_tp = fruit + vegetable + animals
print(food_stuff_tp)

fst_lst = list(food_stuff_tp)
print(fst_lst)

f1 = food_stuff_tp[:len(food_stuff_tp)]
f2 = food_stuff_tp[len(food_stuff_tp):]
print(f1,f2)

f3 = food_stuff_tp[:3]
f4 = food_stuff_tp[3:]
print(f3,f4)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
