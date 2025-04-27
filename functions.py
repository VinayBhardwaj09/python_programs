# def mul(p,q):
#     return p*q
# print(mul(10,20))

# def sub():
#     a=int(input("Enter a:"))
#     b=int(input("Enter b:"))
#     print(a-b)
# sub()



#WAFunction to fetch only even num within the range of 1 to 50.
# def even():
#     for i in range(1,51):
#         if i%2==0:
#             print(i)
# even()

# def sub(a,b):
#     print(a-b)
# sub(int(input("Enter a:")),int(input("enter b:")))

# def out(name):
#     name='hello hi how are you'
#     new={}
#     s=name.split()
#     for i in s:
#         new[i]=(len(i),i[::-1])
#     print(new)
# out('hello hi how are you')



#1.waf to perform addition and substraction if "a" is greater than "b" return sum else return difference
# def out(a,b):
#     if a>b:
#         return(a-b)
#     else:
#         return(a+b)
# print(out(a=int(input("Enter a:")),b=int(input("Enter b:"))))


#2.waf to check string is palindrome or not (take user input)
# def check():
#     a=input("Enter string:")
#     if a[::-1]==a:
#         print("Palindrome")
#     else:
#         print("Not palindrome")
# check()

# def check(nan):
#     a=input("Enter string:")
#     if a[::-1]==a:
#         print("Palindrome")
#     else:
#         print("Not palindrome")
#     return nan
    
# print(check)


#3.wap to return length of mutable collection.
# def length(a):
#     if type(a) in ( set,list,  tuple ,dict) :
#         return(len(a))                                 # with argument and with return value
#     else:
#         return("Single value data type")
# print(length(a=eval(input("Enter values:"))))


# def length():
#     a=eval(input("Enter values:"))
#     if type(a) in ( set,list,  tuple ,dict) :           # without argument and without return value
#         print(len(a))
#     else:
#         print("Single value data type")
# length()


# def length(a):
#     if type(a) in ( set,list,  tuple ,dict) :
#         print(len(a))
#     else:                                                # with argument and without return value
#         print("Single value data type")
# length(a=eval(input("Enter values:")))


# def length():
#     a=eval(input("Enter values:"))
#     if type(a) in ( set,list,  tuple ,dict) :
#         return(len(a))
#     else:                                                # without argument and with return value
#         return("Single value data type")
# print(length())



#6.wap to squareing of the element in the given list
#l=[1,2,3,4,5]
