import random

while True:
    user_action = input("Enter a choice (R(rock), P(paper), S(scissors)): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    
    print(f"\nPlayer ({user_action}) : CPU ({computer_action}).\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("ERROR (That's not a valid choice, try again).")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break