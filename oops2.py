class employee:
    def __init__(self,aname,arole,acourse):
        self.name=aname
        self.role=arole
        self.course=acourse
    
    def printdetail(self):
        return f"Name is {self.name} and Role is {self.role} and Course is {self.course}"
    
harry=employee("Dipesh","Manager","Python")
ram=employee("Ram","Project","Php")
print(harry.printdetail())
print(ram.printdetail())
