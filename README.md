# Tic-Tac-Toe Python Game

![Tic-Tac-Toe](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Tic_tac_toe.svg/200px-Tic_tac_toe.svg.png)

A complete command-line implementation of Tic-Tac-Toe built with Python using Object-Oriented Programming principles. Supports human vs human and human vs computer gameplay.

## Features

- 🎮 **Two Game Modes**
  - Human vs Human (2 players)
  - Human vs Computer (single player)
- 🖥️ **Interactive Console Interface**
  - Clear board visualization
  - Turn indicators
- ⚙️ **Input Validation**
  - Prevents invalid moves
  - Handles number input errors
- 🏆 **Win Detection**
  - All 8 possible winning combinations
  - Draw game detection
- 🤖 **Computer AI**
  - Random move selection
  - Easy to extend for smarter AI

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-python.git
   cd tic-tac-toe-python
Ensure you have Python 3.x installed

How to Play
Run the game:

bash
python tic_tac_toe.py
Select game mode when prompted:

text
1 - Human vs Human
2 - Human vs Computer
Players take turns entering numbers 1-9 corresponding to board positions:

text
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
The game automatically ends when a player wins or the board is full.

Code Structure
The game is built using these main classes:

Class	Description
GameBoard	Manages game state and board logic
Player	Abstract base class for players
HumanPlayer	Handles human player input
ComputerPlayer	Implements computer opponent
GameEngine	Controls game flow and rules
Example Gameplay
text
Current board:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Player X, enter position (1-9): 5

| 1 | 2 | 3 |
| 4 | X | 6 |
| 7 | 8 | 9 |

Computer chooses position 1

| O | 2 | 3 |
| 4 | X | 6 |
| 7 | 8 | 9 |
Customization
You can easily modify the game:

Change player symbols by editing the symbol attributes

Improve the AI by modifying the ComputerPlayer class

Adjust board visuals in the print_board() method

Add new features like score tracking

License
This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy the game! For feature requests or bug reports, please open an issue.

text

This README includes:
1. Project title and visual
2. Key features with emojis
3. Installation instructions
4. Gameplay instructions
5. Code structure documentation
6. Example gameplay
7. Customization tips
8. License information