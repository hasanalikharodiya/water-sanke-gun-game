import random

i = ['s','w','g']

chance = 10
no_of_chance = 0
human_point = 0
computer_point = 0

print("Snake,Water and Gun Play the Game \n Made by @HasanAli Kharodiya")

while no_of_chance < chance:
    inp = input("Enter S = Snake , W = Water and G = Gun : ").lower()
    random_char = random.choice(i)

    if inp == random_char:
        print("Game - Tie Both Point is 0 \n")
    
    # Rule for 'S'
    
    if inp == "s" and random_char == "g":
        computer_point = computer_point + 1
        print(f"Computer Win one Point - Computer Guess is {random_char} \n")

    elif inp == "s" and random_char == "w":
        human_point = human_point + 1
        print(f"You Win one Point - Computer Guess is {random_char} \n")
    
    # Rule for 'W'
 
    elif inp == "w" and random_char == "s":
        computer_point = computer_point + 1
        print(f"Computer Win one Point - Computer Guess is {random_char} \n")
    
    elif inp == "w" and random_char == "g":
        human_point = human_point + 1
        print(f"You Win one Point - Computer Guess is {random_char} \n")
    
    # Rule for 'G'

    elif inp == "g" and random_char == "s":
        human_point = human_point + 1
        print(f"You Win one Point - Computer Guess is {random_char} \n")

    elif inp == "g" and random_char == "w":
        computer_point = computer_point + 1 
        print(f"Computer Win one Point - Computer Guess is {random_char} \n")
    
    else:
        print("Please Enter Correct Value \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance } is left out of {chance} \n")

print("Game is Over \n")

if computer_point < human_point:
    print("You Win the Game \n")
elif computer_point > human_point:
    print("Computer Win the Game \n")

print(f"Your Point is {human_point} and Computer Point is {computer_point}")