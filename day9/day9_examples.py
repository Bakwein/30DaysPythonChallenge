num = 9
print("num is greater than 3") if num > 3 else print("num is not greater than zero")

def statement1():
    print("St1")
    return True

def statement2():
    print("St2")
    return True

if(statement1() or statement2()): #st1 True ise st2'ye bakılmadan direkt blok icine girer
    print("hm")

