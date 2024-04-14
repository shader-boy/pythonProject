import random


# initialize the game board
board = {
    1: 2, 2: 0, 3: 0, 4: 0, 5: 0, 6: -5,
    7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 5,
    13: -3, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0,
    19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 2
}

def print_board():
    print("24 " + "-" * 60 + " 1")
    print("|   |   |   |   |   |   |BAR|   |   |   |   |   |")
    print("|{:3}|{:3}|{:3}|{:3}|{:3}|{:3}|    |{:3}|{:3}|{:3}|{:3}|{:3}|".format(*[board[i] for i in range(24, 12, -1)]))
    print("|   |   |   |   |   |   |BAR|   |   |   |   |   |")
    print("-" * 67)
    print("|   |   |   |   |   |   |BAR|   |   |   |   |   |")
    print("|{:3}|{:3}|{:3}|{:3}|{:3}|{:3}|    |{:3}|{:3}|{:3}|{:3}|{:3}|".format(*[board[i] for i in range(1, 13)]))
    print("|   |   |   |   |   |   |BAR|   |   |   |   |   |")
    print("13 " + "-" * 60 + " 12")

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def is_valid_move(start, end, player):
    if start == end or end < 1 or end > 24:
        return False
    if player == 1:
        if board[start] < 0:
            return False
    else:
        if board[start] > 0:
            return False
    return True

def make_move(start, end, player):
    if player == 1:
        board[start] -= 1
    else:
        board[start] += 1
    if abs(start - end) == 1:
        if player == 1:
            board[end] += 1
        else:
            board[end] -= 1
    else:
        if player == 1:
            board[end] -= 1
        else:
            board[end] += 1

def play_nard():
    player = 1
    while True:
        print_board()
        print("Player", player, "'s turn")
        input("Press Enter to roll the dice...")
        dice1, dice2 = roll_dice()
        print("Dice:", dice1, dice2)
        valid_moves = []
        for start in range(1, 25):
            end1 = start + dice1
            end2 = start + dice2
            if is_valid_move(start, end1, player):
                valid_moves.append((start, end1))
            if is_valid_move(start, end2, player):
                valid_moves.append((start, end2))
        if len(valid_moves) == 0:
            print("No valid moves. Skipping turn.")
            player = 3 - player
            continue
        print("Valid moves:", valid_moves)
        start, end = valid_moves[random.randint(0, len(valid_moves) - 1)]
        print("Making move:", start, "->", end)
        make_move(start, end, player)
        player = 3 - player


# Start the game
play_nard()



