#LEVEL1

#1
import string
import random

def random_user_id():
    return_str = ""
    str = ""
    str += string.ascii_letters
    str += string.digits
    str_len = len(str)

    for e in range(6):
        return_str += str[random.randint(0,str_len-1)]
    return return_str

random.randrange
print(random_user_id())
print(random_user_id())
#random.randint(a, b) ve random.randrange(start, stop, step)


#2

def user_id_gen_by_user():
    len_,id_num = int(input("Length per id: ")),int(input("How much ids do you want to create: "))
    str_ = ""
    str_ += string.ascii_letters
    str_ += string.digits
    str_len = len(str_)

    for e in range(id_num):
        print_str = ""
        for t in range(len_):
            print_str += str_[random.randint(0,str_len-1)]
        print(print_str)

user_id_gen_by_user()

#3

def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return("rgb({},{},{})".format(r,g,b))

print(rgb_color_gen())

#LEVEL2

#1
def list_of_hexa_colors():
    str_ = "abdef0123456789"
    len_srt = len(str_)
    ret = "#"
    for _ in range(6):
        ret += str_[random.randint(0,len_srt-1)]
    return ret

print(list_of_hexa_colors())

#2

def list_of_rgb_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return("rgb({},{},{})".format(r,g,b))

print(list_of_rgb_colors())

def generate_colors(type_,num):
    if(type_ == 'hexa'):
        ret_hexa = []
        for _ in range(num):
            str_ = "abdef0123456789"
            len_srt = len(str_)
            ret = "#"
            for _ in range(6):
                ret += str_[random.randint(0,len_srt-1)]
            ret_hexa.append(ret)
        print(ret_hexa) 
    elif(type_ == "rgb"):
        ret_rgb = []
        for _ in range(num):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            ret_rgb.append("rgb({},{},{})".format(r,g,b))
        print(ret_rgb)
    else:
        print("Wrong parameter")
generate_colors('hexa', 3) 
generate_colors('hexa', 1) 
generate_colors('rgb', 3)
generate_colors('rgb', 1) 
generate_colors('hex',5125) # wrong parameter

#LEVEL3

#1
def shuffle_list(l):
    ret_list = []
    while(len(l) != 0):
        c = random.choice(l)
        ret_list.append(c)
        l.remove(c)
    return ret_list

l_test= [1,2,3,4,5,6,7,8,9]
print(shuffle_list(l_test))


#2
def unique7():
    l = []
    while(len(l) != 7):
        r = random.randint(0,9)
        if r not in l:
            l.append(r)
    print(l)

unique7()