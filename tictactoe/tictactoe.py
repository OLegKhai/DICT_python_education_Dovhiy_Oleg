def print_board(cells):
    print("---------")
    for i in range(0, 9, 3):
        print(f"| {' '.join(cells[i:i + 3])} |")
    print("---------")


def analyze_game(cells):
    def check_win(symbol):
        return any(all(cell == symbol for cell in row) for row in
                   [cells[:3], cells[3:6], cells[6:], cells[::3], cells[1::3], cells[2::3], cells[::4], cells[2:8:2]])

    count_x = cells.count("X")
    count_o = cells.count("O")

    diff = abs(count_x - count_o)

    if check_win("X") and check_win("O") or diff > 1:
        return "Impossible"
    elif check_win("X"):
        return "X wins"
    elif check_win("O"):
        return "O wins"
    elif "_" not in cells:
        return "Draw"
    else:
        return "Game not finished"


def get_coordinates(cells, current_player):
    while True:
        try:
            coordinates = input(f"{current_player}'s turn. Enter the coordinates: ").split()
            x, y = map(int, coordinates)
            print(f"Debug: Trying to place '{current_player}' at ({x}, {y})")
            if not (1 <= x <= 3 and 1 <= y <= 3):
                print("Coordinates should be from 1 to 3!")
            elif cells[(3 - y) * 3 + (x - 1)] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                return x, y
        except ValueError:
            print("You should enter numbers!")


def switch_player(current_player):
    return "O" if current_player == "X" else "X"


def main():
    cells = ["_"] * 9
    print_board(cells)

    current_player = "X"

    while True:
        x, y = get_coordinates(cells, current_player)
        index = (3 - y) * 3 + (x - 1)

        if cells[index] == "_":
            cells[index] = current_player
        else:
            print("This cell is occupied! Choose another one!")
            continue

        print_board(cells)
        result = analyze_game(cells)

        if result in ["X wins", "O wins", "Draw"]:
            print(result)
            break

        current_player = switch_player(current_player)


if __name__ == "__main__":
    main()
