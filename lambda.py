# a=lambda i,j: i**2
# b=lambda i: i**3
# print(a(4),b(4))


# a=lambda i: i*-1 if i<0 else i
# print(a(int(input("Enter a -ve number:"))))


# a=lambda i: i.keys()
# print(a({"hello":"Sony","How":"are","You":"bye"}))


# a=lambda i: "Even" if  i%2==0 else "odd"
# print(a(int(input("Enter a num:"))))


# a=lambda i: i[0]
# print(a(eval(input("Enter any multivalue type data:"))))



# a=lambda i: len(i)
# print(a(eval(input("Enter any multivalue type data:"))))

#-----------------------------------MAP Fumnction----------------------------------
# a=lambda i: type(i)
# print(list(map(a,[12,8+7j,'hello'])))


# a= lambda i: i[0]
# print(list(map(a,["laptops",'mouse','keybord','house'])))


# a= lambda i: [len(i),i]
# print(list(map(a,["laptops",'mouse','keybord','house'])))


# a=[2,3,4,5,6]
# b=[3,4,5]
# c=lambda i,j:[i+j]
# print(list(map(c,a,b)))

# names=['a','b','c','d']
# age=[20,35,21,56]
# c=lambda i,j:[i,j]
# print(list(map(c,names,age)))


# d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}
# a=lambda i: d[i] if type(i) in [int,float,complex,bool] else type(i)
# print(list(map(a,d)))


# l=['happy',[2,3],27,9+7j]
# a=lambda i: type(i) in [ str,list,tuple,dict,set]
# print(list(filter(a,l)))


# l=[4,3,5,6,7,8,10]
# a=lambda i: i%2==0
# print(list(filter(a,l)))



# l=["sun flowers","banana tree","lilly flowers","lotus flower","marigold flowers"]
# a=lambda i: 'flowers' in i
# print(list(filter(a,l)))



# l=["hello","guys","please","respond","to","insta","computer"]
# a=lambda i: i[0] not in ['a','e','i','o','u']
# print(list(filter(a,l)))



# k=["apple","google","walmart","fb","insta","act","zomato"]
# a=lambda i: len(i)%2==0
# print(list(filter(a,k)))



# m=[-5,-6,9,-34,90,-28,78,100,89,45,-65]
# a=lambda i: i>0
# print(list(filter(a,m)))


# def sample(a,b):
#     yield(a+b)
#     yield(a-b)
#     yield(a*b)
#     print("Hello")
# print(list(sample(9,5)))

# def outer(func):   #  function name can be passed here
#     def inner(*args,**kwargs):
#         print("Addition is started.")
#         func(10,20)
#         print("Addition is completed.")
#     return inner
# @outer
# def sum(a,b):
#     print(a+b)
# sum(10,20)




# import time
# def timer(func):
#     def inner(*args,**kwargs):
#         st=time.time()
#         func(*args,**kwargs)
#         et=time.time()
#         total=et-st
#         print(f'Time taken during execution:{total}')
#     return inner
# @timer
# def add(a,b):
#     print(a+b)
#     time.sleep(2)
# add(12,15)
# def sub(a,b):
#     print(a-b)
# sub(10,5)


# import sys
# sys.setrecursionlimit(10000)
# import time
# def timer(func):
#     def inner(*args):
#         st=time.time()
#         result = func(*args)
#         et=time.time()
#         total=et-st
#         print(f'Time taken during execution:{total}')
#         return result
#     return inner
# @timer
# def extract(s,i=0,count=0):
#     if i==len(s):
#         return count
#     if s[i] in 'aeiouAEIOU':
#         count+=1
#     return extract(s,i+1,count)
# print(extract(input("Enter any string:")))

# def vowels(s):
#     count=0
#     for i in s:
#         if i in 'aeiouAEIOU':
#             count+=1
#      time.sleep(1)
#     print(count)
# vowels(input("Enter any string:"))





# a=[1,2,3,4]
