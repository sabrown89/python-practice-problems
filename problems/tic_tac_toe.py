from IPython import embed
import sys

class Grid(object):
    def __init__(self):
        self.a1 = "a1"
        self.a2 = "a2"
        self.a3 = "a3"
        self.a4 = "a4"
        self.a5 = "a5"
        self.a6 = "a6"
        self.a7 = "a7"
        self.a8 = "a8"
        self.a9 = "a9"

    def view_grid(self):
        grid_output = f'''
           {self.a1}  | {self.a2}   | {self.a3}
          _______________
           {self.a4}  | {self.a5}   | {self.a6}
          _______________
           {self.a7}  | {self.a8}   | {self.a9}
        '''
        print(grid_output)

    def user_input(self, move, mark):
        if mark == "x":
            setattr(self, move, mark)
        else:
            setattr(self, move, mark)


    def player_win(self, player):
        mark = player[1]
        win = (mark, mark, mark)
        return (
            (self.a1, self.a2, self.a3) == win or
            (self.a4, self.a5, self.a6) == win or
            (self.a7, self.a8, self.a9) == win or
            (self.a1, self.a4, self.a7) == win or
            (self.a2, self.a5, self.a8) == win or
            (self.a3, self.a6, self.a9) == win or
            (self.a1, self.a5, self.a9) == win or
            (self.a3, self.a5, self.a7) == win
        )

player_1 = input("Player one name: ")
player_2 = input("Player two name: ")

players = [(player_1, "x"), (player_2, "o")]
grid = Grid()
print("\nSelect a placement that is available. If you see an 'x' or 'o' in a location, that spot is not available. Type in your desired location exactly as it appears on the board. An example location is a4. Once your location is selected, hit enter.")

for movecount in range(9):
    player = players[movecount % 2]

    while True:
        try:
           grid.view_grid()
           move = input("player select location: ")
           getattr(grid, move)

        except AttributeError:
            print("\nInvalid input, please choose a placement with the letter l + the location. An example would be a1 or a7")
            continue

        if len(getattr(grid, move)) == 1:
            print("\nThat move is taken, choose another available slot")
            continue

        grid.user_input(move, player[1])
        grid.view_grid()
        print("nice move!")

        if grid.player_win(player):
            result = f'Congratulations {player[0]}! Winner, winner, chicken dinner\n'
            print(result)
            sys.exit(1)
        elif movecount < 8:
            break
        else:
            print("It's a tie!")
