board = [
    ["X", "O", "X"], # 1
    [" ", " ", " "], # 2
    ["O", " ", " "], # 3
]   # A    B    C

def get_row_col(reply):
    translation = reply.upper()
    col = translation[0]
    row = int(translation[1]) - 1

    board_keys = {"A": 0, "B": 1, "C": 2}

    for key in board_keys:
        if key == col:
            column = board_keys[key]
            return (row, column)

print(get_row_col("c2"))