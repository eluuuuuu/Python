import random  # Import the random module to allow the computer to make random choices

def get_computer_choice():
    """Randomly selects and returns rock, paper, or scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    """Asks the user to enter rock, paper, or scissors and validates the input."""
    while True:
        choice = input("Enter rock, paper, or scissors: ").strip().lower()  # Take input and normalize case
        if choice in ["rock", "paper", "scissors"]:
            return choice  # Return valid user choice
        print("Invalid choice. Please try again.")  # Prompt the user to enter a correct value

def determine_winner(user, computer):
    """Compares user and computer choices and determines the winner."""
    if user == computer:
        return "It's a tie!"  # If both choices are the same, it's a tie
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"  # Winning conditions for the user
    else:
        return "Computer wins!"  # If none of the above conditions are met, the computer wins

def play_game():
    """Main function to run the game in a loop until the user decides to quit."""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        # Get choices
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine and display the winner
        print(determine_winner(user_choice, computer_choice))

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break  # Exit the loop if the user doesn't want to continue

# Run the game
play_game()
