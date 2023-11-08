# TIC-TAC-TOE Game

Welcome to a simple command-line implementation of the classic TIC-TAC-TOE game in Python. This game allows two players to compete against each other, and one of the players is powered by the MiniMax algorithm, making it a formidable opponent. Follow the instructions below to enjoy the game!

## Instructions

1. Clone or download the project to your local machine.

2. Navigate to the project directory in your terminal.

3. Run the game by executing the following command:

   ```python your_game_file.py```

   Replace `your_game_file.py` with the name of the file where you have the game code.

4. Follow the on-screen instructions to play the game.

## How to Play

- The game starts by displaying an empty board.

- Two players, "Bob" and "Alice," take turns to make their moves. "Bob" plays as "X," and "Alice" plays as "O."

- The game is played in turns, starting with "Bob."

- Players are prompted to enter their moves by specifying the row and column where they want to place their symbol. For example, entering "0 1" would place the player's symbol in the first row and the second column.

- The game continues until one of the players wins by getting three of their symbols in a row, column, or diagonal, or if the board is filled with no winner, resulting in a tie.

- After the game ends, you will be asked if you want to play another round. Type "Y" to play again or "N" to exit the game.

## Game Features

- The game features a simple command-line interface for user interaction.

- The MiniMax algorithm is used to power one of the players, providing a challenging opponent for human players.

## Example Output

Here's an example of how the game might look when running:

```
Welcome to TIC-TAC-TOE Game!

  |   |
---------
  |   |
---------
  |   |

"Bob" (X), it's your turn. Enter your move (row column): 1 1

  |   |
---------
  | X |
---------
  |   |

"Alice" (O), it's your turn. Enter your move (row column): 0 0

O |   |
---------
  | X |
---------
  |   |

...

O | X | X
---------
  | X | O
---------
  | O | X

"Alice" is a winner!
Would you like to play again? [Y/N]
```

Enjoy the game and have fun playing TIC-TAC-TOE!

## Author

This TIC-TAC-TOE game was created by Kriti Bhargava.

## Acknowledgments

- Special thanks to the Python community for their continuous support and inspiration.

- The MiniMax algorithm implementation is based on classic game theory and AI principles.

- Feel free to contribute to and improve this game by submitting pull requests or reporting issues. Happy coding!
