import random

def get_random_word():
    """
    Get a random word and its hint from a predefined list.
    
    Returns:
        tuple: A tuple containing a randomly selected word and its hint.
    """
    # Lista de palavras e dicas associadas
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
    # Escolhe aleatoriamente uma palavra e sua dica
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
    # Retorna a palavra com letras adivinhadas e underscores para letras não adivinhadas
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def provide_hint(hint):
    """
    Provide a hint for the word.
    
    Args:
        hint (str): The hint associated with the word.
    
    Returns:
        str: The hint for the word.
    """
    # Retorna a dica associada à palavra
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
        # Solicita uma letra ao jogador
        guess = input("Guess a letter: ").lower()
        # Verifica se a entrada é uma única letra alfabética
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please guess a single letter.")
        # Verifica se a letra já foi adivinhada
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess

def play_game():
    """
    Main function to play the Hangman game.
    """
    # Mensagem de boas-vindas e introdução do jogo
    print("Welcome to Hangman!")
    player_name = input("Please enter your name: ")
    print(f"\nHello, {player_name}! Let's play Hangman.")
    print("You need to guess the word, one letter at a time.")
    print("If you guess incorrectly, you'll get a hint about the word.\n")

    # Obtém uma palavra aleatória e sua dica
    word, hint = get_random_word()
    guessed_letters = set()  # Conjunto de letras adivinhadas corretamente
    attempts = 6  # Número de tentativas permitidas

    # Loop do jogo: continua até que o jogador esgote as tentativas ou adivinhe a palavra
    while attempts > 0 and set(word) != guessed_letters:
        # Mostra o estado atual da palavra e o número de tentativas restantes
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")

        # Obtém um palpite válido do jogador
        guess = get_valid_guess(guessed_letters)

        # Verifica se o palpite está correto
        if guess in word:
            guessed_letters.add(guess)  # Adiciona a letra correta ao conjunto
            print("Correct!")
        else:
            attempts -= 1  # Deduz uma tentativa para um palpite incorreto
            print(f"Incorrect! Here's a hint: {provide_hint(hint)}")

    # Verifica se o jogador adivinhou a palavra ou não
    if set(word) == guessed_letters:
        print(f"\nCongratulations, {player_name}! You guessed the word: {word}")
    else:
        print(f"\nGame over, {player_name}! The word was: {word}")

if __name__ == "__main__":
    play_game()  # Inicia o jogo se este script for executado diretamente
