"""f=open("dipesh2.txt","a")
a=f.write("Dipesh Lives in Biratnagar.His Aim is to be a Developer\n")
print(a)
f.close()"""
# Handle read and write mode
f=open("dipesh2.txt","r+")
print(f.read())
f.write("thank you")
f.close()
