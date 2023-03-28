import random
from playground import Playground


def main():
    mode = int(input("Choose a mode (against human(1) or AI(2)): "))
    if mode == 1:
        h_vs_h()
    else:
        h_vs_ai()
        
        
def h_vs_ai():
    playground = Playground()
    playground.show_board()
    
    current_player = random.choice(["H", "A"])
    print(f"{current_player} starts!")
    while True:
        while True:
            if current_player == "H":
                # Choice of spot
                spot = int(input("Choose a spot: "))
            else:
                # AI choice of spot
                spot = random.choice(list(playground.open_spots.keys()))
                print(f"AI chose spot {spot}")
            # Update board with chosen spot
            try:
                print("Played")
                playground.update_board(spot, current_player)
                break
            except KeyError:
                print("Invalid spot! Try again.")
        # Check if there is a winner
        if len(playground.open_spots) == 0:
            print("It's a tie!")
            break
        elif playground.check_win(current_player):
            print(f"{current_player} wins!")
            break
        # Switch player
        if current_player == "H":
            current_player = "A"
        else:
            current_player = "H"
    

def h_vs_h():
    playground = Playground()
    playground.show_board()
    
    current_player = random.choice(["X", "O"])
    print(f"{current_player} starts!")
    while True:
        while True:
            # Choice of spot
            spot = int(input("Choose a spot: "))
            # Update board with chosen spot
            try:
                playground.update_board(spot, current_player)
                break
            except KeyError:
                print("Invalid spot! Try again.")
        # Check if there is a winner
        if len(playground.open_spots) == 0:
            print("It's a tie!")
            break
        elif playground.check_win(current_player):
            print(f"{current_player} wins!")
            break
        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    
    
if __name__ == "__main__":
    main()
    