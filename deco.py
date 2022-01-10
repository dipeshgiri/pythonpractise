def dec1(func1):
    def nowexec():
        print("Now Executing")
        func1()
        print("Executed")
    return nowexec

@dec1
def heelo():
    print("Hello Dipesh")

@dec1
def hi():
    print("hi")
heelo()
hi()
