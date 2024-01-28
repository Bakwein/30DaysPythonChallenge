#LEVEL 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1
print(len(it_companies))
print(it_companies)
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(["Comp1","Comp2","Comp3"])
print(it_companies)
#4
rmv = it_companies.pop()
print(it_companies)

#5
it_companies.remove('Twitter')
print(it_companies)
it_companies.discard('Comp1')
print(it_companies)
print(rmv)

#LEVEL2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1
A.update(B)
print(A)

new = A.union(B)
print(new)

#2
A1 = {19, 22, 24, 20, 25, 26}
B1 = {19, 22, 20, 25, 26, 24, 28, 27}

new = A1.intersection(B1)
print(new)

#3
A1 = {19, 22, 24, 20, 25, 26}
B1 = {19, 22, 20, 25, 26, 24, 28, 27}
print("issubset -> ",A1.issubset(B1))

#4
print("isdisjoint ->",A1.isdisjoint(B1))

#5
new2 = A1.union(B1)
new3 = B1.union(A1)

print(new2)
print(new3)

#6
print("symmetric difference",A1.symmetric_difference(B1))

#7 
del A1
del A
del B1
del B

#LEVEL 3

age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
set_age = set(age)
print(set_age)
print("length compare",len(age),"-",len(set_age),"->", len(age) is len(set_age))

#3
str_ = "I am a teacher and I love to inspire and teach people"
str_to_set = set(str_.split())
print(str_to_set)
print(len(str_to_set))



