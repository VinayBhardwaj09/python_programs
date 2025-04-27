# # class addition:
# #     @staticmethod
# #     def add(a,b):
# #         print(a+b)
# #     a=add
# #     @staticmethod
# #     def add(a,b,c,d):
# #         print(a+b+c+d)
# # ob=addition()
# # ob.add(10,25,25,52)



# class company:
#     cname="ABC"
#     cloc="Delhi"
#     Cphone=123
#     CEO="XYZ"
#     def __init__(self,name,eid,dept):
#         self.name=name
#         self.eid=eid
#         self.dept=dept
#     def display(self):
#         print(f"Name:{self.name}")
#         print(f"EID:{self.eid}")
#         print(f"DEPT:{self.dept}")
#     f=display
#     @classmethod
#     def display(cls):
#         print(f"CNAME:{cls.cname}")
#         print(f"CLOC:{cls.cloc}")
#         print(f"CEO:{cls.CEO}")
# el=company("mno",9000,"HR")
# el.display()
# el.f()


# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
# ob1=A(5,5)
# print(ob1.a+ob1.b) 
# ob2=A(5,4)
# print(ob1+ob2) 


#------------------------------------Magic Method----------------------
# class A:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,other):
#         return self.a+other.a    
# ob1=A(50)
# ob2=A(33)
# print(ob1+ob2)


# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         return self.a+other.a,self.b+other.b
#     def __sub__(self,other):
#         return self.a-other.a,self.b-other.b
#     def __mul__(self,other):
#         return self.a*other.a ,self.b*other.b
# ob1=A(25,98)
# ob2=A(20,17)
# print(ob1+ob2)
# print(ob1-ob2)
# print(ob1*ob2)