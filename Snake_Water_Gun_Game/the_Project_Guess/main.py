# the perfect guess 


import random
n = random.randint(1, 100)
guess = 0
a  = -1
while(a != n):
    guess += 1
    a = int(input("Enter your guess between 1 to 100: "))
    if(a < n):
        print("Too low")
    elif(a > n):
        print("Too high")


print(f"Congratulations You guessed the number {n} in {guess} attempts")