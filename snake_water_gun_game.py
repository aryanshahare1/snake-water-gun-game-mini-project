import random

'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Dictionary to convert user input into corresponding values
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Validate user input
if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    # By now we have 2 numbers (variables), you and computer
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("You win!")
    else:
        print("You lose!")
