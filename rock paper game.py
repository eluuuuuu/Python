import random  # Import the random module to make the computer choose randomly

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]  # List of possible choices
    return random.choice(choices)  # Pick a random choice

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()  # Ask the user for their choice
    while choice not in ["rock", "paper", "scissors"]:  # Make sure the input is valid
        print("Invalid choice! Try again.")  
        choice = input("Choose rock, paper, or scissors: ").lower()  # Ask again
    return choice

def determine_winner(user, computer):
    print(f"\nYou chose: {user}")  
    print(f"Computer chose: {computer}\n")  

    if user == computer:  # If both choices are the same
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):  # Check winning conditions
        return "You win! 🎉"
    else:
        return "You lose! 😢"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")  
    user_choice = get_user_choice()  # Get user choice
    computer_choice = get_computer_choice()  # Get computer choice
    result = determine_winner(user_choice, computer_choice)  # Determine the winner
    print(result)  # Show the result

if __name__ == "__main__":  # Run the game if the script is executed
    play_game()
