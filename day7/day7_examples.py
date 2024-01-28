#Küme(set), sıralanmamış ve indekslenmemiş farklı öğelerden oluşan bir koleksiyondur
#Python'da küme benzersiz öğeleri depolamak için kullanılır ve kümeler arasında birleşim(union), kesişim(intersection), fark(difference), simetrik fark( symmetric difference), alt küme(subset), süper küme(super set) ve ayrık kümeyi(disjoint set) bulmak mümkündür.
#küme elemanlarına erişilirken döngüler kulanılır

st = set()
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

#eleman ekleme
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
#birden fazla eleman ekleme
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
#eleman silme - pop random bir eleman siler - remove(),discard()'da var. 
#Discard execption return etmez
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
#tüm elemanları silme
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
#kümeyi silme
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
#list to set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
#join in set
#A- union
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
#B- update
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

#kesişim(instersection) bulma
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

#subset-super set -issubset,issuperset - return true,false
# syntax
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

#fark- difference
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}

#simetrik fark - symetric dif -> (A\B) ∪ (B\A)
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}

#isdisjoint() - ayrık mı
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}