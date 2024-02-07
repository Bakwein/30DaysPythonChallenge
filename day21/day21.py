import statistics
from collections import Counter

class Statistics():
    def __init__(self,arr):
        self.arr = arr
    def count(self):
        return len(self.arr)
    def sum(self):
        return sum(self.arr)
    def min(self):
        return min(self.arr)
    def max(self):
        return max(self.arr)
    def range(self):
        return self.max() - self.min()
    def mean(self):
        return statistics.mean(self.arr)
    def median(self):
        return statistics.median(self.arr)
    def mode(self):
        return statistics.mode(self.arr)
    def std(self):
        return statistics.stdev(self.arr)
    def var(self):
        return statistics.variance(self.arr)
    def freq_dist(self):
        freq_dist = Counter(self.arr)
        print("Frequency Distribution:")
        for k,v in freq_dist.items():
            print(k,":",v)
    
    
    

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]


data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 29.76
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) #26
data.freq_dist()


class PersonAccount():
    def __init__(self,firstname,lastname,incomes,expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    
    def total_income(self):
        return sum(self.incomes.values())
    
    def total_expense(self):
        return sum(self.expenses.values())
    
    def add_income(self,k,v):
        self.incomes[k] = v

    def add_expense(self,k,v):
        self.expenses[k] = v

    def account_balance(self):
        return sum(self.incomes.values())-sum(self.expenses.values())
    
    def account_info(self):
        return f'{self.firstname} {self.lastname}.\nIncomes -> {self.incomes}.\nExpenses -> {self.expenses}.'
    
p = PersonAccount("sefa","tunca",{"Gelir1" : 24000, "Gelir2" : 1241241},{"Gider1" : 2000,"Gider2" : 24142})

print("\n\n")

print(p.account_balance())
print(p.account_info())
print()
p.add_income("Gelir3",124124124)
p.add_expense("Gider3",12412)
print(p.account_balance())
print(p.account_info())

    
