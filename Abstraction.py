from abc import ABC,abstractmethod
class Demo(ABC):
    @abstractmethod
    def disp(self):
        pass
    @abstractmethod
    def ch_name(self):
        pass
class School(Demo):
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
    def disp(self):
        print(f"Name:{self.name}")
        print(f"age:{self.age}")
        print(f"phone:{self.phone}")
    def ch_name(self):
        self.phone=int(input("Enter new phone number:"))
s1=School("vinay",20,875588996)
s1.ch_name()
s1.disp()