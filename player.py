class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def place_ships(self):
        """Default ship placement for a player."""
        self.board.place_all_ships()
