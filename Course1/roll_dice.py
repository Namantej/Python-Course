import random
roll = random.randint(1,6)

guess = int(input("Guess the dice roll: 6"))

if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print(f"You gussed wrong. They rolled a {roll}")

