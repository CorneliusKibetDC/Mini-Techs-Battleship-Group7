


import hashlib
import os
from board import Board
from human_player_place import HumanPlayer as HumanPlayerPlace
from human_player_attack import HumanPlayer as HumanPlayerAttack
from computer_player import ComputerPlayer
from utils import print_divider

USER_FILE = "users.txt"

def hash_password(password):
    """Hashes a password using SHA-256 for security."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Loads users from the file into a dictionary."""
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as file:
        lines = file.readlines()
    users = {}
    for line in lines:
        username, hashed_password = line.strip().split(",")
        users[username] = hashed_password
    return users

def save_users(users):
    """Saves the users dictionary to the file."""
    with open(USER_FILE, "w") as file:
        for username, hashed_password in users.items():
            file.write(f"{username},{hashed_password}\n")

def signup(users):
    """Handles user signup."""
    print("Sign Up")
    while True:
        username = input("Enter a username: ")
        if username in users:
            print("Username already exists. Try a different one.")
        else:
            password = input("Enter a password: ")
            confirm_password = input("Confirm your password: ")
            if password == confirm_password:
                users[username] = hash_password(password)
                save_users(users)
                print("Signup successful!")
                return username
            else:
                print("Passwords do not match. Try again.")

def login(users):
    """Handles user login."""
    print("Log In")
    while True:
        username = input("Enter your username: ")
        if username in users:
            password = input("Enter your password: ")
            if users[username] == hash_password(password):
                print("Login successful!")
                return username
            else:
                print("Incorrect password. Try again.")
        else:
            print("Username not found. Try again or sign up.")

def main():
    print("Welcome to Battleship!")
    users = load_users()  # Load users from file

    while True:
        choice = input("Do you want to (1) Log In or (2) Sign Up? Enter 1 or 2: ")
        if choice == "1":
            username = login(users)
            break
        elif choice == "2":
            username = signup(users)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print(f"\nWelcome, {username}! Please log in again to start placing your ships.")

    # Require the user to log in again before placing ships
    while True:
        print("\nPlease log in to proceed with placing your ships.")
        second_login_username = login(users)
        if second_login_username == username:
            print("Second login successful. You may now place your ships.")
            break
        else:
            print("The login credentials do not match the original user. Please try again.")

    board_size = 10

    # Create boards
    human_board = Board(board_size)
    computer_board = Board(board_size)

    # Create players
    human_place = HumanPlayerPlace(username, human_board)
    human_attack = HumanPlayerAttack(username, human_board)
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
