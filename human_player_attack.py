from player import Player

class HumanPlayer(Player):
    def attack(self, opponent_board):
        """Allows the human player to attack the opponent's board."""
        while True:
            try:
                coords = input("Enter coordinates to attack (e.g., 2(horizontal) 3(vertical)): ").split()
                x, y = int(coords[0]), int(coords[1])
                if 0 <= x < opponent_board.size and 0 <= y < opponent_board.size:
                    result = opponent_board.receive_attack(x, y)
                    if result is not None:
                        if result:
                            print(f"{self.name} hit a ship at ({x}, {y})!")
                        else:
                            print(f"{self.name} missed at ({x}, {y}).")
                        return result
                    else:
                        print("You already attacked this spot. Try again.")
                else:
                    print("Coordinates out of bounds. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter coordinates as two integers separated by a space.")