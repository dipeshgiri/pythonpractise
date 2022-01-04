a=9
b=5
c=sum((a,b))
print(c)

def name():
    print("you are in function name")

name()
#return type function
def average(a,b):
    """This is the function that will calculate the average of the two number"""
    average=(a+b)/2
    return average

v=average(2,5)
print(v)
print(average.__doc__)
print(sum.__doc__)