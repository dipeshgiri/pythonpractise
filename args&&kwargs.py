#def function_name_print(a,b,c,d):
 #   print(a,b,c,d)

#function_name_print("Dipesh","laravel","hamad","skillf")

def fun_args(normal,*args,**kwargs):
    print(normal)
    for items in args:
        print(items)
    print("Some value of dictionary is")

    for key,value in kwargs.items():
        print(f"The {key} is {value}")
    
har=["Dipesh","Ram","hari","Rohan","Python","Laravel","Django","PHP"]
nor="I am normal argument"
dict={"Dipesh":"Engineer","Ram":"CA","Hari":"Banker","Roshan":"Programmer"}
fun_args(nor,*har,**dict)
