"""class student:
    pass
hari=student()
ram=student()
hari.name="Hari"
hari.classs="5"
hari.roll="10"
ram.name="ram"
print(ram.name)
"""
class Employee:
    no_of_leaves=45
    pass
ram=Employee()
hari=Employee()
ram.name="Hari"
ram.classs="5"
print(ram.__dict__)
ram.no_of_leaves=10
print(ram.__dict__)
print(Employee.__dict__)
