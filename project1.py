# ROCK PAPER SCISSOR
import random
user_choice=int(input("Enter your choice 0 for Rock , 1 for paper , 2 for scissor"))
computer_choice=random.randint(0,2)

print("Computer Choice-")
print(computer_choice)
if user_choice >2:
    print("invalid input") 

if user_choice == computer_choice:
    print("it's a draw")
if user_choice > computer_choice:
    print("you lose")
    
if user_choice < computer_choice:
    print("you win")
  
if computer_choice > user_choice:
    print("you win")

if user_choice == 0 and computer_choice == 2:
    print('you win')

if user_choice == 2 and computer_choice == 0:
    print("you lose")
  
      
