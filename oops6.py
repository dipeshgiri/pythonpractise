class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am in Constructor of class A"
        self.classvar1="I am instance variable of class A"
        self.special="I am special variable"

class B(A):
    classvar1="I am class variable in class B"
    def __init__(self):
        self.var1="I am in constructor of class B"
        self.classvar1="I am the instance variable of class B"
        super().__init__()

a=A()
b=B()
print(a.classvar1)
print(b.classvar1)
print(b.special)