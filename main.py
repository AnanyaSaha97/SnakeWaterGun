import random


def check(comp,user):
    if(comp == user):
        return 0
    elif(comp==0 and user == 1 ):
        return -1
    elif(comp==1 and user == 2):
        return -1
    elif(comp == 2 and user ==0):
        return -1
    return 1


comp = random.randint(0,2)
user = int(input("enter 0 for snake , 1 for water and 2 for gun :" ))

score = check(comp,user)

print("You:",user)
print("Computer:",comp)

if (score == 0):
    print("It's a DRAW")
elif (score == -1):
    print("You LOSS")
else:
    print("yOU WON")




