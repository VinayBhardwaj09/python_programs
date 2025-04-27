class school:
    sname='abc'#public member
    __sloc='noida'   #private member
    _phone=8744598555  #protected member
    def __init__(self,name,sloc,phone):
        self.name=name
        self.sloc=sloc
        self.phone=phone
    def disp(self):
        print(f"Name:{self.name}")
        print(f"loc:{self.sloc}")
        print(f"phone:{self.phone}")
s1=school("a","abc",7955542045)
print(s1._phone)
print(s1.__sloc)



