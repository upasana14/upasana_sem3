
# # q1...................................................
# def multiply(i):
#     return i*i*i
# x=map(multiply,(1,2,3,4,5,))
# print (list(x))


#q2.................................................
# i=(2,3,4,5,6,7,8,9)
# def num(i):
#     if i%2==0:
#         return i,(":even") 
#     else:
#         return i,("odd")

# res=map(num,i)
# print( list(res))

# q3................................................
# def lower_case(l):
#     return l.lower()
# tuple_ex=('This','IS','MAP','PRACTICE')
# t=map(lower_case,tuple_ex)
# print(tuple(t))


# q4..................................................
# import math


# def square_root(s):
#     return math.sqrt(s)
# value=map(square_root,(2,3,4,16,9,36,25))
# print(list(value))

# /////////////////////q5........................................................
# from typing import OrderedDict


# def duplicate(d):
#     return OrderedDict.fromkeys(d)
# a=('Hello world')
# res=map(duplicate,a)
# print(list(res))


# ///q6..................................................
# num=int(input("Enter the number to show its table:"))

# def multiply(i):
#     return num*i
# x=map(multiply,(1,2,3,4,5,6,7,8,9,10))
# print(list(x))
# print(tuple(num,"x",multiply,"=",x))


# q7........................................................

# from operator import add

# l=[1,2,3,4]
# l2=[5,6,7,8]
# final=list(map(add,l,l2))
# print (str(final))

# q8...............................................

# from pickletools import int4

# def float(f):
#     return int(f)
# int_l=list(map(float,(1.1,2.3,5.66,8.1,9,10,11.6)))
# print(list(int_l))

# q9...........................................................

# def reset(s):
#     return reversed(s)
# rev=list(map(reset,(1,2,3,4,5,6,7,8,9,10)))
# print(list(rev))
# -------------

set1=[1,2,3,4,5,6]
print(list(reversed(set1)))

# q10............................................................

dict={"upasana":1,"ami":2}
res=map(lambda i:(i[0]+"@gmail.com"),dict)
print(list(res))