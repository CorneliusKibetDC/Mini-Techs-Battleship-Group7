# Battleship Game (CLI)

Welcome to the Battleship game! This is a command-line (CLI) version of the classic Battleship game, where you can play against the computer. The game involves placing ships on a grid and attempting to sink the opponent's ships by guessing their coordinates.

## How to Play

### 1. Start the Game
To start the game, run the Python script `game.py` from your terminal:

```bash
python game.py


2. Player Setup
When the game begins, you will be prompted to place your ships on a 10x10 grid. The game includes the following ships with specific sizes:

1 ship of size 5
1 ship of size 4
2 ships of size 3
1 ship of size 2
You will need to place these ships one by one by entering the starting coordinates and choosing whether you want them to be placed horizontally or vertically.

How to Place a Ship:
For each ship, enter the starting coordinates (row and column).
After that, specify the direction: h for horizontal or v for vertical.
The ships must fit within the grid and cannot overlap with other ships.
3. Computer Setup
The computer will also place its ships randomly on the grid. You will not see the computer's ship positions, but they will be placed just like yours.

4. Attacking
Once all ships are placed, the game alternates turns between you and the computer. On your turn, you will be asked to enter the coordinates to attack. The goal is to hit and sink the computer's ships.

How to Attack:
You will be prompted to enter the coordinates (row and column) where you want to attack.
If you hit a ship, the game will mark the position as a "hit" (X).
If you miss, the game will mark the position as a "miss" (O).
You cannot attack the same spot twice, so make sure to choose a new spot for each attack.
5. Winning the Game
The game continues until all of one player's ships are destroyed. If you sink all the computer's ships, you win the game!

Example of the Game Flow
Player places ships: You are prompted to place each ship by entering starting coordinates and direction.
Computer places ships: The computer places its ships randomly.
Turn-based play: You and the computer take turns attacking each other's boards.
End of game: The first player to sink all of the opponent's ships wins.
Board Representation
Each grid cell is represented by:
~ for water (empty space)
S for a ship
X for a hit
O for a miss
The grid is 10x10, with coordinates starting from (0,0) to (9,9).