import random

# tic_tac_toe

play_table = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
variants = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def main():
    while True:
        you_turn()
        print_table(play_table)
        if who_von():
            break
        computer_turn()
        print_table(play_table)
        if who_von():
            break
        if game_over():
            break


def print_table(table):
    i = 0
    while i < len(table):
        print(table[i], table[i + 1], table[i + 2])
        i += 3


def you_turn():
    while True:
        turn = input('You turn: ')
        while True:
            if turn not in variants:
                turn = input('it is incorrect field, please, select again: ')
            elif turn in variants:
                make_a_turn(turn, 'X')
                break
        return True


def computer_turn():
    print('Computer turn')
    while True:
        turn = random.choice(variants)
        if turn in variants:
            make_a_turn(turn, '0')
            break


def game_over():
    game_done = input('Forfeit? y/n ')
    if game_done.lower() == 'y':
        print('Game over.')
        return True


def make_a_turn(num, p):
    variants.remove(num)
    play_table[int(num) - 1] = p
    return True


def who_von():
    i = 0
    for j in range(3):
        if play_table[j] == play_table[j + 3] and play_table[j + 3] == play_table[j + 6]:
            if play_table[j] == '0':
                print("computer von.")
                return True
            elif play_table[j] == 'X':
                print('you von!')
                return True
            else:
                return False
    while i in range(len(play_table)):
        if play_table[i] == play_table[i + 1] and play_table[i + 1] == play_table[i + 2]:
            if play_table[i] == '0':
                print("computer von")
                return True
            elif play_table[i] == 'X':
                print('you von!')
                return True
            else:
                return False
        i += 3

    if play_table[0] == play_table[4] and play_table[4] == play_table[8]:
        if play_table[4] == '0':
            print("computer von")
        elif play_table[4] == 'X':
            print('you von!')
            return True
    elif play_table[2] == play_table[4] and play_table[4] == play_table[6]:
        if play_table[4] == '0':
            print("computer von")
            return True
        elif play_table[4] == 'X':
            print('you von!')
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    main()
