import random  # Pick a random word

def choose_word():
    words = ["python", "hangman", "developer", "programming", "challenge", "keyboard"]  # List of words
    return random.choice(words)  # Choose one word from the list

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)  # Show guessed letters, hide others

def hangman():
    word = choose_word()  # Pick a secret word
    guessed_letters = set()  # Keep track of guessed letters
    attempts = 6  # Number of tries
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))  # Show the word with blanks
        guess = input("Guess a letter: ").lower()  # Get a letter from the player
        
        if guess in guessed_letters:  # If letter was already guessed
            print("You already guessed that letter!")
            continue  # Skip to next round
        
        guessed_letters.add(guess)  # Save the guessed letter
        
        if guess in word:  # If the letter is in the word
            print("Good guess!")
        else:
            attempts -= 1  # Lose a try
            print(f"Wrong guess! You have {attempts} attempts left.")
        
        if all(letter in guessed_letters for letter in word):  # If all letters are guessed
            print("\nCongratulations! You guessed the word:", word)
            break  # End game
    else:
        print("\nGame over! The word was:", word)  # Show the word if player loses

if __name__ == "__main__":  # Start the game when running the script
    hangman()
