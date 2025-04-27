# def add():
#     a=12
#     b=20
#     print(a+b)
#     def sub():
#         nonlocal a,b
#         a=30
#         b=20
#         print(a-b)
#     sub()
# add()

# def mock(vinay="*",b=1,c="*"):
#     print(f"vinay={vinay}")
#     print(f"b={b}")
#     print(f"c={c}")
# mock("*","*")

# def value(a,b,c,d):
#     print(a,b,c,d)
# value(1,2,d=4,c=3)




#PACKING
# def demo(*a):
#     print(a)
#     print(type(a))
# demo(1,2,3,3.4,"hello")      

# def trip(**detail):
#     print(detail)
#     print(type(detail))
# trip(name='vinay',phone=875508585578, )


#UNPACKING
# def unpack(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# unpack(**{'a':1, 'b':2, 'c':3})



# def outt(*a):
#     for i in a :
#         if type(i)==str and len(i)%2==0:
#             print(i)
# outt(10,'hello','orange')