def getdate():
    import datetime
    return datetime.datetime.now()
def appendfooddata(x):
    date=str(getdate())
    print("Enter The Food Name :")
    food=input()
    x.write("["+date+"]"+food+"\n")

def appendexercisedata(x):
    date=str(getdate())
    print("Enter The Exercise Name :")
    exercise=input()
    x.write("["+date+"]"+exercise+"\n")

def searchfooddata(x):
    print(x.read())

def searchexerdata(x):
    print(x.read())


print("............Welcome to Fitness and Food Time Table Record and Display System..........")
print("Do you want to log the record or retireve record: ")
print("1. Log Record")
print("2. Retrive Record")
choice1=int(input())
if(choice1==1):
    print("Whose Record You want to Lock:Press 1,2,3")
    print("1. Hari")
    print("2. Ram")
    print("3. Aastha")
    choice2=int(input())
    if(choice2==1):
        print("What Do you Want to Log Food or Exercise ? :")
        print("1.Food")
        print("2.Exercise")
        choice3=int(input())
        if(choice3==1):
            file=open("harifood.txt","a")
            appendfooddata(file)
            file.close()
        elif(choice3==2):
            file=open("hariexe.txt","a")
            appendexercisedata(file)
            file.close()
        else:
            print("Please Enter Correct Data")
    elif(choice2==2):
        print("What Do you Want to Log Food or Exercise ? :")
        print("1.Food")
        print("2.Exercise")
        choice3=int(input())
        if(choice3==1):
            file=open("ramfood.txt","a")
            appendfooddata(file)
            file.close()
        elif(choice3==2):
            file=open("ramexe.txt","a")
            appendexercisedata(file)
            file.close()
        else:
            print("Please Enter Correct Data")
    elif(choice2==3):
        print("What Do you Want to Log Food or Exercise ? :")
        print("1.Food")
        print("2.Exercise")
        choice3=int(input())
        if(choice3==1):
            file=open("aasthafood.txt","a")
            appendfooddata(file)
            file.close()
        elif(choice3==2):
            file=open("aasthaexe.txt","a")
            appendexercisedata(file)
            file.close()
        else:
            print("Please Enter Correct Data")
elif(choice1==2):
    print("Whose Record You want to Retireve:Press 1,2,3")
    print("1. Hari")
    print("2. Ram")
    print("3. Aastha")
    choice4=int(input())
    if(choice4==1):
        print("What Do you Want to Retrieve Food or Exercise ? :")
        print("1.Food")
        print("2.Exercise")
        choice5=int(input())
        if(choice5==1):
            file=open("harifood.txt","r")
            searchfooddata(file)
            file.close()
        elif(choice5==2):
            file=open("hariexe.txt","r")
            searchexerdata(file)
            file.close()
        else:
            print("Please Enter Data Correctly")
    elif(choice4==2):
        print("What Do you Want to Retrieve Food or Exercise ? :")
        print("1.Food")
        print("2.Exercise")
        choice5=int(input())
        if(choice5==1):
            file=open("ramfood.txt","r")
            searchfooddata(file)
            file.close()
        elif(choice5==2):
            file=open("ramexe.txt","r")
            searchexerdata(file)
            file.close()
        else:
            print("Please Enter Data Correctly")
    elif(choice4==3):
        print("What Do you Want to Retrieve Food or Exercise ? :")
        print("1.Food")
        print("2.Exercise")
        choice5=int(input())
        if(choice5==1):
            file=open("aasthafood.txt","r")
            searchfooddata(file)
            file.close()
        elif(choice5==2):
            file=open("aasthaexe.txt","r")
            searchexerdata(file)
            file.close()
        else:
            print("Please Enter Data Correctly")     

    


