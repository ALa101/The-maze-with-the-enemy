import time
import keyboard
from sys import exit
import pickle
import os
import pyfiglet
from model import save_class
from model import function
from model.save_class import saved
from art import tprint
# import save_class
# from save_class import saved

current_level = 0
# The eight levels to be played from the file from levels.txt
all_levels = [0, 27, 54, 81, 108, 135, 162, 189]
saved_variables = save_class.saved(0, 0, 0)  # this to save the game

level_y = [[] for a in range(24)]  # this row of the game

player_x = 6  # the start point in X line ( 0 player )
player_y = 3
last_x = 6  # the last point ( player )
last_y = 3
enemy_x = 65  # the start point ( enemy * )
enemy_y = 20
e_last_x = 56
e_last_y = 20
lives = 5  # number fo lives
score = 0
loop = True


# saved_variables =


def print_level():  # this print all level
    for row in level_y:
        print(*row, sep='')


def clear_level():
    for row in level_y:  # this clear level_y ( row )
        row.clear()


def new_level():  # function git level from level.txt and set in level_y ( list [list])
    global player_x
    global player_y
    global enemy_x
    global enemy_y
    enemy_x = 65
    enemy_y = 20
    player_x = 6
    player_y = 3
    clear_level()
    byte = all_levels[current_level]  # take the current_level to start with it
    # all_levels = [0, 27, 54, 81, 108, 135, 162, 189]
    range_value = byte  # start take from level.txt line
    range_value2 = byte + 24
    row = 0  # row from level.txt to level_y
    while byte in range(range_value, range_value2):
        read_file = open('levels.txt', 'r')
        read_line = read_file.readlines()  # read line by line
        final_answer = read_line[byte]
        byt = 0
        first = 0
        second = 1
        while byt in range(0, 72):  # 72 num of char in thr row
            # line_y = level_y[row]
            level_y[row].append(final_answer[first:second])  # read key by key
            first = first + 1
            second = second + 1
            byt = byt + 1
        byte = byte + 1
        row = row + 1

    level_y[0].append(">Score: ")
    level_y[0].append("")
    level_y[1].append(">Lives: ")
    level_y[1].append("")


def save():  # to save the game in save.txt
    global saved_variables
    global score
    global lives
    global player_x
    global player_y
    global enemy_x
    global enemy_y
    global current_level
    saved_variables = saved(score, lives, current_level)  # from class

    with open('save.txt', 'wb') as fp:
        pickle.dump(saved_variables, fp)  # to save as object
    print('saved to "save.txt"')
    time.sleep(1)
    pause_menu(0)


def open_save():  # open the save game
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
    score = saved_variables.score
    lives = saved_variables.lives
    current_level = saved_variables.current_level
    pause_menu(0)


def pause_menu(print_pause):
    if print_pause == 1:
        result = pyfiglet.figlet_format("PAUSE", font="5lineoblique")
        print(result)
    print('Enter :\n"c" To Resume.\n"q" to quit,\n"s" to save,\n"o" to open an existing game')

    while loop:
        if keyboard.is_pressed('c'):
            return
        if keyboard.is_pressed('q'):
            # return
            function.main_menu()
            exit()
        if keyboard.is_pressed('s'):
            save()
        if keyboard.is_pressed('o'):
            open_save()


def take_inputs():  # take from inputs.
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


def evaluate():  # Check game status
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
        if current_level == 8:
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


def replace():  # switch values
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


def cls():   # clear screen
    _ = os.system("cls")


def strat_game():
    new_level()

    while True:
        cls()
        take_inputs()
        evaluate()
        print_level()
        replace()
        time.sleep(.1)


def open_levle():
    global current_level
    while True:
        try:
            level = int(input("Enter the level you want to play :"))
            if level > 0 and level < 8:
                current_level = level
                break
            else:
                print( "plcae chose level(1 - 7)")
        except:
            print("place Enter number ( 0 - 7)  not char ")
    startGame = input("press Enter to Start game with level -> (" + str(current_level) + " )or any key to back menu")
    if startGame == "":
        strat_game()
    else:
        return




