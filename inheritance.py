#                single inheritance
# class resume:
#     def __init__(self,name,age,phone):
#         self.name=name
#         self.age=age
#         self.phone=phone
#     def disp(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Phone: {self.phone}")
# class Resume2(resume):
#     def __init__(self, name, age, phone, tenth,twelth):
#         super().__init__(name, age, phone)
#         self.tenth=tenth
#         self.twelth=twelth
#     def disp(self):
#         super().disp()
#         print(f"Tenth Marks: {self.tenth}")
#         print(f"Twelth Marks: {self.twelth}")
# me=Resume2('Vinay',18,8745962100,70,72)
# me.disp()


#                            Hierarchical Inheritance 
# class TestYantra:
#     ceo="abc"
#     manager="def"
#     location="Delhi"
# class Qspiders(TestYantra):
#     loc="Noida"
#     branchHead="ghi"
#     count_std=200
    

# class area:
#     shape=input("Enter the shape for area:")
#     if shape =="circle":
#         def circle(radius):
#                 arc=3.14*radius*radius
#                 return "Area of circle is:",arc
#         print(circle(radius=int(input("Enter the radius of circle:"))))  
#     elif shape == "rectangle":
#          def rectangle():




# class shape:
#     if shape == "circle":
#         arc=arc=3.14*radius*radius
#     elif shape == "rectangle":
#         arr=len*bredth

# class circle(shape):
#     def circle(radius):



#Hybrid inheritance 
# class grandfather:
#     location="abc"
#     properties=100
#     def show(self):
#         print(self.location)
    
# class father(grandfather):
#     name="def"
#     income=50000

# class mother(grandfather):
#     name="ghi"

# class child(father,mother):
#     name="jkl"
#     def show(self):
#         print(self.location)

# out=child
# out.show()



class resume:
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
    def disp(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")
class Resume2(resume):
    def __init__(self, name, age, phone, tenth,twelth):
        super().__init__(name, age, phone)
        self.tenth=tenth
        self.twelth=twelth
    def disp(self):
        super().disp()
        print(f"Tenth Marks: {self.tenth}")
        print(f"Twelth Marks: {self.twelth}")
class Resume3(Resume2):
    def __init__(self, name, age, phone,tenth,twelth,YOP,degree,cgpa):
        super().__init__(name, age, phone,)
        self.YOP=YOP
        self.degree=degree
        self.cgpa=cgpa
    def disp(self):
        super().disp()
        print(f"Year of passing: {self.YOP}")
        print(f"Degree: {self.degree}")
        print(f"CGPA: {self.cgpa}")
me=Resume3('vinay',20,8745963144,70,72,2025,'BCA',8)
me.disp()