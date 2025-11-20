
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a console-based Hangman game that teaches string manipulation, loop logic, and input handling in Python. Students will write a clean game loop, show progress to the player, and present win/lose states.

## 📝 Tasks

### 🛠️ Build the Hangman Core

#### Description
Implement the core Hangman game that randomly selects a word from a list and lets the player guess letters until the word is revealed or attempts run out.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list (see `starter-code.py`).
- Accept single-letter guesses and ignore repeated guesses.
- Show current progress using blanks and revealed letters (e.g., "p _ t h o n").
- Display the remaining incorrect guesses and the letters the player has guessed so far.
- End when the player guesses the word or uses up all attempts and display a win/lose message.

Example game interaction:

```
Secret word: _ _ _ _ _ _
Guesses left: 6
Guessed letters: 
Enter a letter: p
Progress: p _ _ _ _ _
Guesses left: 6
```

### 🛠️ Add Features & Polish

#### Description
Add optional features to make the game more robust and user-friendly.

#### Requirements
Completed program may include one or more of the following:

- Input validation to ensure exactly one alphabetic character is accepted per turn.
- A replay option so players can play multiple rounds without restarting the program.
- A hint system or difficulty levels (e.g., more/less guesses based on difficulty).
- Persist high scores or win counts across runs (optional, file I/O).

Tip: Start with the `starter-code.py` file in this folder — it includes simple scaffolding for picking words and running a loop.

**Skills practiced:** String manipulation, loops, conditionals, random selection, basic I/O
