'''
1 for snake
-1 for water
0 for gun
'''

import random

computer = random.choice([1, 0, -1])

youstr = input("Enter your choice (s/w/g): ").lower()

youdict = {"s": 1,"w": -1,"g": 0}

reversedict = {1: "snake",-1: "water", 0: "gun"}

if youstr not in youdict:                                   # for user 
    print("Try again enter s, w, g ")

else:
    you = youdict[youstr]                                       

    print(f"You chose {reversedict[you]}")                       
    print(f"Computer chose {reversedict[computer]}")           

    if computer == you:
        print("It's a draw")

    else:
        if(computer - you) ==-1 or (computer-you)==2:
            print("you loose!")
        else:
            print("you win !")