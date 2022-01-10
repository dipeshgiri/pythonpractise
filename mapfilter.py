number=["1","2","3","4","5"]
number=list(map(int,number))
print(number[2]+5)

def sq(a):
    return a*a
def cu(a):
    return a*a*a

num=[2,5,6,8,2,3,9,10,12]
square=list(map(sq,num))
print(square)

func=[sq,cu]
for i in range(10):
    val=list(map(lambda x:x(i),func))
    print(val)

def func_greater(num):
    return num>5

grth5=list(filter(func_greater,num))
print(grth5)

from functools import reduce
r=reduce(lambda x,y:x*y,num)
print(r)
