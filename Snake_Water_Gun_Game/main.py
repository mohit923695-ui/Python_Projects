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
    you = youdict[youstr]                                        #this line taken by chatgpt

    print(f"You chose {reversedict[you]}")                       #this line taken by chatgpt
    print(f"Computer chose {reversedict[computer]}")           #this line taken by chatgpt

    if computer == you:
        print("It's a draw")

    else:
        if computer == -1 and you == 1:
            print("You win!")

        elif computer == -1 and you == 0:
            print("You lose")

        elif computer == 1 and you == -1:
            print("You lose")

        elif computer == 1 and you == 0:
            print("You win")

        elif computer == 0 and you == -1:
            print("You win")

        elif computer == 0 and you == 1:
            print("You lose")

        else:
            print("Try Again")