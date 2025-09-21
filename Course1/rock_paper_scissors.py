import random
computer_choice = random.choice(["scissors","paper","rock"])
user_choice = input("Rock, Paper or Scissors? ")
if computer_choice == user_choice:
     print("TIE")
elif user_choice == "rock" and computer_choice == 'scissors':
    print("WIN")
elif user_choice == "paper" and computer_choice == 'rock':
    print("WIN")
elif user_choice == "scissors" and computer_choice == 'paper':
    print("WIN") 
else:
    print("You Lost. Computer has won") 