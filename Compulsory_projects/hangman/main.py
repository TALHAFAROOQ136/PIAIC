import random

# List of words to choose from
word_list = ["python", "hangman", "programming", "developer", "code", "computer", "artificial", "intelligence"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)

# Function to play the Hangman game
def play():
    # Choose a word randomly
    word = choose_word()
    word_length = len(word)
    
    # List to store guessed letters
    guessed_letters = ['_'] * word_length
    
    # Number of incorrect guesses allowed
    incorrect_guesses_left = 6
    
    # List to store already guessed letters
    guessed = []
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses_left > 0:
        # Show current state of the word
        print(f"\nCurrent Word: {' '.join(guessed_letters)}")
        print(f"You have {incorrect_guesses_left} incorrect guesses left.")
        
        # Ask the player for their guess
        guess = input("Enter a letter: ").lower()
        
        # If the letter has already been guessed
        if guess in guessed:
            print("You've already guessed that letter!")
            continue
        
        # Add the guessed letter to the guessed list
        guessed.append(guess)
        
        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            
            # Update guessed letters list
            for i in range(word_length):
                if word[i] == guess:
                    guessed_letters[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses_left -= 1
        
        # Check if the word is fully guessed
        if "_" not in guessed_letters:
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

# Run the game
play()
