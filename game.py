
from board import Board
from human_player_place import HumanPlayer as HumanPlayerPlace
from human_player_attack import HumanPlayer as HumanPlayerAttack
from computer_player import ComputerPlayer
from utils import print_divider

def main():
    board_size = 10

    # Create boards
    human_board = Board(board_size)
    computer_board = Board(board_size)

    # Create players
    human_place = HumanPlayerPlace("You", human_board)  # Handles placing ships
    human_attack = HumanPlayerAttack("You", human_board)  # Handles attacking
    computer = ComputerPlayer("Computer", computer_board)

    # Place ships
    print("Place your ships manually.")
    human_place.place_ships()
    print("\nComputer is placing its ships...")
    computer.place_ships()

    # Main game loop
    while True:
        print_divider()
        print("Your board:")
        human_board.display()

        print_divider()
        print("Computer's board (hidden):")
        computer_board.display(hide_ships=True)

        print_divider()
        print("Your turn:")
        hit = human_attack.attack(computer_board)
        if hit:
            print("You hit a ship!")
        else:
            print("You missed!")

        if computer_board.is_all_ships_destroyed():
            print("Congratulations! You sunk all the computer's ships!")
            break

        print_divider()
        print("Computer's turn...")
        hit = computer.attack(human_board)
        if hit:
            print("The computer hit your ship!")
        else:
            print("The computer missed!")

        if human_board.is_all_ships_destroyed():
            print("Oh no! The computer sunk all your ships!")
            break

if __name__ == "__main__":
    main()
