

import random
import pygame
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class Board:
    def __init__(self, size=10):  # Fixed constructor
        self.size = size
        self.grid = [["~"] * size for _ in range(size)]  # "~" represents water
        self.ship_sizes = [5, 4, 3, 3, 2]  # Sizes of ships
        self.ships = []  # To store ship coordinates
        pygame.mixer.init()  # Initialize pygame mixer for sound

    def place_ship(self, size):
        """Attempts to place a ship of a given size on the board."""
        for _ in range(100):  # Try 100 times to place the ship
            direction = random.choice(["horizontal", "vertical"])
            if direction == "horizontal":
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - size)
                coordinates = [(x, y + i) for i in range(size)]
            else:  # vertical
                x = random.randint(0, self.size - size)
                y = random.randint(0, self.size - 1)
                coordinates = [(x + i, y) for i in range(size)]

            # Check if the ship overlaps with existing ships
            if all(self.grid[x][y] == "~" for x, y in coordinates):
                for x, y in coordinates:
                    self.grid[x][y] = "S"
                self.ships.append(coordinates)
                return True
        return False

    def place_all_ships(self):
        """Places all ships on the board based on the defined sizes."""
        for size in self.ship_sizes:
            if not self.place_ship(size):
                raise RuntimeError("Unable to place all ships on the board.")

    def receive_attack(self, x, y):
        """Handles an attack on the board."""
        if self.grid[x][y] == "S":
            self.grid[x][y] = "X"  # "X" represents a hit
            self.play_sound('hit_sound.mp3')  # Play sound for a hit
            time.sleep(1)
            return True
        elif self.grid[x][y] == "~":
            self.grid[x][y] = "O"  # "O" represents a miss
            self.play_sound('miss_sound.mp3')  # Play sound for a miss
            return False
        return None  # Already attacked

    def play_sound(self, sound_file):
        """Plays the given sound file using pygame."""
        try:
            sound = pygame.mixer.Sound(sound_file)
            sound.play()
        except pygame.error as e:
            print(f"Error playing sound {sound_file}: {e}")

    def display(self, hide_ships=False):
        """Displays the board with coordinates, keeping both rows and columns visible."""
        print("   " + " ".join([str(i) for i in range(self.size)]))  # Column headers
        for idx, row in enumerate(self.grid):
            row_to_display = []
            for cell in row:
                if hide_ships and cell == "S":
                    row_to_display.append(Fore.CYAN + "~")  # Hide ships as water
                elif cell == "S":
                    row_to_display.append(Fore.RED + "S")  # Ship in red
                elif cell == "X":
                    row_to_display.append(Fore.GREEN + "X")  # Hit in green
                elif cell == "O":
                    row_to_display.append(Fore.YELLOW + "O")  # Miss in yellow
                else:
                    row_to_display.append(Fore.BLUE + "~")  # Water in blue
            print(f"{idx:2} " + " ".join(row_to_display))  # Row number and grid

    def is_all_ships_destroyed(self):
        """Checks if all ships are destroyed."""
        for ship in self.ships:
            if any(self.grid[x][y] == "S" for x, y in ship):
                return False
        return True
