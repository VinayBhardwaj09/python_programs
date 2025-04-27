# # create a class company, create 4 class members 4 object members and atleast 3 object methods 
# class company:
#     CEO = 'Ratan Tata'
#     cloc = 'Nodia'
#     cphone = 9876543210
#     def __init__(self, name, age, eid, dept):
#         self.name = name
#         self.age = age
#         self.eid = eid
#         self.dept = dept
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Eid: {self.eid}")
#         print(f"Dept: {self.dept}")
#     @classmethod
#     def disp_c(cls):
#         print(f"CEO: {cls.CEO}")
#         print(f"Location: {cls.cloc}")
#         print(f"Phone: {cls.cphone}")
# el=company("Vinay",21,9000,"Manager")
# el.display()
# print()
# company.disp_c()

# #Static method 
# class company:
#     CEO = 'Ratan Tata'
#     cloc = 'Nodia'
#     cphone = 9876543210
#     def __init__(self, name, age, eid, dept):
#         self.name = name
#         self.age = age
#         self.eid = eid
#         self.dept = dept
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Eid: {self.eid}")
#         print(f"Dept: {self.dept}")
#     @classmethod
#     def disp_c(cls):
#         print(f"CEO: {cls.CEO}")
#         print(f"Location: {cls.cloc}")
#         print(f"Phone: {cls.cphone}")
#         @staticmethod
#         def add(a,b):
#             print(a+b)
# el=company("Vinay",21,9000,"Manager")
# # el.display()
# # print()
# # company.disp_c()
# el.add(10,20)



# class car:
#     color="red"
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#     def start(self):
#         print(f"{self.name} is of {self.color} color")
# car1=car("Audi","Black")
# car2=car("BMW", "Red")
# car1.start()
# car2.start()


# zomato={1:80,2:50,3:45,4:119,5:80,6:159,7:60,8:80,9:40,10:20,11:20,12:20}
# swiggy={1:60,2:40,3:55,4:109,5:85,6:149,7:50,8:90,9:60,10:10,11:10,12:10}
# menu={1: "Cold Coffee",     2: "Burgur",
#       3: "Hot Coffee",      4:"Veg Corn Pizza",
#       5: "Chilli Potato",   6: "Paneer Pizza",
#       7: "Momos",           8: "Veg Paneer Roll",
#       9: "Cold Drink",     10: "Punjabi Tadka",
#      11: "Aloo Bhujia",    12: "Chips"}
# print('''                     MENU
#       1. Cold Coffee     2. Burgur
#       3. Hot Coffee      4. Veg Corn Pizza
#       5. Chilli Potato   6. Paneer Pizza
#       7. Momos           8. Veg Paneer Roll
#       9. Cold Drink     10. Punjabi Tadka
#      11. Aloo Bhujia    12. Chips
# ''')
# while True:
#     item=int(input("Select an item number from menu:"))
#     if 1<=item<=12:
#         print(f'''         ON Zomato                     On swiggy
#               {menu[item]} = {zomato[item]}           {menu[item]} = {swiggy[item]}     ''') 
#         while True:
            # def costSwiggy():
            #     print(f'''Dear {name}, We have noted your order as
            #     Item name = {menu[item]}  
            #     Item cost = {swiggy[item]}
            #     Quantity = {quan}
            #     Delivary charges = 50
            #     Total AMT = {swiggy[item]}*{quan}+50 = {quan*swiggy[item]+50}''')
            # def costZomato():
            #      print(f'''Dear {name}, We have noted your order as
            # Item name = {menu[item]}  
            # Item cost = {zomato[item]}
            # Delivary charges = 50
            # Total AMT = {zomato[item]}*{quan}+50 = {quan*zomato[item]+50}''')
            # quan=int(input(f"How many {menu[item]} you want to order:"))
            # order=(int(input("Press 1 for Zomato or 2 for Swiggy:")))
#             if order in [1,2]:
#               break
#             else:
#                  print("Invalid choice! Please select 1 for Zomato or 2 for Swiggy.")      
        # if order==1:
        #     print("You are on Zomato.")
        #     name=input("Enter your name:")
        #     num=input("Enter contact number:")
        #     address=input("Enter delivary address:")
        #     costZomato()
#         elif order==2:
            # print("You are on Swiggy.")
            # name=input("Enter your name:")
            # num=input("Enter contact number:")
            # address=input("Enter delivary address:")
#             costSwiggy()
#     else :
#         print("you select wrong item.")
#     break
# pay={1:"online",2:"cash on delivary"}
# payment=int(input('''Select a payment method
#               1.Online
#               2.Cash on delivary
#               '''))
# print(f'''Thank you 
#       Your payment method is {pay[payment]}
# please hang in
# We are there with your order in few moments ''')




class Menu:
    zomato={1:80,2:50,3:45,4:119,5:80,6:159,7:60,8:80,9:40,10:20,11:20,12:20}
    swiggy={1:60,2:40,3:55,4:109,5:85,6:149,7:50,8:90,9:60,10:10,11:10,12:10}
    menu={1: "Cold Coffee",     2: "Burgur",
      3: "Hot Coffee",      4:"Veg Corn Pizza",
      5: "Chilli Potato",   6: "Paneer Pizza",
      7: "Momos",           8: "Veg Paneer Roll",
      9: "Cold Drink",     10: "Punjabi Tadka",
     11: "Aloo Bhujia",    12: "Chips"}
    def display(self):
        print('''                     MENU
        1. Cold Coffee     2. Burgur
        3. Hot Coffee      4. Veg Corn Pizza
        5. Chilli Potato   6. Paneer Pizza
        7. Momos           8. Veg Paneer Roll
        9. Cold Drink     10. Punjabi Tadka
        11. Aloo Bhujia    12. Chips''')


class price(Menu):
    def input(self):
        item=int(input("Select a item:"))
        if 1<=item<=12:
            print(f'''         ON Zomato                     On swiggy
                {self.menu[item]} = {self.zomato[item]}           {self.menu[item]} = {self.swiggy[item]}     ''') 
        self.quan=int(input(f"How many {self.menu[item]} you want to order:"))
        order=int(input("Press 1 for zomato 2 for swiggy."))
        if order == 1:
            print("You are on Zomato.")
            self.name=input("Enter your name:")
            self.num=input("Enter contact number:")
            self.address=input("Enter delivary address:")
        
        elif order == 2:
            print("You are on Swiggy.")
            self.name=input("Enter your name:")
            self.num=input("Enter contact number:")
            self.address=input("Enter delivary address:")

class Order(price):
    def costSwiggy(self):
                print(f'''Dear {self.name}, We have noted your order as
                Item name = {self.menu[self.item]}  
                Item cost = {self.swiggy[self.item]}
                Quantity = {self.quan}
                Delivary charges = 50
                Total AMT = {self.swiggy[self.item]}*{self.quan}+50 = {self.quan*self.swiggy[self.item]+50}''')
    def costZomato(self):
                print(f'''Dear {self.name}, We have noted your order as
                Item name = {self.menu[self.item]}  
                Item cost = {self.zomato[self.item]}
                Delivary charges = 50
                Total AMT = {self.zomato[self.item]}*{self.quan}+50 = {self.quan*self.zomato[self.item]+50}''')
            

            
