l=10
def fun(n):
    m=8
    global l
    l=l+10
    print(l,m,n)

print(l)
fun(5)
print(l)