import random
import artno
print(artno.logo)
numbers=[]
for i in range(0,101):
    numbers.append(i)
n=int(random.choice(numbers))
print("The number is between 0 to 100.")
print("Which level do u want to play on? easy or hard?")
choice=input()
if choice=="easy":
    chance=10
    while chance!=0:
        print("Enter your guess:")      
        guess=int(input())
        if guess==n:
            print("Correct answer.")
            break
        elif guess>n:
            print("Too High")
            print("Guess again")
            chance-=1
            print(f"You have {chance} tries remaining.")
        elif guess<n:
            print("Too low")
            print("Guess again")
            chance-=1
            print(f"You have {chance} tries remaining.")
    if chance==0:
        print("You lost")
        print(f"No was:{n}")
    
elif choice=="hard":
      chance=5
      while chance!=0:
        print("Enter your guess:")      
        guess=int(input())
        if guess==n:
            print("Correct answer.")
            break
        elif guess>n:
            print("Too High")
        elif guess<n:
            print("Too low")  
      if chance==0:
          print("You lost.")
          print(f"Number was:{n}")                            
else: print("Invalid choice.")