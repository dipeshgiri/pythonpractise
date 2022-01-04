nog=10
gn=97
print("Welcome to the guess game")
while(1):
    nog=nog-1
    if(nog==-1):
        print("Your Guess Has Been Finished Please Try Again")
        break
    else:
        print("Enter your Guess No: ")
        un=int(input())
        if(un<gn):
            print("Please Enter The Higher Number")
        elif(un>gn):
            print("Please Enter The Lower Number")
        elif(un==gn):
            print("You have Guessed Correctly and at Remaining Guess is",nog)
            break
        else:
            print("please enter correctly")
            continue

