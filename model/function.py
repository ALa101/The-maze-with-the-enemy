# import codeGame
from model.codeGame import *


def help():
    print("You are the player ( O )")
    print("You most accesses to (+) and don't touch *")
    print("You have 5 lives")
    print(" ( # ) is wall you can not through")
    print(" < , > , ^ , v  well kil you if you touch them")
    print("  H  increse lives +1 ")

def main_menu():
    while True:
        print("1.Start new Game.")
        print("2.Open save Game.")
        print("3.See help.")
        print("4.Eixt")
        chose = input("chose :")
        while chose not in ["1", "2", "3", "4"]:
            chose = input("chose from (1 - 4):")
        if chose == "1":
            strat_game()
        elif chose == "2":
            open_save()
            strat_game()
        elif chose == "3":
            help()
        else:
            exit()




