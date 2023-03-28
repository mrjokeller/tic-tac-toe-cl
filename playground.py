class Playground:
    
    def __init__(self):
        self.board = "   |   |   \n-----------\n   |   |   \n-----------\n   |   |   "
        self.open_spots = {
            1: 1,
            2: 5,
            3: 9,
            4: 25,
            5: 29,
            6: 33,
            7: 49,
            8: 53,
            9: 57
                           }
        self.closed_spots = {"X": [], "O": []}
        self.winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
           
    def show_board(self):
        print(f"\nOpen spots: {list(self.open_spots.keys())}\n")
        print(self.board)
        
    def update_board(self, spot: int, player):
        b = list(self.board)
        b[self.open_spots[spot]] = player
        self.board = "".join(b)
        self.open_spots.pop(int(spot))
        self.closed_spots[player].append(spot)
        self.show_board()
        
    def check_win(self, player):
        return any([all([spot in self.closed_spots[player] for spot in combo]) for combo in self.winning_combos])
