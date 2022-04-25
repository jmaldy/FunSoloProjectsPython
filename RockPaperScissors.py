import random
while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    user_input = None

    while user_input not in choices:
        user_input = input("rock, paper, or scissors?: ").lower()
    
    if computer == user_input:
        print("computer: ", computer)
        print("user input: ", user_input)
        print('Draw, go again.')
        
   
    elif computer == "rock": 
        if user_input == "scissors":
            print("computer: ", computer)
            print("user input: ", user_input)
            print("you lost, better luck next time")
        if user_input == "paper":
            print("computer: ", computer)
            print("user input: ", user_input)
            print("You Win!")

    
    elif computer == "scissors":
        if user_input == "paper":
            print("computer: ", computer)
            print("user input: ", user_input)
            print("you lost, better luck next time")
        if user_input == "rock":
            print("computer: ", computer)
            print("user input: ", user_input)
            print("You Win!")
    
    
    elif computer == "paper": 
        if user_input == "rock":
            print("computer: ", computer)
            print("user input: ", user_input)
            print("you lost, better luck next time")
        if user_input == "scissors":
            print("computer: ", computer)
            print("user input: ", user_input)
            print("You Win!")

    play_again = input('Would you like to play again? (y/n): ').lower
    if play_again == "y":
              break
print("Thanks for playing!")
