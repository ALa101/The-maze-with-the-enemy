# import codeGame
from colorama import Fore, Style

from model.codeGame import *


def help():
    print("1.You are the player ( O )".center(80))
    print("2.You most accesses to (+) and don't touch *".center(80))
    print("3.You have 5 lives".center(80))
    print("4.( # ) is wall you can not through".center(80))
    print("5.< , > , ^ , v  well kil you if you touch them".center(80))
    print("6.H  increase lives +1 ".center(80))


def main_menu():
    print(Fore.BLUE)
    tprint('Hellow  in  my   Game'.center(50))
    while True:
        print(Fore.GREEN + "1.Start new Game.")
        print("2.Open save Game.")
        print("3.Open level")
        print("4.See help.")
        print("5.Ext")

        chose = input(Style.RESET_ALL + "Enter your chose :")
        while chose not in ["1", "2", "3", "4"]:
            chose = input("chose from (1 - 4):")
        if chose == "1":
            strat_game()
        elif chose == "2":
            open_save()
            strat_game()
        elif chose == "3":
            open_levle()
        elif chose == "4":
            help()
        else:
            exit()




