import random

def get_random_word():
    """
    Get a random word and its hint from a predefined list.
    
    Returns:
        tuple: A tuple containing a randomly selected word and its hint.
    """
    words_with_hints = [
        ('python', 'A popular programming language.'),
        ('hangman', 'A classic word-guessing game.'),
        ('challenge', 'Something that tests your abilities.'),
        ('programming', 'The process of writing computer code.'),
        ('openai', 'The organization that developed this model.'),
        ('algorithm', 'A step-by-step procedure for solving a problem.'),
        ('variable', 'A storage location identified by a memory address.'),
        ('function', 'A block of code that performs a specific task.'),
        ('debugging', 'The process of identifying and removing errors.'),
        ('syntax', 'The set of rules that defines the combinations of symbols.'),
        ('compiler', 'A program that translates code from high-level to machine language.'),
        ('loop', 'A sequence of instructions that is continually repeated.'),
        ('conditional', 'Statements that only run when a certain condition is true.'),
        ('recursion', 'When a function calls itself.'),
        ('array', 'A collection of items stored at contiguous memory locations.')
    ]
    return random.choice(words_with_hints)

def display_word(word, guessed_letters):
    """
    Display the current state of the word with guessed letters.
    
    Args:
        word (str): The word to be guessed.
        guessed_letters (set): The set of letters that have been guessed correctly.
    
    Returns:
        str: The current state of the word with guessed letters and underscores for unguessed letters.
    """
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def provide_hint(hint):
    """
    Provide a hint for the word.
    
    Args:
        hint (str): The hint associated with the word.
    
    Returns:
        str: The hint for the word.
    """
    return hint

def get_valid_guess(guessed_letters):
    """
    Prompt the user for a valid letter guess.
    
    Args:
        guessed_letters (set): The set of letters that have been guessed correctly.
    
    Returns:
        str: A valid letter guess from the user.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please guess a single letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess

def play_game():
    """
    Main function to play the Hangman game.
    """
    word, hint = get_random_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0 and set(word) != guessed_letters:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")

        guess = get_valid_guess(guessed_letters)

        if guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            attempts -= 1
            print(f"Incorrect! Here's a hint: {provide_hint(hint)}")

    if set(word) == guessed_letters:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    play_game()