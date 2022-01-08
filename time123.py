import time
intial=time.time()
k=0
while(k<45):
    print(k)
    time.sleep(2)
    k=k+1
print(f"While loop ran in {time.time()-intial} Seconds")
intial2=time.time()
for i in range(45):
    print(i)
print(f"While loop ran in {time.time()-intial2} Seconds")

localtime=time.asctime(time.localtime(time.time()))
print(localtime)
