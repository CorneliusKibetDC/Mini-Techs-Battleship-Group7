from player import Player

class ComputerPlayer(Player):
    def init(self, name, board):
        super().init(name, board)
        self.pending_targets = []  # To store cells adjacent to hits for targeted attacks
        self.attacked_positions = set()  # To track already attacked positions

def attack(self, opponent_board):
    """Allows the computer to attack the opponent's board using a smarter algorithm."""
    def is_valid_position(x, y):
        return 0 <= x < self.board.size and 0 <= y < self.board.size and (x, y) not in self.attacked_positions

    if self.pending_targets:
        # If there are pending targets, prioritize them
        x, y = self.pending_targets.pop(0)
    else:
        # Choose a random position that hasn't been attacked yet
        while True:
            x, y = self.random_unattacked_position()
            if (x, y) not in self.attacked_positions:
                break

    # Attack the chosen position
    result = opponent_board.receive_attack(x, y)
    self.attacked_positions.add((x, y))

    if result is not None:
        if result:  # If it's a hit
            print(f"{self.name} hit a ship at ({x}, {y})!")
            # Add adjacent cells to pending targets
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if is_valid_position(nx, ny):
                    self.pending_targets.append((nx, ny))
        else:
            print(f"{self.name} missed at ({x}, {y}).")
    return result

def random_unattacked_position(self):
    """Generates a random unattacked position."""
    import random
    return random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1)