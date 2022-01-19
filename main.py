import time
import keyboard
from sys import exit
import pickle
import os
from save_class import saved
current_level = 0
all_levels = [0, 27, 54, 81, 108, 135, 162, 189]  # from levels.txt


level_y = [[] for a in range(24)]

enemy_x = 65
enemy_y = 20
e_last_x = 56
e_last_y = 20
player_x = 6
player_y = 3
last_x = 6
last_y = 3
lives = 5
score = 0
loop = True
saved_variables = []


def print_level():
    for row in level_y:
        print(*row,sep='')



def clear_level():
    for row in level_y:
        row.clear()


def new_level():
    global player_x
    global player_y
    global enemy_x
    global enemy_y
    enemy_x = 65
    enemy_y = 20
    player_x = 6
    player_y = 3
    clear_level()
    byte = all_levels[current_level]
    range_value = byte
    range_value2 = byte + 24
    row = 0
    while byte in range(range_value, range_value2):
        read_file = open('levels.txt', 'r')
        read_line = read_file.readlines()
        final_answer = read_line[byte]
        byt = 0
        first = 0
        second = 1
        while byt in range(0, 72):
            # line_y = level_y[row]
            level_y[row].append(final_answer[first:second])
            first = first + 1
            second = second + 1
            byt = byt + 1
        byte = byte + 1
        row = row + 1

    level_y[0].append(">Score: ")
    level_y[0].append("")
    level_y[1].append(">Lives: ")
    level_y[1].append("")


def save():
    global saved_variables
    global score
    global lives
    global player_x
    global player_y
    global enemy_x
    global enemy_y
    global current_level
    saved_variables = saved(score, lives, current_level)

    with open('chase_save.txt', 'wb') as fp:
        pickle.dump(saved_variables, fp)
    print('saved to "chase_save.txt"')
    time.sleep(1)
    pause_menu(0)


def open_save():
    global saved_variables
    global score
    global lives
    global player_x
    global player_y
    global enemy_x
    global enemy_y
    global current_level
    print('opening "chase_save.txt"')
    time.sleep(1)
    with open('chase_save.txt', 'rb') as fp:
        saved_variables = pickle.load(fp)
    score = saved_variables[0]
    lives = saved_variables[1]
    current_level = saved_variables[2]
    pause_menu(0)


def pause_menu(print_pause):
    if print_pause == 1:
        print(" _ __   __ _ _   _ ___  ___ ")
        print("| |   \ / _` | | | / __|/ _ \ ")
        print("| |   |  (_| | |_| \__ \  __/")
        print("| |  / \__,_|\__,_|___/\___|")
        print("|_|  | |    ")
        print("")
    print('"c" to resume, "q" to quit, "s" to save, "o" to open an existing game')
    while loop:
        if keyboard.is_pressed('c'):
            return
        if keyboard.is_pressed('q'):
            exit()
        if keyboard.is_pressed('s'):
            save()
        if keyboard.is_pressed('o'):
            open_save()


def take_inputs():
    move_up = True
    move_down = True
    move_right = True
    move_left = True
    e_move_up = True
    e_move_down = True
    e_move_right = True
    e_move_left = True
    global last_y
    global last_x
    global player_y
    global player_x
    global e_last_y
    global e_last_x
    global enemy_y
    global enemy_x
    global loop
    global score
    global lives
    last_x = player_x
    last_y = player_y

    which_y = level_y[player_y + 1]
    y_up = which_y[player_x]

    which_y = level_y[player_y - 1]
    y_down = which_y[player_x]

    which_y = level_y[player_y]
    x_right = which_y[player_x + 1]

    x_left = which_y[player_x - 1]
    if y_up == "#":
        move_up = False
    if y_down == "#":
        move_down = False
    if x_right == "#":
        move_right = False
    if x_left == "#":
        move_left = False

    if keyboard.is_pressed('p'):
        pause_menu(1)

    if move_down:
        if keyboard.is_pressed('w'):
            player_y = player_y - 1
            if y_down == "^" or y_down == ">" or y_down == "v" or y_down == "<":
                score = 0
                lives = lives - 12
                new_level()
            if y_down == "c":
                score = score + 1
            if y_down == "H":
                lives = lives + 1
    if move_up:
        if keyboard.is_pressed('s'):
            player_y = player_y + 1
            if y_up == "^" or y_up == ">" or y_up == "v" or y_up == "<":
                score = 0
                lives = lives - 1
                new_level()
            if y_up == "c":
                score = score + 1
            if y_up == "H":
                lives = lives + 1
    if move_left:
        if keyboard.is_pressed('a'):
            player_x = player_x - 1
            if x_left == "^" or x_left == ">" or x_left == "v" or x_left == "<":
                score = 0
                lives = lives - 1
                new_level()
            if x_left == "c":
                score = score + 1
            if x_left == "H":
                lives = lives + 1
    if move_right:
        if keyboard.is_pressed('d'):
            player_x = player_x + 1
            if x_right == "^" or x_right == ">" or x_right == "v" or x_right == "<":
                score = 0
                lives = lives - 1
                new_level()
            if x_right == "c":
                score = score + 1
            if x_right == "H":
                lives = lives + 1

    e_last_x = enemy_x
    e_last_y = enemy_y

    which_y = level_y[enemy_y + 1]
    y_up = which_y[enemy_x]

    which_y = level_y[enemy_y - 1]
    y_down = which_y[enemy_x]

    which_y = level_y[enemy_y]
    x_right = which_y[enemy_x + 1]
    x_left = which_y[enemy_x - 1]
    if y_up == "#" or y_up == "^" or y_up == ">" or y_up == "<" or y_up == "v" or y_up == "+" or y_up == "c" or y_up == "H":
        e_move_up = False
    if y_down == "#" or y_down == "^" or y_down == ">" or y_down == "<" or y_down == "v" or y_down == "+" or y_down == "c" or y_down == "H":
        e_move_down = False
    if x_right == "#" or x_right == "^" or x_right == ">" or x_right == "<" or x_right == "v" or x_right == "+" or x_right == "c" or x_right == "H":
        e_move_right = False
    if x_left == "#" or x_left == "^" or x_left == ">" or x_left == "<" or x_left == "v" or x_left == "+" or x_left == "c" or x_left == "H":
        e_move_left = False

    if e_move_up == True and player_y > enemy_y:
        enemy_y = enemy_y + 1
    if e_move_down == True and player_y < enemy_y:
        enemy_y = enemy_y - 1
    if e_move_right == True and player_x > enemy_x:
        enemy_x = enemy_x + 1
    if e_move_left == True and player_x < enemy_x:
        enemy_x = enemy_x - 1


def evaluate():
    global player_x
    global player_y
    global loop
    global current_level
    global score
    global lives
    if player_x == enemy_x and player_y == enemy_y:
        score = 0
        lives = lives - 1
        new_level()
    if lives == 0:
        print("You Lose!")
        time.sleep(1)
        play_again = input("press enter to replay")
        if play_again == '':
            current_level = 0
            score = 0
            lives = 5
            new_level()
        else:
            time.sleep(1)
            print("thank you for playing")
            time.sleep(1)
            exit()
    if player_x == 65 and player_y == 20:
        current_level = current_level + 1
        if current_level == 9:
            print("You Win !")
            time.sleep(1)
            play_again = input('press enter to replay')
            if play_again == '':
                current_level = 0
                new_level()
            else:
                time.sleep(1)
                print("thank you for playing")
                time.sleep(1)
                exit()
        new_level()


def replace():
    which_last_y = level_y[last_y]
    which_last_y[last_x] = '_'
    which_last_y = level_y[e_last_y]
    which_last_y[e_last_x] = '_'
    which_y = level_y[player_y]
    which_y[player_x] = 'O'
    which_y = level_y[enemy_y]
    which_y[enemy_x] = '*'
    which_y = level_y[20]
    which_y[65] = '+'
    level_y[0][73] = score
    level_y[1][73] = lives

def cls():
    _ = os.system("cls")


def strat_game():
    new_level()
    #
    while True:
        cls()
        take_inputs()
        evaluate()
        print_level()
        replace()
        time.sleep(.1)
strat_game()