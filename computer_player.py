
import random
from player import Player

class ComputerPlayer(Player):
    def __init__(self, name, board):
        super().__init__(name, board)
        self.pending_targets = []  # Store cells adjacent to hits for smarter attacks
        self.attacked_positions = set()  # Track positions already attacked

    def attack(self, opponent_board):
        """Allows the computer to attack the opponent's board using a smart algorithm."""
        def is_valid_position(x, y):
            """Check if a position is within bounds and not already attacked."""
            return 0 <= x < opponent_board.size and 0 <= y < opponent_board.size and (x, y) not in self.attacked_positions

        # Choose target: pending targets first or random positions
        if self.pending_targets:
            x, y = self.pending_targets.pop(0)  # Attack a pending target
        else:
            while True:
                x, y = self.random_unattacked_position(opponent_board.size)
                if is_valid_position(x, y):
                    break

        # Attack the chosen position
        result = opponent_board.receive_attack(x, y)
        self.attacked_positions.add((x, y))  # Mark the position as attacked

        # Handle result
        if result is not None:
            if result:  # It's a hit
                print(f"{self.name} hit a ship at ({x}, {y})!")
                # Add adjacent cells to pending targets
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
                    nx, ny = x + dx, y + dy
                    if is_valid_position(nx, ny):
                        self.pending_targets.append((nx, ny))
            else:
                print(f"{self.name} missed at ({x}, {y}).")
        return result

    def random_unattacked_position(self, board_size):
        """Generates a random unattacked position."""
        return random.randint(0, board_size - 1), random.randint(0, board_size - 1)
