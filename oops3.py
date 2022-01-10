class employee:
    no_of_leaves=8
    games=9
    def __init__(self,aname,arole,acourse):
        self.name=aname
        self.role=arole
        self.course=acourse
    
    def printdetail(self):
        return f"Name is {self.name} and Role is {self.role} and Course is {self.course}"
    
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    
    # using classmethod as a constructor
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def print_from(string):
        print("This is Good "+ string)


#Single Level Inheritance
class programmer(employee):
    salary=9000
    def __init__(self,aname,arole,acourse,alanaguage):
        self.name=aname
        self.role=arole
        self.course=acourse
        self.language=alanaguage

    def progprint(self):
        return f"Name is {self.name} and Role is {self.role} and Course is {self.course} and langauages known is{self.language}"

class player():
    
    games=8
    def __init__(self,aname,agames):
        self.name=aname
        self.games=agames

    def printplayer(self):
        return f"Name is {self.name} and game is {self.games}"



#multiple inheritance
class empply(player,employee):
    pass

#harry=employee("Dipesh","Manager","Python")
#ram=employee("Ram","Project","Php")
#karan=employee.from_dash("Karan-DeputyManager-Laravel")
#rajan=programmer("Rajan","Coder","Laravel",["C","Cpp"])
dipesh=empply("Dipesh","[c,cpp]")
print(dipesh.printplayer())
print(dipesh.games)
#print(harry.printdetail())
#print(ram.printdetail())

#harry.change_leaves(34)
#print(harry.__dict__)
#employee.change_leaves(65)
#print(employee.__dict__)
#print(ram.no_of_leaves)
#print(karan.no_of_leaves)
#print(karan.__dict__)
#karan.print_from("Object")
#employee.print_from("Class")
#print(rajan.progprint())
#print(rajan.salary)