# q1...................................................
# from operator import truediv
# from pickle import TRUE

# from pickle import TRUE


# num=[1,-23,6,-8,-10,11,-5,2,5,10]
# def negative(num):
#     if num<0:
#         return TRUE
#     return False
# neg=filter(negative,num)
# print(list(neg))

# q2------------------------------------------------------
# from pickle import FALSE, TRUE


# def chk(num):
#     if num%2==0:
#         return False
#     else:
#         return num
# numbers=(1,2,3,4,5)
# res=filter(chk,numbers)
# print (list (res))


# /////////////// q3................................................................

# from pickle import TRUE

# letters=['a','b','e','i','d','o','j']
# def f_vowels(letter):
#     vowels=['a','e','i','o','u']
#     return True if letter in vowels else False
    
# f_vowels=filter(f_vowels,letters)
# print(tuple(f_vowels))

# q4..........................................................


# from operator import truediv
# from pickle import TRUE

# num=[1,-23,6,-8,-10,11,-5,2,5,10]
# def positive(num):
#     if num>0:
#         return TRUE
#     return False
# pos=filter(positive,num)
# print(list(pos))

# q5...........................................................

from pickle import FALSE, TRUE
from operator import truediv

no=[-1,-2,-5,9,-3]
def con(no):
    if no < 0:
        return abs(no)
    else :
        return FALSE
res=filter(con,no)
print(list(res))

# print(abs(-23))

# ----------------


