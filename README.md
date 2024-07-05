# CodeGuess Hangman

This Hangman game was developed to provide a fun and educational experience, helping players improve their word-guessing skills and expand their knowledge of programming terms.

This game allows users to guess programming-related words one letter at a time, with hints provided after incorrect guesses. The goal is to guess the word before running out of attempts.

The game is ideal for programming students, developers, and tech enthusiasts looking to test their knowledge in an engaging and interactive manner.

[You can access the live version of my project here.](https://codeguess-hangman-17434baed82d.herokuapp.com/)

<img width="1009" alt="Captura de ecrã 2024-07-02, às 20 00 48" src="https://github.com/elsei123/BattleshipGame/assets/164704332/7b27a2a3-026c-4c3f-af21-ec76cee7e4e3">


## Technologies Used
- __Python:__ Primary language used to develop the game, chosen for its simplicity and versatility.

- __Heroku:__ Platform used to deploy the game, making it easily accessible and executable online.

- __Code Institute's Simulated Terminal:__ Environment where the game runs, providing a realistic and interactive terminal experience.

## How to Play

### Step-by-Step Guide
 
- __Enter Your Name:__ When prompted, enter your name. This personalizes the game experience, making it more engaging.

  <img width="368" alt="Captura de ecrã 2024-07-02, às 20 01 38" src="https://github.com/elsei123/BattleshipGame/assets/164704332/e11ed38b-bd93-4592-84ce-9ac9db67ebb5">


- __Guess the Word:__ You will see a series of underscores representing the letters of the word to be guessed. Enter a letter to try to guess it.

  <img width="546" alt="Captura de ecrã 2024-07-02, às 20 02 08" src="https://github.com/elsei123/BattleshipGame/assets/164704332/8c87481f-f651-4bdd-9fe7-118fa5cf2ecb">


- __Receive Hints:__ If you guess incorrectly, you'll receive a hint about the word. This helps guide your future guesses.

  <img width="736" alt="Captura de ecrã 2024-07-02, às 20 03 23" src="https://github.com/elsei123/BattleshipGame/assets/164704332/65c07ff1-3bbf-483b-8093-945796395ed5">


- __Keep Playing:__ Continue guessing until you guess the word or run out of attempts. The game provides ongoing feedback on the word's state and the number of attempts remaining.

  <img width="432" alt="Captura de ecrã 2024-07-04, às 20 49 21" src="https://github.com/elsei123/BattleshipGame/assets/164704332/8119efc9-c25a-43b8-91ae-5d9630f01940">


- __Win or Lose:__ If you guess all letters of the word before running out of attempts, you win. Otherwise, you lose and the word is revealed.
  <img width="539" alt="Captura de ecrã 2024-07-02, às 20 07 25" src="https://github.com/elsei123/BattleshipGame/assets/164704332/afa7680d-0d2b-4814-829e-57a8bcccbd77">

  <img width="465" alt="Captura de ecrã 2024-07-02, às 20 04 52" src="https://github.com/elsei123/BattleshipGame/assets/164704332/a92700bd-e553-4e37-afff-965be4354d55">


## Features
### Current Features

- __Random Word Selection:__ The game selects a random word with a hint from a predefined list, ensuring variety in each new game.

- __Display Guessed Letters:__ Shows the current state of the word with guessed letters and underscores for unguessed letters, allowing the player to track their progress.

- __Hints:__ Provides a hint after an incorrect guess, increasing the player's chances of success.

- __Input Validation:__ Ensures that only valid alphabetic characters are accepted as guesses, preventing invalid and duplicate entries.

### Future Features

- __Word Categories:__ Add different categories for word selection, allowing players to choose specific themes like "Programming Languages," "Development Tools," etc.
  
- __Difficulty Levels:__ Implement difficulty levels such as easy, medium, and hard to challenge players according to their skills.
  
- __Multiplayer Mode:__ Enable two or more players to play together, making the game more social and competitive.

## Data Model

The game utilizes a simple yet effective data model:

- __List of Words and Hints:__ A list of tuples where each tuple contains a word and its corresponding hint.

- __Set of Guessed Letters:__ A set to store letters that have been correctly guessed by the player, facilitating the checking and updating of the word's state.

- __Remaining Attempts:__ A counter for the remaining attempts before the game ends, providing a limit to the number of errors the player can make.

## Testing

The project has been rigorously tested to ensure a smooth gameplay experience with no bugs:

### Testing Methodology

- __Cross-Platform Execution:__ The game has been tested on different operating systems such as Windows, macOS, and Linux to ensure compatibility.

- __Input Validation:__ I tested valid inputs (alphabetic letters) and invalid inputs (numbers, symbols, multiple letters) to ensure the game responds correctly.

- __Hint Display:__ I verified that hints are displayed correctly after incorrect guesses, helping the player to guess the word.

- __End Game Messages:__ I confirmed that the game ends correctly with a victory or defeat message, depending on the player's performance.

## Bugs 

### solved Bugs 

- __Guess Validation:__ Fixed an issue where non-alphabetic characters were accepted as guesses.

- __End Game Messages:__ Resolved a bug where the game did not correctly display victory/defeat messages.

### Remaining Bugs

- __No Known Bugs:__ Currently, there are no known bugs in the game.

## Validator Testing
- __PEP8__
 - No erros were returned from [PEP8](https://pep8ci.herokuapp.com/)
  
## Deployment

This project has been deployed using the Code Institute's simulated terminal on Heroku, providing a robust and accessible development environment.

### Deployment Steps

- __Fork or Clone:__ Fork or clone this repository.

- __New App on Heroku:__ Create a new app on Heroku.

- __Configure Buildpacks:__ Set up buildpacks for Python and NodeJS in that order.

- __Link to Repository:__ Link your Heroku app to the GitHub repository.

- __Deploy:__ Click on Deploy in the Heroku dashboard to deploy the project.

## Credits

- __List of Words and Hints:__ Inspired by common programming terms.
- __Code Institute:__ Provided the simulated terminal and deployment guidance.
